"""Screen 0 — Cinematic loading screen."""

import time
import streamlit as st

from config import content as c
from utils.helpers import go_to, md_html


def render():
    md_html(
        f"""
        <div class="screen screen-center" style="min-height: 100vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:1.1rem;">
                <div class="big-heart anim-pulse" style="font-size:3.2rem;">❤️</div>
                <div class="eyebrow">{c.SITE_TITLE}</div>
                <div class="script-text" style="font-size:1.3rem; text-align:center; max-width:280px;">
                    {c.LOADING_TEXT} {c.LOADING_SUBTEXT}
                </div>
                <div class="loader-bar"><div class="loader-fill"></div></div>
            </div>
        </div>
        <style>
        .loader-bar {{
            width: 160px; height: 3px; border-radius: 3px;
            background: rgba(242,226,196,0.15); overflow: hidden; margin-top: 0.4rem;
        }}
        .loader-fill {{
            width: 40%; height: 100%; border-radius: 3px;
            background: linear-gradient(90deg, var(--color-gold), var(--color-rose));
            animation: loaderSlide 1.1s ease-in-out infinite;
        }}
        @keyframes loaderSlide {{
            0% {{ transform: translateX(-100%); }}
            100% {{ transform: translateX(350%); }}
        }}
        </style>
        """
    )

    if not st.session_state.get("loaded"):
        time.sleep(1.4)  # short, elegant — not a long fake wait
        st.session_state["loaded"] = True
        go_to("hero")
