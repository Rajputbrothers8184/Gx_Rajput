# Gx_Rajput — Personal Portfolio Website

Dark-theme (black / blue / orange) portfolio for **Noor Ul Hassan (Gx_Rajput)** — Graphics Designer,
Video Editor and Full-Stack / App Developer from **Layyah, Punjab, Pakistan**.

- **Live site:** https://rajputbrothers8184.github.io/Gx_Rajput/
- **Repository:** https://github.com/Rajputbrothers8184/Gx_Rajput

Built as a plain static site (HTML + CSS + vanilla JS) — no build step, no dependencies, loads fast and
hosts free on GitHub Pages.

---

## 1. Go live (one-time, 1 minute)

The deploy workflow is already in `.github/workflows/pages.yml`. To switch it on:

1. Open **https://github.com/Rajputbrothers8184/Gx_Rajput/settings/pages**
2. Under **Build and deployment → Source**, choose **GitHub Actions**
3. Done. Every push to `main` rebuilds and publishes the site at
   `https://rajputbrothers8184.github.io/Gx_Rajput/`

To publish manually: **Actions → "Deploy Portfolio to GitHub Pages" → Run workflow**.

> **Note:** GitHub Pages only deploys from the **default branch (`main`)** — pushes to other branches
> build the site but the deploy job is skipped. Merge into `main` (pull request) to publish changes.

---

## 2. What's inside

| Section | Details |
|---|---|
| **Hero** | Profile icon (man in a 3-piece suit), name, roles, WhatsApp / Portfolio / Save-contact buttons, stats |
| **About** | Who you are, the three skill stacks, tools, quick-facts card (name, location, experience, contacts) |
| **Skills** | Percentage bars for Design (Photoshop, Illustrator, CorelDRAW, Canva), Video (Premiere Pro, CapCut, After Effects) and Development (HTML/CSS/JS, React, Node, Flutter, Python) + a note that you work **without Figma** |
| **Portfolio** | **48 designs — 6 in each of 8 categories**, filterable, with a full-screen lightbox |
| **Services** | 4 packages (Starter, Brand Kit, Video Pack, Development) + the printing-on-demand note |
| **Process** | 4-step workflow |
| **Contact** | WhatsApp, Instagram, Facebook, TikTok, GitHub, Email, Call, Location + a form that opens WhatsApp |
| **Extras** | Sticky nav, mobile menu, floating WhatsApp button, back-to-top, scroll animations, SEO/OG tags, JSON-LD, downloadable vCard |

### Portfolio categories (6 designs each)

Logo Design · Social Media Posts · YouTube Thumbnails · Banners & Covers · Business Cards ·
Print & Packaging · Video Editing · Web & App / Dev Projects

---

## 3. Contact details wired into the site

| Channel | Value |
|---|---|
| WhatsApp | **0311 0682944** → `+92 311 0682944` (`wa.me/923110682944`) |
| Instagram | [@noor_ul8184](https://www.instagram.com/noor_ul8184/) |
| Facebook | [noorulhassan8184](https://www.facebook.com/noorulhassan8184) |
| TikTok | [@gx_rajput](https://www.tiktok.com/@gx_rajput) |
| GitHub | [Rajputbrothers8184](https://github.com/Rajputbrothers8184) |
| Email | n88908410@gmail.com |
| Location | Layyah, Punjab, Pakistan |

---

## 4. Project structure

```
index.html                  the whole site (all content lives here)
css/style.css               theme: black / blue / orange
js/main.js                  nav, filters, lightbox, animations, WhatsApp form
assets/img/profile.png      profile icon — man in a 3-piece suit
assets/img/cover.jpg        hero cover art
assets/img/og-image.jpg     social share preview (1200×630)
assets/img/favicon.png      browser tab icon
assets/img/work/*.jpg       photo-based samples (social posts, thumbnails, video frames)
assets/svg/*.svg            31 hand-crafted vector samples (logos, cards, banners, print, UI, thumbnail)
assets/Gx_Rajput.vcf        downloadable contact card
tools/gen_sample_assets.py  regenerates the vector samples
.github/workflows/pages.yml GitHub Pages deployment
```

---

## 5. How to customise

Everything is plain HTML — open `index.html` and edit:

| What | Where |
|---|---|
| Name, tagline, bio | Hero section (`<section class="hero">`) |
| **Stats (7+, 1200+, 600+, 24h)** | `.hero-stats` — ⚠️ set these to your real numbers |
| Skills & percentages | `#skills` — change `data-w="95"` and the label |
| **Package prices** | `#services` — ⚠️ starting rates, edit to your actual charges |
| Portfolio items | `#portfolio` — each card is one `<article class="card" data-cat="…">` |
| Colours | `:root` in `css/style.css` (`--blue`, `--orange`, `--bg`) |
| Social links | Hero buttons, `#contact` cards, footer, and `js/main.js` (WhatsApp number) |

### Adding / replacing a portfolio design

1. Drop the image in `assets/img/work/` (or `assets/svg/` for vector work).
2. Copy any `<article class="card">` block, change the `src`, title, description and `data-cat`.
3. If you add a brand-new category, add a matching filter button:
   `<button class="filter" data-f="newcat">New Category <small>6</small></button>`

Valid `data-cat` values: `logo`, `social`, `thumb`, `banner`, `card`, `print`, `video`, `ui`.

### The WhatsApp number appears in 5 places

`index.html` (hero button ×2, contact cards, service buttons) and `js/main.js` (contact form).
Search for `923110682944` to find them all.

---

## 6. Printing note

Printing is **on demand** and charged **separately** — that is stated in the About section and in the
highlighted note under the pricing section. Design packages include print-ready digital files only.

---

## 7. Run locally

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

Regenerate the vector sample designs after editing the generator:

```bash
python3 tools/gen_sample_assets.py
```

---

© Gx_Rajput — designed, edited and coded by Noor Ul Hassan, Layyah, Punjab, Pakistan.
