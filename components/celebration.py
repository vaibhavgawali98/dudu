"""Screen 10 — She Said Yes! A confetti/petal celebration climax."""

import random
import streamlit as st

from config import content as c
from utils.helpers import go_to, md_html, background_music


def _confetti(count: int = 40):
    colors = ["#e63950", "#d4af37", "#f6b8cf", "#f2e2c4", "#6e1a3f"]
    pieces = []
    for _ in range(count):
        left = random.randint(0, 100)
        delay = round(random.uniform(0, 2.2), 2)
        duration = round(random.uniform(2.6, 4.6), 2)
        color = random.choice(colors)
        size = random.randint(6, 12)
        shape = "border-radius:50%;" if random.random() > 0.5 else "border-radius:2px;"
        pieces.append(
            f'<span class="confetti-piece" style="left:{left}%; '
            f"animation-delay:{delay}s; animation-duration:{duration}s; "
            f"width:{size}px; height:{size}px; background:{color}; {shape}\"></span>"
        )
    md_html(
        f"""
        <div class="confetti-layer">{''.join(pieces)}</div>
        <style>
        .confetti-layer {{ position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 5; }}
        .confetti-piece {{ position: absolute; top: -5%; animation-name: confettiFall;
            animation-timing-function: ease-in; animation-iteration-count: infinite; opacity: 0.9; }}
        </style>
        """
    )


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("celebration"):
        background_music(c.BACKGROUND_MUSIC["celebration"], key="celebration", volume=c.BACKGROUND_MUSIC_VOLUME)

    _confetti(46)

    md_html(
        f"""
        <div class="screen screen-center" style="min-height:90vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:1rem;">
                <div style="font-size:4rem;" class="anim-pulse">💍❤️</div>
                <h1 class="serif-title anim-glow" style="font-size:2rem; text-align:center;
                    padding:0.4rem 1rem; border-radius:16px;">
                    {c.YES_HEADLINE}
                </h1>
                <p class="script-text" style="font-size:1.15rem; text-align:center;">{c.YES_SUBTEXT}</p>
                <div class="glass-card anim-fade-up" style="margin-top:0.6rem;">
                    <div class="body-text" style="text-align:center;">{c.YES_MESSAGE}</div>
                </div>
            </div>
        </div>
        """
    )

    st.write("")
    cols = st.columns([1, 3, 1])
    with cols[1]:
        if st.button("Continue ❤️", use_container_width=True, type="primary"):
            go_to("final")
