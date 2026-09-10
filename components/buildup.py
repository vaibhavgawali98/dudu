"""Screen 8 — Build-up before the proposal reveal."""

import streamlit as st

from config import content as c
from utils.helpers import go_to, floating_petals, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("buildup"):
        background_music(c.BACKGROUND_MUSIC["buildup"], key="buildup", volume=c.BACKGROUND_MUSIC_VOLUME)

    md_html(
        f"""
        <div class="screen screen-center" style="min-height:88vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:1rem;">
                <div class="big-heart anim-glow" style="font-size:3.6rem; padding:1.4rem;
                     border-radius:50%; background:radial-gradient(circle, rgba(230,57,80,0.18), transparent 70%);">
                    💌
                </div>
                <h2 class="serif-title" style="font-size:1.6rem; text-align:center; max-width:300px;">
                    {c.BUILDUP_TITLE}
                </h2>
                <p class="script-text" style="font-size:1.2rem;">{c.BUILDUP_SUBTITLE}</p>
            </div>
        </div>
        """
    )

    floating_petals(8)

    st.write("")
    cols = st.columns([1, 3, 1])
    with cols[1]:
        if st.button(c.BUILDUP_BUTTON, use_container_width=True, type="primary"):
            go_to("proposal")

    st.write("")
    if st.button("← Back", key="buildup_back", use_container_width=True):
        go_to("surprises")
