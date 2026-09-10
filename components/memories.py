"""Screens 3 & 4 — Our Memories gallery and individual memory detail."""

import streamlit as st

from config import content as c
from utils.helpers import go_to, image_data_uri, photo_path, md_html, background_music


def _render_detail(index: int):
    """Screen 4 — full detail view for a single tapped memory."""
    memory = c.MEMORIES[index]
    uri = image_data_uri(memory["filename"])

    md_html('<div class="screen">')

    if st.button("← Back to gallery", key="memory_detail_back"):
        st.session_state["selected_memory"] = None
        st.rerun()

    if uri:
        md_html(
            f'<img src="{uri}" class="detail-photo anim-fade-in" />'
        )
    else:
        md_html(
            '<div class="asset-placeholder" style="height:260px; '
            'display:flex; align-items:center; justify-content:center;">'
            '🖼️ Photo coming soon</div>'
        )

    meta_bits = [b for b in [memory.get("date"), memory.get("location")] if b]
    meta_line = " · ".join(meta_bits)

    md_html(
        f"""
        <div class="glass-card anim-fade-up" style="margin-top:1rem;">
            {f'<div class="eyebrow">{meta_line}</div>' if meta_line else ''}
            <div class="serif-title" style="font-size:1.2rem; margin:0.4rem 0;">
                {memory['caption']}
            </div>
            <div class="body-text">{memory.get('detail', '')}</div>
        </div>
        <style>
        .detail-photo {{
            width: 100%; border-radius: 20px; box-shadow: var(--shadow-soft);
            border: 1px solid rgba(212,175,55,0.2);
        }}
        </style>
        """
    )
    md_html("</div>")


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("memories"):
        background_music(c.BACKGROUND_MUSIC["memories"], key="memories", volume=c.BACKGROUND_MUSIC_VOLUME)

    if "selected_memory" not in st.session_state:
        st.session_state["selected_memory"] = None

    if st.session_state["selected_memory"] is not None:
        _render_detail(st.session_state["selected_memory"])
        return

    md_html(
        f"""
        <div class="screen">
            <div class="eyebrow" style="text-align:center;">chapter two</div>
            <h2 class="section-title serif-title" style="text-align:center;">{c.MEMORIES_TITLE}</h2>
            <p class="script-text" style="text-align:center; margin-bottom:1.4rem;">
                {c.MEMORIES_SUBTITLE}
            </p>
        </div>
        """
    )

    md_html('<div class="gallery-grid">')
    available = []
    for i, memory in enumerate(c.MEMORIES):
        uri = image_data_uri(memory["filename"])
        stagger = f"stagger-{min(i + 1, 6)}"
        if uri:
            available.append(i)
            md_html(
                f"""
                <div class="gallery-tile scroll-reveal {stagger}">
                    <img src="{uri}" />
                    <div class="gallery-caption">{memory['caption'][:40]}</div>
                </div>
                """
            )
        else:
            md_html(
                '<div class="gallery-tile asset-placeholder" style="height:150px; '
                'display:flex; align-items:center; justify-content:center;">🖼️</div>'
            )
    md_html("</div>")

    md_html(
        """
        <style>
        .gallery-grid {
            display: grid; grid-template-columns: repeat(2, 1fr);
            gap: 0.6rem; margin-bottom: 1rem;
        }
        .gallery-tile {
            border-radius: 16px; overflow: hidden; position: relative;
            box-shadow: 0 6px 18px rgba(0,0,0,0.4);
            border: 1px solid rgba(212,175,55,0.15);
        }
        .gallery-tile img {
            width: 100%; height: 150px; object-fit: cover; display: block;
        }
        .gallery-caption {
            position: absolute; bottom: 0; left: 0; right: 0;
            padding: 0.4rem 0.5rem;
            background: linear-gradient(to top, rgba(10,3,8,0.85), transparent);
            font-size: 0.72rem; color: var(--color-champagne);
        }
        </style>
        """
    )

    # Tap-to-open buttons (kept as real Streamlit buttons for reliable
    # interaction — styled to sit invisibly under each tile via layout).
    if available:
        st.caption("Tap a memory to read more about it")
        cols = st.columns(2)
        for n, i in enumerate(available):
            with cols[n % 2]:
                if st.button(f"Open memory {i + 1}", key=f"open_memory_{i}",
                             use_container_width=True):
                    st.session_state["selected_memory"] = i
                    st.rerun()

    st.write("")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("← Back", key="memories_back", use_container_width=True):
            go_to("story")
    with col2:
        if st.button("Read Our Letter →", key="memories_next",
                     use_container_width=True, type="primary"):
            go_to("letter")
