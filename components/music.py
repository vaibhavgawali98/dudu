"""Screen 6 — Our Song, with a self-contained HTML5 audio player.

The player is built as one self-sufficient HTML snippet (rendered via
st.components.v1.html) so its play/pause JavaScript executes reliably
inside its own sandboxed frame -- a Streamlit limitation we work
around deliberately rather than fighting. Autoplay is never attempted;
the browser requires an explicit tap on Play, which this respects.
"""

import streamlit as st
import streamlit.components.v1 as components

from config import content as c
from utils.helpers import go_to, audio_data_uri, md_html


def render():
    md_html(
        f"""
        <div class="screen screen-center">
            <div class="eyebrow">chapter four</div>
            <h2 class="section-title serif-title">{c.MUSIC_SECTION_TITLE}</h2>
            <p class="script-text">{c.MUSIC_SECTION_SUBTITLE}</p>
        </div>
        """
    )

    src = audio_data_uri(c.SONG_FILENAME)

    if not src:
        md_html(
            '<div class="asset-placeholder">🎵 Add your song to '
            '<code>assets/music/</code> to enable this player.</div>'
        )
    else:
        artist_html = f'<div class="player-artist">{c.SONG_ARTIST}</div>' if c.SONG_ARTIST else ""
        player_html = f"""
        <div style="font-family: 'Poppins', sans-serif;">
        <style>
            .player-card {{
                background: linear-gradient(160deg, rgba(74,14,46,0.75), rgba(10,3,8,0.85));
                border: 1px solid rgba(212,175,55,0.35);
                border-radius: 20px;
                padding: 1.4rem 1.2rem;
                color: #f2e2c4;
                box-shadow: 0 10px 30px rgba(0,0,0,0.4);
                max-width: 420px;
                margin: 0 auto;
            }}
            .player-title {{ font-size: 1.05rem; font-weight: 500; margin-bottom: 2px; }}
            .player-artist {{ font-size: 0.8rem; opacity: 0.7; margin-bottom: 14px; }}
            .player-controls {{ display: flex; align-items: center; gap: 14px; }}
            .play-btn {{
                width: 52px; height: 52px; border-radius: 50%; border: none;
                background: linear-gradient(135deg, #4a0e2e, #e63950);
                color: #fbf3e7; font-size: 1.3rem; cursor: pointer;
                display: flex; align-items: center; justify-content: center;
                flex-shrink: 0; box-shadow: 0 6px 18px rgba(230,57,80,0.4);
            }}
            .progress-wrap {{
                flex: 1; height: 6px; border-radius: 4px;
                background: rgba(255,255,255,0.12); position: relative; cursor: pointer;
            }}
            .progress-fill {{
                height: 100%; border-radius: 4px; width: 0%;
                background: linear-gradient(90deg, #d4af37, #e63950);
            }}
            .time-row {{
                display:flex; justify-content:space-between; font-size:0.68rem;
                opacity:0.65; margin-top:6px;
            }}
        </style>
        <div class="player-card">
            <div class="player-title">{c.SONG_TITLE}</div>
            {artist_html}
            <div class="player-controls">
                <button class="play-btn" id="playBtn" onclick="toggleAudio()">▶</button>
                <div style="flex:1;">
                    <div class="progress-wrap" id="progressWrap" onclick="seekAudio(event)">
                        <div class="progress-fill" id="progressFill"></div>
                    </div>
                    <div class="time-row">
                        <span id="curTime">0:00</span>
                        <span id="durTime">0:00</span>
                    </div>
                </div>
            </div>
        </div>
        <audio id="ourSongAudio" src="{src}" preload="metadata"></audio>
        <script>
            const audio = document.getElementById('ourSongAudio');
            const playBtn = document.getElementById('playBtn');
            const progressFill = document.getElementById('progressFill');
            const progressWrap = document.getElementById('progressWrap');
            const curTime = document.getElementById('curTime');
            const durTime = document.getElementById('durTime');

            function formatTime(t) {{
                if (!isFinite(t)) return '0:00';
                const m = Math.floor(t / 60);
                const s = Math.floor(t % 60).toString().padStart(2, '0');
                return m + ':' + s;
            }}

            function toggleAudio() {{
                if (audio.paused) {{
                    audio.play();
                    playBtn.innerHTML = '❚❚';
                }} else {{
                    audio.pause();
                    playBtn.innerHTML = '▶';
                }}
            }}

            function seekAudio(e) {{
                const rect = progressWrap.getBoundingClientRect();
                const ratio = (e.clientX - rect.left) / rect.width;
                if (isFinite(audio.duration)) {{
                    audio.currentTime = ratio * audio.duration;
                }}
            }}

            audio.addEventListener('loadedmetadata', () => {{
                durTime.textContent = formatTime(audio.duration);
            }});
            audio.addEventListener('timeupdate', () => {{
                const pct = (audio.currentTime / audio.duration) * 100 || 0;
                progressFill.style.width = pct + '%';
                curTime.textContent = formatTime(audio.currentTime);
            }});
            audio.addEventListener('ended', () => {{
                playBtn.innerHTML = '▶';
            }});
        </script>
        </div>
        """
        components.html(player_html, height=150)

    st.write("")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("← Back", key="music_back", use_container_width=True):
            go_to("letter")
    with col2:
        if st.button("Continue →", key="music_next",
                     use_container_width=True, type="primary"):
            go_to("surprises")
