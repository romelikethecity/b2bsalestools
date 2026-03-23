# B2B Sales Tools — Complete Brand System
## b2bsalestools.com

This is the authoritative brand reference for building b2bsalestools.com. Use this for all pages, components, and assets.

---

## 1. BRAND OVERVIEW

- **Site:** b2bsalestools.com
- **Type:** Static HTML review/comparison site (~190 programmatic pages)
- **Audience:** Sales professionals (SDRs, AEs, Sales Managers, VPs of Sales, CROs, RevOps)
- **Tone:** Authoritative, direct, data-forward. "We tested it so you don't have to."
- **Direction:** "The Operator" — feels like a dashboard built by RevOps people
- **Icon:** "The Stack" — three descending horizontal bars representing ranked evaluation

---

## 2. COLOR SYSTEM

### Primary Palette

| Token | Hex | Usage |
|---|---|---|
| `--indigo` | `#6366F1` | CTAs, buttons, interactive elements, hover states, links |
| `--indigo-hover` | `#4F46E5` | Button hover state |
| `--indigo-light` | `#818CF8` | Gradient endpoints, secondary accents |
| `--indigo-muted` | `rgba(99,102,241,0.12)` | Badge backgrounds, selected states |
| `--cyan` | `#22D3EE` | Scores, rating badges, top-ranked highlights, icon accent |
| `--cyan-dim` | `#06B6D4` | Gradient endpoint for score badges |

### Neutral Palette

| Token | Hex | Usage |
|---|---|---|
| `--slate-900` | `#0F172A` | Headlines, nav text, primary headings |
| `--slate-700` | `#334155` | Body text, paragraphs |
| `--slate-600` | `#475569` | Secondary body text, nav links |
| `--slate-400` | `#94A3B8` | Muted text, placeholders, metadata |
| `--slate-300` | `#CBD5E1` | Borders, icon bottom bar (light bg), dividers |
| `--slate-200` | `#E2E8F0` | Card borders, table borders, separators |
| `--slate-100` | `#F1F5F9` | Table striping, subtle backgrounds |
| `--slate-50` | `#F8FAFC` | Card surface backgrounds |
| `--white` | `#FFFFFF` | Page background |

### CSS Variables Block

```css
:root {
  /* Brand */
  --indigo: #6366F1;
  --indigo-hover: #4F46E5;
  --indigo-light: #818CF8;
  --indigo-muted: rgba(99,102,241,0.12);
  --cyan: #22D3EE;
  --cyan-dim: #06B6D4;

  /* Neutrals */
  --slate-900: #0F172A;
  --slate-700: #334155;
  --slate-600: #475569;
  --slate-400: #94A3B8;
  --slate-300: #CBD5E1;
  --slate-200: #E2E8F0;
  --slate-100: #F1F5F9;
  --slate-50: #F8FAFC;
  --white: #FFFFFF;

  /* Semantic */
  --text-primary: var(--slate-900);
  --text-body: var(--slate-700);
  --text-secondary: var(--slate-600);
  --text-muted: var(--slate-400);
  --bg-page: var(--white);
  --bg-card: var(--slate-50);
  --border-default: var(--slate-200);
  --border-subtle: var(--slate-100);
  --cta-primary: var(--indigo);
  --cta-hover: var(--indigo-hover);
  --score-highlight: var(--cyan);
}
```

---

## 3. TYPOGRAPHY

### Font Stack (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### Type Scale

| Element | Font | Weight | Size | Line Height | Letter Spacing | Color |
|---|---|---|---|---|---|---|
| H1 (page title) | Space Grotesk | 700 | 32px | 1.15 | -1px | `--slate-900` |
| H2 (section) | Space Grotesk | 600 | 22px | 1.25 | -0.5px | `--slate-900` |
| H3 (card title) | Space Grotesk | 600 | 16px | 1.3 | -0.3px | `--slate-900` |
| Body | IBM Plex Sans | 400 | 15px | 1.6 | 0 | `--slate-700` |
| Body small | IBM Plex Sans | 400 | 13px | 1.55 | 0 | `--slate-700` |
| Nav links | IBM Plex Sans | 500 | 13px | 1 | 0.3px | `--slate-600` |
| Nav brand | Space Grotesk | 700 | 15px | 1 | -0.3px | `--slate-900` |
| Data label | JetBrains Mono | 500 | 9-10px | 1 | 1.5px, uppercase | `--slate-400` |
| Tag/badge | IBM Plex Sans | 400 | 11px | 1 | 0 | `--slate-600` |
| Score text | Space Grotesk | 700 | 16px | 1 | 0 | `#FFFFFF` |
| CTA button | Space Grotesk | 600 | 13px | 1 | 0.3px | `#FFFFFF` |
| Category label | IBM Plex Sans | 400 | 12px | 1 | 0 | `--slate-400` |

