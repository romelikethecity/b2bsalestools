# Context Window Prompt — b2bsalestools.com

Copy everything below this line into a new Claude context window.

---

## Your Task

You are building **b2bsalestools.com** — a programmatic comparison and review site for B2B sales software. The site generates ~190 static HTML pages from structured data using a Python build script, hosted on GitHub Pages.

**Read these two files first (in this order):**
```
Read the file at /Users/rome/Documents/projects/b2bsalestools/BRAND-SYSTEM.md
Read the file at /Users/rome/Documents/projects/b2bsalestools/HANDOFF.md
```

- **BRAND-SYSTEM.md** — Complete brand spec: colors, typography, component patterns (tool card, VS comparison, nav, hero, footer), icon system, logo lockups, spacing. All CSS is ready to use.
- **HANDOFF.md** — Full build spec: 22 tool categories, 130+ tools, page types, URL structure, SEO patterns, newsletter routing, and build order.

## What to Build

A Python build script (`build.py`) that generates a complete static site with these page types:
1. **Homepage** — hero + category grid + featured comparisons + newsletter CTA
2. **22 category pages** — "Best [Category] Tools 2026" with ranked tool lists
3. **~130 tool profile pages** — individual review pages per tool
4. **20+ comparison pages** — "X vs Y" side-by-side comparisons
5. **10+ alternatives pages** — "Best [Tool] Alternatives"
6. **6 ICP guide pages** — "Best Sales Tools for [Persona]"
7. **Newsletter hub** — routes visitors to owned newsletters by ICP

## Architecture Rules

1. **All data lives in `build.py`.** Tools, categories, comparisons, alternatives — everything is inline Python dicts/lists. No separate JSON or YAML files. This is the proven pattern from the Provyx site.
2. **Static HTML output.** The build script generates all HTML files into an `output/` directory. No server, no framework, no build tools beyond Python.
3. **Single CSS file** at `assets/css/styles.css`. Use the CSS variables, typography, and component styles from BRAND-SYSTEM.md. Do NOT invent new colors or fonts — the brand system is final.
4. **SEO-first.** Every page needs proper title tags, meta descriptions, Open Graph tags, canonical URLs, and internal cross-links. The URL patterns and title patterns are specified in the handoff.
5. **Opinionated content.** This is a review site, not a directory. Every category page should have a clear "our pick." Every comparison should have a verdict. The tone is authoritative and direct.
6. **Newsletter cross-promotion.** Contextual CTAs throughout the site recommend specific newsletters based on which ICP the page targets:
   - CRO / VP Sales → The CRO Report (thecroreport.com)
   - RevOps → The RevOps Report (therevopsreport.com)
   - Data/Ops → DataStack Guide (datastackguide.com)
   - Fractional Executives → Fractional Pulse (fractionalpulse.com)
   - AI/Tech → AI Market Pulse (theaimarketpulse.com)
7. **Affiliate link placeholders.** Use `class="affiliate-link"` on all "Visit Tool" / "Try Free" buttons so they're easy to update later. Link to the tool's actual website URL for now.
8. **Year is parameterized.** Define `CURRENT_YEAR = 2026` at the top of `build.py` and reference it in all titles and content so annual updates are a one-line change.

## Brand System (Already Complete)

The brand is fully designed. Everything is in `BRAND-SYSTEM.md` and `assets/`. Do NOT deviate from it.

- **Colors:** Indigo `#6366F1` (CTAs), Cyan `#22D3EE` (scores/highlights), Slate neutrals (see CSS variables block)
- **Fonts:** Space Grotesk (headings/buttons), IBM Plex Sans (body), JetBrains Mono (data labels)
- **Components:** Tool card, VS comparison, nav bar, page hero, footer — all have HTML + CSS in BRAND-SYSTEM.md. Use them directly.
- **Assets already in `assets/`:**
  - `favicons/` — favicon.ico, PNGs, apple-touch-icon, webmanifest, browserconfig
  - `icons/` — primary-light, primary-dark, mono-white, mono-dark, indigo-mono (16-512px PNGs)
  - `logos/` — horizontal-light-bg, horizontal-dark-bg (PNG + @2x retina)
  - `social/` — og-image-1200x630.png, twitter-card-1200x630.png, email headers
  - `svg/` — all icons, logos, social images as SVG source files
  - `html-head-snippet.html` — ready-to-use `<head>` tags (favicon, fonts, OG meta)

## Build Order

Start with Phase 1 (foundation) and build incrementally:

### Phase 1: Foundation
1. Project structure + `build.py` skeleton with data model
2. `styles.css` built from BRAND-SYSTEM.md (copy CSS variables, typography, component styles)
3. Homepage template + generation
4. Category page template + generate all 22
5. Tool profile page template + generate all ~130

### Phase 2: High-Value Pages
6. Comparison page template + generate 20+
7. Alternatives page template + generate 10+
8. ICP guide pages (6)
9. Newsletter hub page

### Phase 3: Polish
10. Internal linking pass
11. sitemap.xml + robots.txt
12. Mobile responsive check
13. Open Graph + social meta (use assets from `assets/social/`)

## Working Directory

```
/Users/rome/Documents/projects/b2bsalestools/
```

## Reference Sites (for architecture patterns, NOT for design)

- **Provyx site** (`/Users/rome/Documents/projects/provyx-website/`) — look at `scripts/build.py` for how inline data + templates generate 346 pages. Follow this pattern.
- **AI Market Pulse** (`/Users/rome/Documents/aimarketpulse/`) — reference for newsletter integration patterns

## Important

- Read BRAND-SYSTEM.md and HANDOFF.md first before writing any code
- Start with `build.py` data model — get the tool/category data structure right before building templates
- The `build.py` script should copy assets from `assets/` into `output/` as part of the build (favicons, social images, CSS, etc.)
- Generate a working site that can be previewed with `python3 -m http.server 8083` from the output directory
- Use the brand system exactly as specified — do not invent new colors, fonts, or component styles
- Every page must be mobile-responsive
- Do NOT over-engineer. Start with the core pages and iterate.
