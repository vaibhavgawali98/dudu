"""Screen 7 — Hidden surprises / easter eggs.

Each surprise is independently toggleable from config/content.py and
implemented with plain Streamlit widgets + session_state, so every
interaction is 100% reliable (no custom JS click-handlers needed).
"""

import streamlit as st

from config import content as c
from utils.helpers import go_to, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("surprises"):
        background_music(c.BACKGROUND_MUSIC["surprises"], key="surprises", volume=c.BACKGROUND_MUSIC_VOLUME)

    md_html(
        """
        <div class="screen">
            <div class="eyebrow" style="text-align:center;">chapter five</div>
            <h2 class="section-title serif-title" style="text-align:center;">A Few Secrets</h2>
            <p class="script-text" style="text-align:center; margin-bottom:1.2rem;">
                Some things I've been keeping for the right moment.
            </p>
        </div>
        """
    )

    any_surprise = False

    # ---- Heart tap surprise ------------------------------------------------
    if c.ENABLE_HEART_TAP_SURPRISE:
        any_surprise = True
        taps = st.session_state.get("heart_taps", 0)
        with st.container():
            md_html('<div class="glass-card" style="margin-bottom:1rem; text-align:center;">')
            if taps < c.HEART_TAP_TARGET:
                md_html(
                    f'<div class="body-text" style="margin-bottom:0.6rem;">'
                    f"Tap the heart {c.HEART_TAP_TARGET} times...</div>"
                )
                if st.button("❤️", key="heart_tap_btn", use_container_width=True):
                    st.session_state["heart_taps"] = taps + 1
                    st.rerun()
                st.caption(f"{taps} / {c.HEART_TAP_TARGET}")
            else:
                md_html(
                    f'<div class="script-text anim-fade-in" style="font-size:1.05rem;">'
                    f'{c.HEART_TAP_MESSAGE}</div>'
                )
            md_html("</div>")

    # ---- Secret memory -------------------------------------------------------
    if c.ENABLE_SECRET_MEMORY:
        any_surprise = True
        with st.container():
            md_html('<div class="glass-card" style="margin-bottom:1rem;">')
            if not st.session_state.get("secret_memory_revealed"):
                md_html(f'<div class="body-text">{c.SECRET_MEMORY_TEASER}</div>')
                if st.button("Reveal", key="secret_memory_btn", use_container_width=True):
                    st.session_state["secret_memory_revealed"] = True
                    st.rerun()
            else:
                md_html(
                    f'<div class="script-text anim-fade-in" style="font-size:1.05rem;">'
                    f'{c.SECRET_MEMORY_TEXT}</div>'
                )
            md_html("</div>")

    # ---- One more thing -------------------------------------------------------
    if c.ENABLE_ONE_MORE_THING:
        any_surprise = True
        with st.container():
            md_html('<div class="glass-card" style="margin-bottom:1rem;">')
            if not st.session_state.get("one_more_thing_revealed"):
                if st.button(f"✨ {c.ONE_MORE_THING_TEASER}", key="one_more_btn",
                             use_container_width=True):
                    st.session_state["one_more_thing_revealed"] = True
                    st.rerun()
            else:
                md_html(
                    f'<div class="script-text anim-fade-in" style="font-size:1.05rem;">'
                    f'{c.ONE_MORE_THING_TEXT}</div>'
                )
            md_html("</div>")

    if not any_surprise:
        md_html(
            '<div class="body-text" style="text-align:center; opacity:0.6;">'
            "(No surprises enabled right now.)</div>"
        )

    st.write("")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("← Back", key="surprises_back", use_container_width=True):
            go_to("music")
    with col2:
        if st.button("Keep going →", key="surprises_next",
                     use_container_width=True, type="primary"):
            go_to("buildup")