### CSS Typography

```css
h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 32px;
  line-height: 1.15;
  letter-spacing: -1px;
  color: var(--slate-900);
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 22px;
  line-height: 1.25;
  letter-spacing: -0.5px;
  color: var(--slate-900);
}

h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 16px;
  line-height: 1.3;
  letter-spacing: -0.3px;
  color: var(--slate-900);
}

body, p {
  font-family: 'IBM Plex Sans', sans-serif;
  font-weight: 400;
  font-size: 15px;
  line-height: 1.6;
  color: var(--slate-700);
}

.data-label {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 500;
  font-size: 9px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--slate-400);
}
```

---

## 4. ICON — THE STACK

The icon is three horizontal bars of descending width, left-aligned. Top bar = cyan (the winner), middle = indigo (contender), bottom = slate (baseline).

### SVG Source — Primary (Dark Background)

Use when placing on dark backgrounds (#0F172A or darker).

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="14" width="48" height="10" rx="3" fill="#22D3EE"/>
  <rect x="8" y="28" width="36" height="10" rx="3" fill="#6366F1"/>
  <rect x="8" y="42" width="24" height="10" rx="3" fill="#334155"/>
</svg>
```

### SVG Source — Primary (Light Background)

Use on white or light backgrounds. Bottom bar switches to #CBD5E1.

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="14" width="48" height="10" rx="3" fill="#22D3EE"/>
  <rect x="8" y="28" width="36" height="10" rx="3" fill="#6366F1"/>
  <rect x="8" y="42" width="24" height="10" rx="3" fill="#CBD5E1"/>
</svg>
```

### SVG Source — Monochrome White (Dark Background)

For single-color contexts on dark backgrounds (email footers, watermarks).

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="14" width="48" height="10" rx="3" fill="#FFFFFF" opacity="1"/>
  <rect x="8" y="28" width="36" height="10" rx="3" fill="#FFFFFF" opacity="0.5"/>
  <rect x="8" y="42" width="24" height="10" rx="3" fill="#FFFFFF" opacity="0.2"/>
</svg>
```

### SVG Source — Monochrome Dark (Light Background)

For single-color contexts on light backgrounds.

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="14" width="48" height="10" rx="3" fill="#0F172A" opacity="1"/>
  <rect x="8" y="28" width="36" height="10" rx="3" fill="#0F172A" opacity="0.5"/>
  <rect x="8" y="42" width="24" height="10" rx="3" fill="#0F172A" opacity="0.2"/>
</svg>
```

### SVG Source — Indigo Monochrome

For brand-colored single-tone usage.

```svg
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
  <rect x="8" y="14" width="48" height="10" rx="3" fill="#6366F1" opacity="1"/>
  <rect x="8" y="28" width="36" height="10" rx="3" fill="#6366F1" opacity="0.5"/>
  <rect x="8" y="42" width="24" height="10" rx="3" fill="#6366F1" opacity="0.2"/>
</svg>
```

### Size Adjustments

At sizes below 24px, increase `rx` for legibility:
- 64px+: `rx="3"`
- 32-48px: `rx="3.5"`
- 24px: `rx="4"`
- 16px: `rx="5"`

---

## 5. FAVICON & META

### Favicon Generation

Generate favicons from the primary light-background icon SVG at these sizes:
- `favicon.ico` — multi-resolution (16, 32, 48)
- `favicon-16x16.png`
- `favicon-32x32.png`
- `favicon-48x48.png`
- `apple-touch-icon.png` — 180×180
- `android-chrome-192x192.png`
- `android-chrome-512x512.png`

For PNG favicon generation at small sizes, use the 16px-optimized version (rx="5").

### HTML Head Tags

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="B2B Sales Tools">
<meta property="og:image" content="https://b2bsalestools.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">

<!-- Brand Color -->
<meta name="theme-color" content="#6366F1">
```

### site.webmanifest

```json
{
  "name": "B2B Sales Tools",
  "short_name": "B2BST",
  "icons": [
    { "src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#6366F1",
  "background_color": "#FFFFFF",
  "display": "standalone"
}
```

---

## 6. LOGO LOCKUPS

### Horizontal Lockup (Nav Bar)

Icon (22×22) + 12px gap + "B2B Sales Tools" in Space Grotesk 700 15px.

```html
<div class="site-logo">
  <svg width="22" height="22" viewBox="0 0 64 64" aria-hidden="true">
    <rect x="8" y="14" width="48" height="10" rx="3" fill="#22D3EE"/>
    <rect x="8" y="28" width="36" height="10" rx="3" fill="#6366F1"/>
    <rect x="8" y="42" width="24" height="10" rx="3" fill="#CBD5E1"/>
  </svg>
  <span class="site-logo-text">B2B Sales Tools</span>
</div>
```

```css
.site-logo {
  display: flex;
  align-items: center;
  gap: 12px;
}
.site-logo-text {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 15px;
  color: var(--slate-900);
  letter-spacing: -0.3px;
}
```

---

## 7. COMPONENT PATTERNS

### 7a. Navigation Bar

```html
<nav class="site-nav">
  <div class="site-nav-inner">
    <a href="/" class="site-logo">
      <svg width="22" height="22" viewBox="0 0 64 64" aria-hidden="true">
        <rect x="8" y="14" width="48" height="10" rx="3" fill="#22D3EE"/>
        <rect x="8" y="28" width="36" height="10" rx="3" fill="#6366F1"/>
        <rect x="8" y="42" width="24" height="10" rx="3" fill="#CBD5E1"/>
      </svg>
      <span class="site-logo-text">B2B Sales Tools</span>
    </a>
    <div class="site-nav-links">
      <a href="/reviews/">Reviews</a>
      <a href="/compare/">Compare</a>
      <a href="/best/">Best For</a>
      <a href="/categories/">Categories</a>
    </div>
  </div>
</nav>
```

```css
.site-nav {
  background: var(--white);
  border-bottom: 1px solid var(--slate-200);
  position: sticky;
  top: 0;
  z-index: 100;
}
.site-nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.site-nav-links {
  display: flex;
  gap: 28px;
}
.site-nav-links a {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--slate-600);
  text-decoration: none;
  transition: color 0.15s;
}
.site-nav-links a:hover,
.site-nav-links a.active {
  color: var(--indigo);
}
```

### 7b. Tool Review Card

```html
<div class="tool-card">
  <!-- Optional: only on #1 ranked tool -->
  <div class="top-ranked-badge">★ Top Ranked</div>

  <div class="tool-card-top">
    <div class="tool-score">8.4</div>
    <div class="tool-card-info">
      <h3>Outreach</h3>
      <span class="tool-category">Sales Engagement</span>
    </div>
  </div>

  <p class="tool-verdict">Best-in-class sequencing with the deepest Salesforce integration — but you'll pay for it.</p>

  <div class="tool-bars">
    <div class="tool-bar-item">
      <div class="tool-bar-label">Pricing</div>
      <div class="tool-bar-track"><div class="tool-bar-fill" style="width:35%"></div></div>
    </div>
    <div class="tool-bar-item">
      <div class="tool-bar-label">Ease</div>
      <div class="tool-bar-track"><div class="tool-bar-fill" style="width:65%"></div></div>
    </div>
    <div class="tool-bar-item">
      <div class="tool-bar-label">Support</div>
      <div class="tool-bar-track"><div class="tool-bar-fill" style="width:55%"></div></div>
    </div>
  </div>

  <a href="/reviews/outreach/" class="tool-btn">Read Full Breakdown →</a>

  <div class="tool-card-meta">
    <span class="tool-tag">Mid-Market AEs</span>
    <span class="tool-tag">51-500 seats</span>
  </div>
</div>
```

```css
.tool-card {
  background: var(--slate-50);
  border: 1px solid var(--slate-200);
  border-radius: 10px;
  padding: 24px;
  transition: border-color 0.2s;
}
.tool-card:hover {
  border-color: var(--indigo);
}

.top-ranked-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: 'Space Grotesk', sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: #EEF2FF;
  color: var(--indigo);
  padding: 4px 10px;
  border-radius: 4px;
  margin-bottom: 12px;
}

.tool-card-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}

