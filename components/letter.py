"""Screen 5 — Love letter, with an envelope-opening reveal."""

import streamlit as st

from config import content as c
from utils.helpers import go_to, floating_petals, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("letter"):
        background_music(c.BACKGROUND_MUSIC["letter"], key="letter", volume=c.BACKGROUND_MUSIC_VOLUME)

    if "envelope_opened" not in st.session_state:
        st.session_state["envelope_opened"] = False

    md_html(
        f"""
        <div class="screen screen-center">
            <div class="eyebrow">chapter three</div>
            <h2 class="section-title serif-title">{c.LETTER_TITLE}</h2>
        </div>
        """
    )

    if not st.session_state["envelope_opened"]:
        md_html(
            """
            <div class="envelope-wrap anim-fade-up">
                <div class="envelope">
                    <div class="envelope-flap"></div>
                    <div class="envelope-heart">❤️</div>
                </div>
            </div>
            <style>
            .envelope-wrap { display:flex; justify-content:center; margin: 1.4rem 0; }
            .envelope {
                width: 220px; height: 150px; position: relative;
                background: linear-gradient(160deg, var(--color-burgundy), var(--color-wine));
                border-radius: 10px; box-shadow: var(--shadow-soft);
                border: 1px solid rgba(212,175,55,0.35);
                display: flex; align-items: center; justify-content: center;
            }
            .envelope-flap {
                position: absolute; top: 0; left: 0; width: 0; height: 0;
                border-left: 110px solid transparent;
                border-right: 110px solid transparent;
                border-top: 75px solid var(--color-burgundy-light);
                filter: drop-shadow(0 3px 6px rgba(0,0,0,0.3));
            }
            .envelope-heart {
                font-size: 1.8rem; z-index: 2; animation: gentlePulse 2.4s ease-in-out infinite;
            }
            </style>
            """
        )
        st.write("")
        cols = st.columns([1, 2, 1])
        with cols[1]:
            if st.button("Open the letter ❤️", use_container_width=True, type="primary"):
                st.session_state["envelope_opened"] = True
                st.rerun()
    else:
        floating_petals(6)
        body_html = c.LETTER_BODY.strip().replace("\n\n", "</p><p>").replace("\n", "<br/>")
        signature_html = c.LETTER_SIGNATURE.replace("\n", "<br/>")
        md_html(
            f"""
            <div class="letter-paper anim-fade-up">
                <div class="script-text" style="font-size:1.3rem; margin-bottom:0.8rem;">
                    {c.LETTER_SALUTATION}
                </div>
                <div class="body-text letter-body"><p>{body_html}</p></div>
                <div class="script-text" style="margin-top:1.2rem; font-size:1.15rem;">
                    {signature_html}
                </div>
            </div>
            <style>
            .letter-paper {{
                background: linear-gradient(170deg, #fbf3e7 0%, #f2e2c4 100%);
                color: #3a1220;
                border-radius: 14px;
                padding: 1.8rem 1.4rem;
                box-shadow: var(--shadow-soft);
                position: relative;
                border: 1px solid rgba(212,175,55,0.5);
            }}
            .letter-paper .script-text {{ color: #7a1436; }}
            .letter-body {{ color: rgba(58,18,32,0.85) !important; font-size: 0.95rem; }}
            .letter-body p {{ margin: 0 0 0.8rem 0; }}
            </style>
            """
        )

    st.write("")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("← Back", key="letter_back", use_container_width=True):
            go_to("memories")
    with col2:
        if st.button("Continue →", key="letter_next",
                     use_container_width=True, type="primary"):
            go_to("music")
