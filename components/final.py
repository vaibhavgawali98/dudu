"""Screen 11 — Final closing message."""

import streamlit as st

from config import content as c
from utils.helpers import floating_petals, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("final"):
        background_music(c.BACKGROUND_MUSIC["final"], key="final", volume=c.BACKGROUND_MUSIC_VOLUME)

    floating_petals(10)
    md_html(
        f"""
        <div class="screen screen-center" style="min-height:92vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:1.2rem;">
                <div style="font-size:2.2rem;">❤️</div>
                <p class="body-text" style="text-align:center; max-width:300px; font-size:1.05rem;">
                    {c.FINAL_MESSAGE_LINE_1}
                </p>
                <p class="script-text" style="font-size:1.4rem; text-align:center;">
                    {c.FINAL_MESSAGE_LINE_2}
                </p>
                <div class="eyebrow" style="margin-top:1rem;">{c.FINAL_SIGNATURE}</div>
            </div>
        </div>
        """
    )