.tool-score {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #22D3EE, #06B6D4);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 16px;
  color: #FFFFFF;
  flex-shrink: 0;
}

.tool-card-info h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 16px;
  color: var(--slate-900);
  letter-spacing: -0.3px;
}

.tool-category {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 12px;
  color: var(--slate-400);
}

.tool-verdict {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 13px;
  color: var(--slate-700);
  line-height: 1.55;
  margin-bottom: 16px;
}

.tool-bars {
  display: flex;
  gap: 12px;
  margin-bottom: 18px;
}
.tool-bar-item {
  flex: 1;
}
.tool-bar-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  color: var(--slate-400);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}
.tool-bar-track {
  height: 6px;
  background: var(--slate-200);
  border-radius: 3px;
  overflow: hidden;
}
.tool-bar-fill {
  height: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg, #6366F1, #818CF8);
}

.tool-btn {
  display: inline-block;
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 13px;
  color: #FFFFFF;
  background: var(--indigo);
  padding: 10px 22px;
  border-radius: 8px;
  text-decoration: none;
  border: none;
  cursor: pointer;
  transition: background 0.2s;
  letter-spacing: 0.3px;
}
.tool-btn:hover {
  background: var(--indigo-hover);
}

.tool-card-meta {
  display: flex;
  gap: 8px;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--slate-200);
  flex-wrap: wrap;
}
.tool-tag {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 11px;
  color: var(--slate-600);
  background: #EEF2FF;
  padding: 3px 10px;
  border-radius: 4px;
}
```

### 7c. VS Comparison Layout

```html
<div class="vs-header">
  <h1>Outreach <span class="vs-word">vs</span> Salesloft</h1>
  <p>We ran both side-by-side for 6 weeks. Here's what actually matters.</p>
