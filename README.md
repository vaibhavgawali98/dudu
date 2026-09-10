# Our Forever ❤️

A cinematic, mobile-first interactive proposal website — built with Streamlit,
custom HTML/CSS, and a little JavaScript where it genuinely helps. No
database, no logins, no paid services. Just your story, your photos, your
song, and a proposal at the end.

It's designed to feel like a small interactive love story when opened on an
Android phone in Chrome, and to still look great on a laptop.

---

## 1. What's in this project

```
romantic-proposal/
├── app.py                  # Wires all the screens together (routing only)
├── requirements.txt        # Just Streamlit
├── README.md                # You're reading it
├── .gitignore
│
├── config/
│   └── content.py          # ⭐ EVERYTHING you'll personalize lives here
│
├── components/              # One file per "screen" of the experience
│   ├── loading.py
│   ├── hero.py
│   ├── story.py             # timeline
│   ├── memories.py          # photo gallery + detail view
│   ├── letter.py            # love letter with envelope animation
│   ├── music.py             # "Our Song" player
│   ├── surprise.py          # hidden easter eggs
│   ├── buildup.py           # "I have one more thing to ask..."
│   ├── proposal.py          # the big question
│   ├── celebration.py       # she said YES!
│   └── final.py             # closing message
│
├── styles/
│   ├── main.css             # color theme, typography, buttons, cards
│   ├── mobile.css           # responsive breakpoints
│   └── animations.css       # all keyframes + scroll-reveal
│
├── assets/
│   ├── photos/              # put your photos here
│   ├── music/                # put your song here
│   ├── backgrounds/          # optional hero background photo
│   └── icons/                # optional custom icons (emoji work fine)
│
└── utils/
    └── helpers.py            # asset loading, CSS injection, navigation
```

You will only ever need to edit **`config/content.py`** and drop files into
**`assets/`**. Everything else is plumbing.

---

## 2. Install Python (if you don't have it)

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download and install **Python 3.10 or newer**.
3. On Windows, make sure to check **"Add Python to PATH"** during install.
4. Verify it worked by opening a terminal and running:
   ```
   python3 --version
   ```
   (On Windows this may just be `python --version`.)

---

## 3. Set up the project

Open a terminal in the `romantic-proposal` folder, then:

### Create a virtual environment
```bash
python3 -m venv venv
```

### Activate it
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```

You'll know it worked when you see `(venv)` at the start of your terminal
prompt.

### Install the requirements
```bash
pip install -r requirements.txt
```

---

## 4. Run it locally

```bash
streamlit run app.py
```

This opens a local URL (usually `http://localhost:8501`) — open it in your
browser to preview the site. Every time you save a change to a file,
Streamlit will offer to rerun automatically.

To preview the **mobile** experience on your computer, open Chrome DevTools
(F12), click the device toolbar icon, and pick a phone like "Pixel 7".

---

## 5. Personalize everything

Open **`config/content.py`** in VS Code. It's organized into numbered
sections with comments explaining each one:

| What you want to change | Where |
|---|---|
| Her name / your name | `HER_NAME`, `MY_NAME` |
| Loading screen text | `LOADING_TEXT` |
| Hero title / subtitle / body | `HERO_TITLE`, `HERO_SUBTITLE`, `HERO_BODY` |
| Hero background photo | `HERO_BACKGROUND_IMAGE` (filename in `assets/backgrounds/`) |
| Your story timeline | the `TIMELINE` list — add/remove/edit entries freely |
| Photo gallery | the `MEMORIES` list — filename, caption, date, location, detail |
| Love letter | `LETTER_SALUTATION`, `LETTER_BODY`, `LETTER_SIGNATURE` |
| Your song | `SONG_FILENAME`, `SONG_TITLE`, `SONG_ARTIST` |
| Hidden surprises | `ENABLE_*` flags + their teaser/reveal text |
| Build-up screen text | `BUILDUP_TITLE`, `BUILDUP_SUBTITLE`, `BUILDUP_BUTTON` |
| The proposal itself | `PROPOSAL_LEAD`, `PROPOSAL_QUESTION`, button labels |
| The "she said yes" screen | `YES_HEADLINE`, `YES_SUBTEXT`, `YES_MESSAGE` |
| Final closing message | `FINAL_MESSAGE_LINE_1`, `FINAL_MESSAGE_LINE_2` |

You never need to touch any file in `components/`, `styles/`, or `utils/` —
they read everything from `content.py` automatically.

### Colors and fonts
If you want to tweak the color palette, open `styles/main.css` and look at
the `:root { ... }` block near the top — every color used across the site is
a named variable there (`--color-burgundy`, `--color-gold`, etc.), so
changing one line updates the whole site consistently.

---

## 6. Adding your photos

