"""Screen 9 — The Proposal.

The "not ready yet" option is real and respectful: it never blocks,
dodges the cursor, or nags. It simply says that's okay and lets her
come back to the question whenever she wants.
"""

import streamlit as st

from config import content as c
from utils.helpers import go_to, floating_petals, md_html, background_music


def render():
    if c.ENABLE_BACKGROUND_MUSIC and c.BACKGROUND_MUSIC.get("proposal"):
        background_music(c.BACKGROUND_MUSIC["proposal"], key="proposal", volume=c.BACKGROUND_MUSIC_VOLUME)

    if st.session_state.get("proposal_answer") == "waiting":
        _render_waiting()
        return

    md_html(
        f"""
        <div class="screen screen-center" style="min-height:90vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:0.9rem;">
                <div class="big-heart anim-ring-glow" style="font-size:4.2rem;">{c.PROPOSAL_RING_EMOJI}</div>
                <p class="script-text" style="font-size:1.15rem; max-width:300px; text-align:center;">
                    {c.PROPOSAL_LEAD}
                </p>
                <h1 class="proposal-question serif-title" style="text-align:center; max-width:340px;">
                    {c.PROPOSAL_QUESTION}
                </h1>
            </div>
        </div>
        """
    )

    floating_petals(14)

    st.write("")
    if st.button(c.PROPOSAL_YES_BUTTON, key="yes_btn", use_container_width=True, type="primary"):
        st.session_state["proposal_answer"] = "yes"
        go_to("celebration")

    if st.button(c.PROPOSAL_YES_BUTTON_2, key="yes_btn_2", use_container_width=True, type="primary"):
        st.session_state["proposal_answer"] = "yes"
        go_to("celebration")

    st.write("")
    if st.button(c.PROPOSAL_NO_BUTTON, key="not_ready_btn", use_container_width=True):
        st.session_state["proposal_answer"] = "waiting"
        st.rerun()


def _render_waiting():
    """A gentle, non-manipulative response to 'not ready yet'."""
    md_html(
        """
        <div class="screen screen-center" style="min-height:80vh; justify-content:center;">
            <div class="anim-fade-in" style="display:flex; flex-direction:column; align-items:center; gap:1rem;">
                <div style="font-size:3rem;">🤍</div>
                <h2 class="serif-title" style="text-align:center; font-size:1.4rem; max-width:300px;">
                    That's okay. Take all the time you need.
                </h2>
                <p class="body-text" style="text-align:center; max-width:300px;">
                    I'll be right here whenever you're ready — there's no rush at all.
                </p>
            </div>
        </div>
        """
    )
    st.write("")
    cols = st.columns([1, 2, 1])
    with cols[1]:
        if st.button("I'm ready now ❤️", use_container_width=True, type="primary"):
            st.session_state["proposal_answer"] = None
            st.rerun()