</div>

<div class="vs-grid">
  <div class="vs-tool vs-winner">
    <div class="top-ranked-badge">★ Our Pick</div>
    <h3>Outreach</h3>
    <div class="vs-score winner">8.4 / 10</div>
    <ul class="vs-attrs">
      <li><span>Sequencing</span><span>★★★★★</span></li>
      <li><span>CRM Integration</span><span>★★★★★</span></li>
      <li><span>Ease of Use</span><span>★★★☆☆</span></li>
      <li><span>Pricing</span><span>★★☆☆☆</span></li>
      <li><span>Support</span><span>★★★☆☆</span></li>
    </ul>
  </div>

  <div class="vs-divider">
    <span class="vs-badge">VS</span>
  </div>

  <div class="vs-tool">
    <h3>Salesloft</h3>
    <div class="vs-score">7.8 / 10</div>
    <ul class="vs-attrs">
      <li><span>Sequencing</span><span>★★★★☆</span></li>
      <li><span>CRM Integration</span><span>★★★★☆</span></li>
      <li><span>Ease of Use</span><span>★★★★☆</span></li>
      <li><span>Pricing</span><span>★★★☆☆</span></li>
      <li><span>Support</span><span>★★★★☆</span></li>
    </ul>
  </div>
</div>
```

```css
.vs-header {
  text-align: center;
  margin-bottom: 32px;
}
.vs-header h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--slate-900);
  letter-spacing: -0.5px;
  margin-bottom: 6px;
}
.vs-word {
  color: var(--indigo);
  font-size: 22px;
  margin: 0 4px;
}
.vs-header p {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 14px;
  color: var(--slate-600);
}

.vs-grid {
  display: grid;
  grid-template-columns: 1fr 48px 1fr;
  gap: 0;
  align-items: start;
}

.vs-tool {
  background: var(--white);
  border: 1px solid var(--slate-200);
  border-radius: 10px;
  padding: 28px;
}
.vs-tool h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 18px;
  color: var(--slate-900);
  margin-bottom: 4px;
}
.vs-score {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 28px;
  color: var(--slate-600);
  margin-bottom: 16px;
}
.vs-score.winner {
  color: var(--cyan);
}

.vs-attrs {
  list-style: none;
  padding: 0;
}
.vs-attrs li {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 13px;
  color: var(--slate-700);
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid var(--slate-100);
}
.vs-attrs li span:last-child {
  font-weight: 600;
  color: var(--slate-900);
}