1. Resize your photos so the longest side is under ~1600px (this keeps the
   site fast on mobile). Any free tool like [Squoosh](https://squoosh.app)
   works well for compressing them too.
2. Put the files in `assets/photos/` — e.g. `memory1.jpg`.
3. In `config/content.py`, add an entry to the `MEMORIES` list:
   ```python
   {
       "filename": "memory1.jpg",
       "date": "June 2022",
       "location": "Goa",
       "caption": "The trip that changed everything.",
       "detail": "We almost didn't go, and I'm so glad we did.",
   },
   ```
4. If a photo listed here is missing from the folder, the gallery just shows
   a placeholder instead of crashing — so you can write your captions before
   you've picked the final photos.

---

## 7. Adding your song

1. Export or find your song as an **MP3** file, ideally under 8MB.
2. Put it in `assets/music/`, e.g. `our_song.mp3`.
3. Set `SONG_FILENAME = "our_song.mp3"` in `config/content.py`.
4. Because mobile browsers block audio from playing automatically, she'll
   need to tap the Play button once — this is a hard browser rule, not a bug,
   so the player is designed around it.

---

## 8. Deploying so you can send her a link

The easiest free option is **Streamlit Community Cloud**.

1. **Create a GitHub repository**
   - Go to [github.com/new](https://github.com/new), create a new
     **private** repository (recommended, so the surprise stays a surprise).
2. **Upload the project**
   ```bash
   cd romantic-proposal
   git init
   git add .
   git commit -m "Our Forever"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. **Deploy on Streamlit Community Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with
     GitHub.
   - Click **"New app"**, choose your repository, branch `main`, and set the
     main file to `app.py`.
   - Click **Deploy**.
4. **Get your public URL**
   - Streamlit will give you a URL like
     `https://your-app-name.streamlit.app`.
5. **Open it on Android**
   - Send yourself the link (e.g. via a private note or email) and open it
     in **Chrome for Android** to test the full mobile experience before the
     big moment.
6. **Share it with her**
   - Send the link however you'd like — text, or however you plan to
     surprise her.

> **Privacy note:** if your repository is private, Streamlit Community Cloud
> can still deploy it, but you may need to set the app's sharing setting to
> "Public" so she can open the link without a login. The app itself doesn't
> collect any data, use analytics, or send anything to third parties.

---

## 9. A note on a few technical limits

- **Audio autoplay:** browsers require a real tap before playing sound, so
  the "Our Song" player always needs one tap on Play — this can't be worked
  around, and trying to would just break the player on some phones.
- **Scroll animations:** the timeline and gallery use a modern CSS feature
  (`animation-timeline: view()`) for scroll-triggered reveals on Chrome
  Android. On older or non-Chromium browsers, the same content just appears
  normally with a simple fade-in instead — nothing breaks, it just animates
  a little less.
- **Missing assets:** if a photo or the song file isn't in `assets/` yet,
  the app shows a small placeholder instead of crashing, so you can build
  and deploy the site before your assets are 100% final.

---

## 10. Common errors and fixes

| Problem | Fix |
|---|---|
| `streamlit: command not found` | Make sure your virtual environment is activated (`source venv/bin/activate`) and you ran `pip install -r requirements.txt`. |
| Fonts or colors look different | Google Fonts may not have loaded (no internet, or blocked). The site falls back to system serif/sans-serif fonts automatically — this is expected and still looks good. |
| Photo doesn't show up | Double-check the filename in `content.py` **exactly** matches the file in `assets/photos/`, including capitalization and extension (`.jpg` vs `.JPG`). |
| Song won't play | Confirm the file is a real `.mp3` and under ~8MB, and that `SONG_FILENAME` in `content.py` matches exactly. |
| App crashes with an import error | Make sure you didn't rename or move any files inside `components/`, `styles/`, or `utils/` — `app.py` expects the folder structure exactly as delivered. |
| Deployed app shows old content | Streamlit Cloud auto-redeploys on every `git push` to `main` — if it looks stale, check the deploy logs on share.streamlit.io or manually reboot the app from its dashboard. |

---

## HOW TO PERSONALIZE THIS (quick reference)

1. **Her photos** → `assets/photos/`, then list them in `MEMORIES` in `config/content.py`
2. **The song** → `assets/music/`, then set `SONG_FILENAME` in `config/content.py`
3. **Her name** → `HER_NAME` in `config/content.py`
4. **Your name** → `MY_NAME` in `config/content.py`
5. **Your dates/story** → the `TIMELINE` list in `config/content.py`
6. **The love letter** → `LETTER_BODY` in `config/content.py`
7. **Memories/captions** → the `MEMORIES` list in `config/content.py`
8. **The proposal message** → `PROPOSAL_LEAD`, `PROPOSAL_QUESTION` in `config/content.py`
9. **Run it locally** → `streamlit run app.py` (after `pip install -r requirements.txt`)
10. **Deploy it** → push to GitHub → deploy on [share.streamlit.io](https://share.streamlit.io) → get your link

---

Made with care, for a moment worth making beautiful. ❤️
