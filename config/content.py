"""
=====================================================================
  CONTENT.PY  —  YOUR PERSONALIZATION FILE
=====================================================================

  This is the ONLY file you need to touch to make this website
  yours. Everything on the site — names, dates, story, letter,
  photos, song, proposal text — is edited right here.

  Rules for editing safely:
    1. Only change the text INSIDE the quotes " " or ' '.
    2. Keep the commas ( , ) at the end of lines.
    3. Keep the quotation marks.
    4. Emojis are optional — feel free to remove or add your own.

  Everything is explained with comments (lines starting with #).
=====================================================================
"""

# ---------------------------------------------------------------
# 1. THE TWO OF YOU
# ---------------------------------------------------------------
HER_NAME = "Duduu😍"          # Her name, e.g. "Ananya"
MY_NAME = "Bubu"                 # Your name, e.g. "Rohan"

# The site title shown in the browser tab
SITE_TITLE = "Our Forever ❤️"

# ---------------------------------------------------------------
# 2. SCREEN 0 — LOADING SCREEN
# ---------------------------------------------------------------
LOADING_TEXT = "Preparing something special for you..."
LOADING_SUBTEXT = "❤️"

# ---------------------------------------------------------------
# 3. SCREEN 1 — WELCOME / HERO
# ---------------------------------------------------------------
HERO_TITLE = "Happy BirthDay Sweet"
HERO_SUBTITLE = "You are my everything."
HERO_BODY = (
    "Every moment with you became a beautiful chapter of my life. "
    "Tonight, I want to take you through our story — one more time."
)
HERO_BUTTON = "Start Our Journey ❤️"

# Background image for the hero screen.
# Put a file inside assets/backgrounds/ and put its filename here.
# Example: "hero.jpg"  ->  assets/backgrounds/hero.jpg
HERO_BACKGROUND_IMAGE = "hero.jpg"

# ---------------------------------------------------------------
# 4. SCREEN 2 — OUR STORY (TIMELINE)
# ---------------------------------------------------------------
# Add, remove, or edit as many timeline moments as you like.
# icon = any emoji. date is optional — leave "" to hide it.
TIMELINE = [
    {
        "icon": "❤️",
        "date": "The Beginning",
        "title": "We Met",
        "description": "That's where our story began.",
    },
    {
        "icon": "✨",
        "date": "2022",
        "title": "We Connected",
        "description": "Somehow, you became special.",
    },
    {
        "icon": "💕",
        "date": "2023",
        "title": "We Fell in Love",
        "description": "My heart already knew.",
    },
    {
        "icon": "♾️",
        "date": "Today",
        "title": "Forever Together",
        "description": "And now I want forever with you.",
    },
]

# ---------------------------------------------------------------
# 5. SCREEN 3 & 4 — OUR MEMORIES (PHOTO GALLERY)
# ---------------------------------------------------------------
# Step 1: put your photos inside assets/photos/
# Step 2: list them here with a caption, date, and location.
# If a filename doesn't exist yet, the app will simply skip it
# instead of crashing — so you can add this list in advance.
MEMORIES_TITLE = "Our Memories"
MEMORIES_SUBTITLE = "Every picture, a piece of us."

MEMORIES = [
    {
        "filename": "memory1.jpg",
        "date": "",
        "location": "",
        "caption": "That day didn't look special at first...",
        "detail": "...but it became one of my favorite memories, "
                   "because I was with you.",
    },
    {
        "filename": "memory2.jpg",
        "date": "",
        "location": "",
        "caption": "I remember exactly how you laughed that day.",
        "detail": "It's still one of my favorite sounds in the world.",
    },
    {
        "filename": "memory3.jpg",
        "date": "",
        "location": "",
        "caption": "A quiet moment, just us.",
        "detail": "Those are the ones I treasure most.",
    },
    {
            "filename": "memory4.jpg",
            "date": "",
            "location": "",
            "caption": "",
            "detail": "",
    },
    {
            "filename": "memory5.jpg",
            "date": "",
            "location": "",
            "caption": ".",
            "detail": "",
    },
    {
            "filename": "memory6.jpg",
            "date": "",
            "location": "",
            "caption": "",
            "detail": "",
    },
    {
            "filename": "memory7.jpg",
            "date": "",
            "location": "",
            "caption": "",
            "detail": "",
    },
    {
            "filename": "memory8.jpg",
            "date": "",
            "location": "",
            "caption": "",
            "detail": "",
    }, 
    {
            "filename": "memory9.jpg",
            "date": "",
            "location": "",
            "caption": "",
            "detail": "",
    },               
]

