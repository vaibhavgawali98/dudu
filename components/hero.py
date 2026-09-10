"""Screen 1 — Welcome / hero screen."""

import streamlit as st

from config import content as c
from utils.helpers import go_to, background_path, image_data_uri, floating_petals, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("hero"):
        background_music(c.BACKGROUND_MUSIC["hero"], key="hero", volume=c.BACKGROUND_MUSIC_VOLUME)

    from utils.helpers import BACKGROUNDS_DIR
    bg_uri = image_data_uri(c.HERO_BACKGROUND_IMAGE, directory=BACKGROUNDS_DIR)

    if bg_uri:
        bg_style = (
            f"background-image: linear-gradient(180deg, rgba(10,3,8,0.35) 0%, "
            f"rgba(10,3,8,0.55) 55%, rgba(10,3,8,0.95) 100%), url('{bg_uri}');"
            f"background-size: cover; background-position: center;"
        )
    else:
        bg_style = (
            "background: radial-gradient(ellipse at 50% 20%, var(--color-burgundy-light) 0%, "
            "var(--color-wine) 45%, var(--color-black) 100%);"
        )

    md_html(
        f"""
        <div class="hero-wrap" style="{bg_style}">
            <div class="hero-inner anim-fade-up">
                <div class="eyebrow">{c.SITE_TITLE}</div>
                <h1 class="hero-title serif-title">{c.HERO_TITLE} ❤️</h1>
                <p class="script-text hero-subtitle">{c.HERO_SUBTITLE}</p>
                <p class="body-text" style="max-width:340px; margin: 0.8rem auto 0 auto;">{c.HERO_BODY}</p>
            </div>
        </div>
        <style>
        .hero-wrap {{
            min-height: 88vh;
            border-radius: 26px;
            display: flex;
            align-items: flex-end;
            padding: 2rem 1.4rem 2.2rem 1.4rem;
            position: relative;
            overflow: hidden;
            box-shadow: var(--shadow-soft);
            border: 1px solid rgba(212,175,55,0.15);
        }}
        .hero-inner {{ text-align: center; width: 100%; }}
        </style>
        """
    )

    floating_petals(10)

    st.write("")
    if st.button(c.HERO_BUTTON, use_container_width=True, type="primary"):
        go_to("story")
