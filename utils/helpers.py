"""
Utility helpers: asset loading, base64 encoding, CSS injection,
and screen navigation. Everything here is written to fail
gracefully — a missing photo or song must never crash the app.
"""

import base64
import os
import streamlit as st

# ---------------------------------------------------------------
# Paths
# ---------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
PHOTOS_DIR = os.path.join(ASSETS_DIR, "photos")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
BACKGROUNDS_DIR = os.path.join(ASSETS_DIR, "backgrounds")
ICONS_DIR = os.path.join(ASSETS_DIR, "icons")
STYLES_DIR = os.path.join(BASE_DIR, "styles")


# ---------------------------------------------------------------
# Screen order — used by the progress indicator & navigation
# ---------------------------------------------------------------
SCREENS = [
    "loading",
    "hero",
    "story",
    "memories",
    "letter",
    "music",
    "surprises",
    "buildup",
    "proposal",
    "celebration",
    "final",
]


def init_session_state():
    """Set up every piece of session state the app relies on."""
    defaults = {
        "screen": "loading",
        "loaded": False,
        "heart_taps": 0,
        "secret_memory_revealed": False,
        "one_more_thing_revealed": False,
        "proposal_answer": None,
        "no_button_dodges": 0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def go_to(screen_name: str):
    """Navigate to a given screen and rerun immediately."""
    st.session_state["screen"] = screen_name
    st.rerun()


def screen_progress():
    """Return (index, total) of the current screen for a progress dot UI."""
    try:
        idx = SCREENS.index(st.session_state["screen"])
    except (KeyError, ValueError):
        idx = 0
    return idx, len(SCREENS)


# ---------------------------------------------------------------
# Asset helpers — all of these fail gracefully (return None)
# ---------------------------------------------------------------
def _safe_path(directory: str, filename: str):
    if not filename:
        return None
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        return path
    return None


def photo_path(filename: str):
    return _safe_path(PHOTOS_DIR, filename)


def music_path(filename: str):
    return _safe_path(MUSIC_DIR, filename)


def background_path(filename: str):
    return _safe_path(BACKGROUNDS_DIR, filename)


def file_to_base64(path: str) -> str:
    """Read any file and return a base64 string. Returns '' if missing."""
    if not path or not os.path.isfile(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def image_data_uri(filename: str, directory: str = PHOTOS_DIR) -> str:
    """Return a data: URI for an image, or '' if the file is missing."""
    path = _safe_path(directory, filename)
    if not path:
        return ""
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    b64 = file_to_base64(path)
    if not b64:
        return ""
    return f"data:image/{mime};base64,{b64}"


def audio_data_uri(filename: str) -> str:
    path = music_path(filename)
    if not path:
        return ""
    b64 = file_to_base64(path)
    if not b64:
        return ""
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "mpeg" if ext == "mp3" else ext
    return f"data:audio/{mime};base64,{b64}"


def background_music(filename: str, key: str, volume: float = 0.35):
    """Loop a quiet background track for the current chapter.

    Missing files are skipped silently (never crashes). Chrome blocks
    audio-with-sound autoplay until the visitor has interacted with the
    page at least once — since every chapter here is reached via a
    button tap, that's almost always already satisfied by the time
    this runs. If a browser still blocks it, a small "tap for music"
    pill appears in the corner instead of failing with no feedback.
    `key` must be unique per chapter so each one gets its own player
    and the previous chapter's track stops when you navigate away.
    """
    import streamlit.components.v1 as components

    src = audio_data_uri(filename)
    if not src:
        return

    components.html(
        f"""
        <audio id="bgm-{key}" src="{src}" loop autoplay playsinline></audio>
        <button id="bgm-btn-{key}" onclick="
            document.getElementById('bgm-{key}').play();
            this.style.display='none';
        " style="display:none; position:fixed; bottom:16px; right:16px; z-index:9999;
            background:rgba(74,14,46,0.9); color:#f2e2c4;
            border:1px solid rgba(212,175,55,0.55); border-radius:999px;
            padding:8px 14px; font-size:0.78rem; font-family:sans-serif;
            cursor:pointer; box-shadow:0 4px 14px rgba(0,0,0,0.4);">
            🔈 Tap for music
        </button>
        <script>
            const a = document.getElementById('bgm-{key}');
            a.volume = {volume};
            const btn = document.getElementById('bgm-btn-{key}');
            const playPromise = a.play();
            if (playPromise !== undefined) {{
                playPromise.catch(() => {{ btn.style.display = 'block'; }});
            }}
        </script>
        """,
        height=0,
    )


# ---------------------------------------------------------------
# CSS / styling
# ---------------------------------------------------------------
def md_html(content: str):
    """Render an HTML/CSS/JS snippet safely via st.markdown.

    Streamlit's markdown parser treats any line indented 4+ spaces as a
    literal code block. Because our HTML is written inside indented
    Python f-strings, every call site needs its per-line leading
    whitespace stripped before rendering, or the browser shows raw
    markup instead of the rendered page. This helper does that in one
    place so every component can just call md_html(f\"\"\"...\"\"\") safely.
    """
    stripped = "\n".join(line.lstrip() for line in content.split("\n"))
    st.markdown(stripped, unsafe_allow_html=True)


def load_css():
    """Inject every stylesheet in /styles into the page, in order."""
    css_files = ["main.css", "mobile.css", "animations.css"]
    combined = ""
    for filename in css_files:
        path = os.path.join(STYLES_DIR, filename)
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                combined += f.read() + "\n"
    md_html(f"<style>{combined}</style>")


def hide_streamlit_chrome():
    """Remove Streamlit's default header/footer/menu/padding for an
    immersive, non-templated feel."""
    md_html(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        div[data-testid="stToolbar"] {visibility: hidden; height: 0;}
        div[data-testid="stDecoration"] {visibility: hidden; height: 0;}
        div[data-testid="stStatusWidget"] {visibility: hidden;}
        .block-container {
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            padding-left: 0.6rem !important;
            padding-right: 0.6rem !important;
            max-width: 560px !important;
        }
        [data-testid="stAppViewContainer"] {
            background: #0a0308;
        }
        [data-testid="stVerticalBlock"] { gap: 0.4rem; }
        </style>
        """
    )


def floating_petals(count: int = 14):
    """Render a purely-CSS layer of floating hearts/petals. Cheap and
    GPU-friendly — no JavaScript required."""
    import random

    pieces = []
    symbols = ["❤️", "🌹", "✨", "💕"]
    for i in range(count):
        left = random.randint(0, 100)
        delay = round(random.uniform(0, 12), 2)
        duration = round(random.uniform(10, 20), 2)
        size = round(random.uniform(0.7, 1.4), 2)
        symbol = random.choice(symbols)
        pieces.append(
            f'<span class="petal" style="left:{left}%; '
            f"animation-delay:{delay}s; animation-duration:{duration}s; "
            f'font-size:{size}rem;">{symbol}</span>'
        )
    md_html(
        f'<div class="petal-layer">{"".join(pieces)}</div>'
    )


def progress_dots():
    """Small, unobtrusive progress indicator for the top of the screen."""
    idx, total = screen_progress()
    if st.session_state["screen"] in ("loading",):
        return
    dots = ""
    for i in range(total - 1):  # exclude the loading screen from the count
        active = "active" if i == idx - 1 else ""
        dots += f'<span class="dot {active}"></span>'
    md_html(
        f'<div class="progress-track"><div class="progress-dots">{dots}</div></div>'
    )


def nav_buttons(back_screen: str = None, next_label: str = "Continue",
                 next_screen: str = None, show_back: bool = True):
    """Consistent Back / Continue navigation used across screens."""
    cols = st.columns([1, 2]) if (back_screen and show_back) else st.columns([1])
    if back_screen and show_back:
        with cols[0]:
            if st.button("← Back", key=f"back_{back_screen}_{next_screen}",
                         use_container_width=True):
                go_to(back_screen)
        with cols[1]:
            if st.button(next_label, key=f"next_{next_screen}",
                         use_container_width=True, type="primary"):
                go_to(next_screen)
    else:
        with cols[0]:
            if st.button(next_label, key=f"next_only_{next_screen}",
                         use_container_width=True, type="primary"):
                go_to(next_screen)
