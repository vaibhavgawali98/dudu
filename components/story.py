"""Screen 2 — Our Story: interactive vertical timeline."""

import streamlit as st

from config import content as c
from utils.helpers import go_to, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("story"):
        background_music(c.BACKGROUND_MUSIC["story"], key="story", volume=c.BACKGROUND_MUSIC_VOLUME)

    md_html(
        """
        <div class="screen">
            <div class="eyebrow" style="text-align:center;">chapter one</div>
            <h2 class="section-title serif-title" style="text-align:center;">Our Story</h2>
            <p class="script-text" style="text-align:center; margin-bottom:1.6rem;">
                Scroll to relive it with me.
            </p>
        </div>
        """
    )

    md_html('<div class="timeline">')
    total = len(c.TIMELINE)
    for i, item in enumerate(c.TIMELINE):
        is_last = i == total - 1
        stagger = f"stagger-{min(i + 1, 6)}"
        date_html = (
            f'<div class="eyebrow" style="margin-bottom:2px;">{item["date"]}</div>'
            if item.get("date")
            else ""
        )
        md_html(
            f"""
            <div class="timeline-row">
                <div class="timeline-rail">
                    <div class="timeline-dot">{item['icon']}</div>
                    {'' if is_last else '<div class="timeline-line"></div>'}
                </div>
                <div class="timeline-item scroll-reveal {stagger} glass-card">
                    {date_html}
                    <div class="serif-title" style="font-size:1.15rem; margin-bottom:0.3rem;">
                        {item['title']}
                    </div>
                    <div class="body-text" style="font-size:0.92rem;">{item['description']}</div>
                </div>
            </div>
            """
        )
    md_html("</div>")

    md_html(
        """
        <style>
        .timeline { display: flex; flex-direction: column; }
        .timeline-row { display: flex; gap: 0.8rem; align-items: stretch; }
        .timeline-rail { display: flex; flex-direction: column; align-items: center; width: 34px; }
        .timeline-dot {
            width: 34px; height: 34px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: linear-gradient(135deg, var(--color-burgundy), var(--color-rose));
            border: 1px solid rgba(212,175,55,0.5);
            font-size: 1rem; flex-shrink: 0;
            box-shadow: 0 0 14px rgba(230,57,80,0.35);
        }
        .timeline-line {
            flex: 1; width: 2px; min-height: 26px;
            background: linear-gradient(to bottom, rgba(212,175,55,0.5), rgba(212,175,55,0.05));
            margin: 4px 0;
        }
        .timeline-item { flex: 1; margin-bottom: 1rem; }
        </style>
        """
    )

    st.write("")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("← Back", key="story_back", use_container_width=True):
            go_to("hero")
    with col2:
        if st.button("See Our Memories →", key="story_next",
                     use_container_width=True, type="primary"):
            go_to("memories")
