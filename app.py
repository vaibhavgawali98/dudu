"""
=====================================================================
  OUR FOREVER ❤️  —  app.py
=====================================================================
  Main entry point. This file only wires screens together — all the
  actual content lives in config/content.py, and all the visual
  design lives in styles/*.css. You should not need to edit this
  file to personalize the site; see README.md.
=====================================================================
"""

import streamlit as st

from config import content as c
from utils.helpers import init_session_state, load_css, hide_streamlit_chrome, progress_dots

from components import (
    loading,
    hero,
    story,
    memories,
    letter,
    music,
    surprise,
    buildup,
    proposal,
    celebration,
    final,
)

# ---------------------------------------------------------------
# Page configuration — must be the first Streamlit call
# ---------------------------------------------------------------
st.set_page_config(
    page_title=c.SITE_TITLE,
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

hide_streamlit_chrome()
load_css()
init_session_state()

# ---------------------------------------------------------------
# Routing table — maps a screen name to its render() function
# ---------------------------------------------------------------
SCREEN_RENDERERS = {
    "loading": loading.render,
    "hero": hero.render,
    "story": story.render,
    "memories": memories.render,
    "letter": letter.render,
    "music": music.render,
    "surprises": surprise.render,
    "buildup": buildup.render,
    "proposal": proposal.render,
    "celebration": celebration.render,
    "final": final.render,
}

current_screen = st.session_state.get("screen", "loading")

# Small, unobtrusive progress indicator (hidden on loading screen)
progress_dots()

renderer = SCREEN_RENDERERS.get(current_screen, hero.render)
renderer()