# ---------------------------------------------------------------
# 6. SCREEN 5 — LOVE LETTER
# ---------------------------------------------------------------
LETTER_TITLE = "A Letter For You"
LETTER_SALUTATION = f"Dear {HER_NAME},"
LETTER_BODY = """I don't think I've ever told you this the way I truly feel it,
so I'm putting it here, where I hope it stays with you.

From the very beginning, being with you felt easy in a way
nothing else ever has. You make ordinary days feel like they
matter. You make me want to be better, softer, braver.

I know I don't say it enough, but every single day with you
has been a gift I don't take for granted.

This is just the beginning of what I want to say to you tonight."""
LETTER_SIGNATURE = f"Forever yours,\n{MY_NAME}"

# ---------------------------------------------------------------
# 6b. BACKGROUND MUSIC (plays quietly on each chapter)
# ---------------------------------------------------------------
# Set to False to disable background music everywhere.
ENABLE_BACKGROUND_MUSIC = True

# How loud the background music is, from 0.0 (silent) to 1.0 (full volume).
BACKGROUND_MUSIC_VOLUME = 0.35

# One track per chapter. Put MP3 files in assets/music/ and reference
# them by filename here. Leave a value as "" to keep that chapter
# silent. It's fine to reuse the same filename for several chapters,
# or to point every chapter at one track for a simpler, unified feel.
BACKGROUND_MUSIC = {
    "hero": "apt_bubu_dudu.mp3",
    "story": "",
    "memories": "",
    "letter": "",
    "surprises": "",
    "buildup": "",
    "proposal": "",
    "celebration": "",
    "final": "",
}

# ---------------------------------------------------------------
# 7. SCREEN 6 — OUR SONG
# ---------------------------------------------------------------
# Put an MP3 file inside assets/music/ and put its filename here.
SONG_FILENAME = "our_song.mp3"
SONG_TITLE = "Guess ?? 🙂"
SONG_ARTIST = ""   # optional, e.g. "Ed Sheeran"

MUSIC_SECTION_TITLE = "Song for my Cutie❤️"
MUSIC_SECTION_SUBTITLE = "The one that always reminds me of you."

# ---------------------------------------------------------------
# 8. SCREEN 7 — HIDDEN SURPRISES (EASTER EGGS)
# ---------------------------------------------------------------
# Set any of these to False to disable that surprise.
ENABLE_HEART_TAP_SURPRISE = True
ENABLE_SECRET_MEMORY = True
ENABLE_ONE_MORE_THING = True

HEART_TAP_TARGET = 3   # how many taps to reveal the hidden message
HEART_TAP_MESSAGE = (
    "You found it. 🤫\n\nSince the day we met, not one day has gone by "
    "where I didn't think about you at least once. Not one."
)

SECRET_MEMORY_TEASER = "Tap to reveal a memory I've never told you about..."
SECRET_MEMORY_TEXT = (
    "The first time I saw you, I already knew you were going to "
    "matter to me. I just didn't know how much."
)

ONE_MORE_THING_TEASER = "one more thing..."
ONE_MORE_THING_TEXT = (
    "Every road in my life, no matter how it winds, "
    "somehow always leads back to you."
)

# ---------------------------------------------------------------
# 9. SCREEN 8 — BUILD-UP TO THE PROPOSAL
# ---------------------------------------------------------------
BUILDUP_TITLE = "I have one more thing to ask you..."
BUILDUP_SUBTITLE = "Are you ready?"
BUILDUP_BUTTON = "Yes, I'm Ready ❤️"

# ---------------------------------------------------------------
# 10. SCREEN 9 — THE PROPOSAL
# ---------------------------------------------------------------
PROPOSAL_LEAD = "I want to spend every tomorrow with you."
PROPOSAL_QUESTION = "Will You Marry Me?"
PROPOSAL_RING_EMOJI = "💍"

PROPOSAL_YES_BUTTON = "YES ❤️"
PROPOSAL_YES_BUTTON_2 = "Of Course ❤️"
# The "no" option is intentionally soft and never blocks her —
# see components/proposal.py for how it behaves.
PROPOSAL_NO_BUTTON = "Give me a moment 🥺"

# ---------------------------------------------------------------
# 11. SCREEN 10 — SHE SAID YES
# ---------------------------------------------------------------
YES_HEADLINE = "She Said YES! ❤️"
YES_SUBTEXT = "You just made me the happiest person alive."
YES_MESSAGE = (
    "Thank you for saying yes to forever with me. I promise to spend "
    "every day making sure you never regret it. I love you, endlessly."
)

# ---------------------------------------------------------------
# 12. SCREEN 11 — FINAL MESSAGE
# ---------------------------------------------------------------
FINAL_MESSAGE_LINE_1 = "Whatever happens, thank you for being part of my life."
FINAL_MESSAGE_LINE_2 = "Forever yours ❤️"
FINAL_SIGNATURE = MY_NAME