.vs-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 64px;
}
.vs-badge {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 13px;
  color: var(--indigo);
  background: #EEF2FF;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### 7d. Category Grid (cards layout)

```css
.tool-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

@media (max-width: 860px) {
  .tool-grid {
    grid-template-columns: 1fr;
  }
  .vs-grid {
    grid-template-columns: 1fr;
  }
}
```

### 7e. Page Hero Section

```html
<div class="page-hero">
  <h1>Best Sales Engagement Tools (2026)</h1>
  <p>14 platforms evaluated across 8 dimensions. Data-driven rankings updated quarterly.</p>
</div>
```

```css
.page-hero {
  text-align: center;
  padding: 40px 0;
  margin-bottom: 40px;
}
.page-hero h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: var(--slate-900);
  letter-spacing: -1px;
  margin-bottom: 10px;
}
.page-hero p {
  font-family: 'IBM Plex Sans', sans-serif;
  font-size: 15px;
  color: var(--slate-600);
  max-width: 500px;
  margin: 0 auto;
}
```

### 7f. Footer

```css
.site-footer {
  background: var(--slate-900);
  color: var(--slate-400);
  padding: 48px 32px;
  margin-top: 80px;
}
.site-footer a {
  color: var(--slate-300);
  text-decoration: none;
}
.site-footer a:hover {
  color: var(--white);
}
.site-footer .footer-brand {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 15px;
  color: var(--white);
  letter-spacing: -0.3px;
}
```

---

## 8. PAGE TEMPLATES

The site has ~190 pages across these types:

### Page Types & URL Structure

1. **Tool Review** — `/reviews/[tool-slug]/` (e.g., `/reviews/outreach/`)
2. **X vs Y Comparison** — `/compare/[tool-a]-vs-[tool-b]/` (e.g., `/compare/outreach-vs-salesloft/`)
3. **Best Tools for Persona** — `/best/[persona-slug]/` (e.g., `/best/enterprise-aes/`)
4. **Category Ranking** — `/categories/[category-slug]/` (e.g., `/categories/sales-engagement/`)
5. **Homepage** — `/`

### Layout Structure (all pages)

```
┌─────────────────────────────────────┐
│  Nav (sticky)                       │
├─────────────────────────────────────┤
│  Page Hero (h1 + subtitle)          │
├─────────────────────────────────────┤
│  Main Content Area                  │
│  (varies by page type)              │
├─────────────────────────────────────┤
│  Footer                             │
└─────────────────────────────────────┘
```

Max content width: `1200px`, centered with `padding: 0 32px`.

---

## 9. ICON USAGE RULES

### Do
- Use the full-color icon on white or near-white backgrounds
- Switch bottom bar to `#CBD5E1` on light backgrounds
- Maintain minimum clear space equal to the icon width on all sides
- Use monochrome variants for single-color contexts
- Increase `rx` (border-radius) at sizes below 24px

### Don't
- Rotate or flip the icon — bars always descend left-to-right
- Place on busy photographic backgrounds without a container
- Use the dark-variant bottom bar (`#334155`) on light backgrounds
- Stretch or distort the aspect ratio
- Add drop shadows, gradients, or other effects to the icon
- Recolor the bars outside of the defined variants

---

## 10. COMPONENT QUICK REFERENCE

| Component | Background | Border | Radius | Hover |
|---|---|---|---|---|
| Tool card | `--slate-50` | `1px solid --slate-200` | `10px` | `border-color: --indigo` |
| Score badge | `gradient(#22D3EE → #06B6D4)` | none | `10px` | — |
| CTA button | `--indigo` | none | `8px` | `bg: --indigo-hover` |
| Tag | `#EEF2FF` | none | `4px` | — |
| Top ranked badge | `#EEF2FF` | none | `4px` | — |
| Bar track | `--slate-200` | none | `3px` | — |
| Bar fill | `gradient(#6366F1 → #818CF8)` | none | `3px` | — |
| Nav | `--white` | `bottom: 1px solid --slate-200` | `0` | — |
| VS badge | `#EEF2FF` | none | `50%` | — |

---

## 11. SPACING SYSTEM

Use 4px base unit:
- `4px` — tight spacing (between label and value)
- `8px` — element internal gaps
- `12px` — between related elements
- `16px` — between components within a card
- `20px` — grid gap between cards
- `24px` — card padding
- `28px` — VS tool card padding
- `32px` — page horizontal padding, section gaps
- `40px` — hero section vertical padding
- `48px` — section vertical padding
- `80px` — major section separators
