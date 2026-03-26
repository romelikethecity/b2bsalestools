# b2bsalestools.com — Handoff Document

## What This Is
A programmatic comparison/review site for B2B sales software. Generates 190+ static HTML pages from structured data via a Python build script. Hosted on GitHub Pages.

## Business Model
- **Phase 1 (now):** Build site, generate all pages, establish search presence
- **Phase 2 (with traffic):** Add affiliate links to tool profile and comparison pages (SaaS affiliate programs pay $50-200/conversion)
- **Phase 3:** Cross-promote owned newsletters to matching ICPs (see Newsletter Routing below)

## Tech Stack
- **Build:** Python build script (`build.py`) generates all HTML from inline structured data
- **Hosting:** GitHub Pages (static HTML, no server)
- **Brand system:** Complete brand already defined — see `BRAND-SYSTEM.md` in project root
- **Fonts:** Space Grotesk (headings), IBM Plex Sans (body), JetBrains Mono (data labels)
- **Colors:** Indigo `#6366F1` (CTAs), Cyan `#22D3EE` (scores/highlights), Slate neutrals
- **No frameworks.** Pure HTML/CSS/JS. No React, no Hugo, no Astro.

## Architecture (Follow the Provyx Pattern)
The site follows the same pattern as getprovyx.com (`~/Documents/websites/services/provyx-website/`):
- `build.py` contains ALL data inline (tools, categories, comparisons) plus HTML templates
- `build.py` generates all pages into an output directory
- `scripts/` for any helper scripts
- `assets/` for images, CSS, JS
- GitHub Pages serves the output

Key difference from Provyx: this site has MORE page types (tool profiles, X vs Y comparisons, alternatives, category pages, ICP guides, newsletter hub).

## Page Types & Counts

### 1. Category Pages (~22 pages)
URL: `/categories/{slug}/` (e.g., `/categories/cold-email-tools/`)
Content: "Best [Category] Tools in 2026" — ranked list of tools with mini-reviews, pros/cons, pricing summary, verdict. Each tool links to its full profile page.

### 2. Tool Profile Pages (~130 pages)
URL: `/tools/{slug}/` (e.g., `/tools/apollo/`)
Content: What it does, key features, pricing, pros/cons, best for (which ICP), alternatives, related comparisons. Placeholder for affiliate link (button: "Visit [Tool]" or "Try [Tool] Free").

### 3. X vs Y Comparison Pages (~20+ pages)
URL: `/compare/{tool-a}-vs-{tool-b}/` (e.g., `/compare/hubspot-vs-salesforce/`)
Content: Side-by-side feature comparison table, pricing comparison, best for which use case, verdict. Links to both tool profiles.

### 4. Alternatives Pages (~10+ pages)
URL: `/alternatives/{tool}/` (e.g., `/alternatives/zoominfo/`)
Content: "Best [Tool] Alternatives in 2026" — ranked list of alternatives with comparison to the original tool.

### 5. ICP Guide Pages (6 pages)
URL: `/guides/{icp}/` (e.g., `/guides/best-tools-for-sdrs/`)
Content: "Best Sales Tools for [ICP]" — curated tool recommendations organized by workflow stage, specific to that buyer persona.

### 6. Newsletter Hub (1 page)
URL: `/newsletters/`
Content: Recommends newsletters by ICP. Routes visitors to owned properties.

### 7. Homepage (1 page)
URL: `/`
Content: Hero + category grid + featured comparisons + newsletter CTA.

### 8. Blog/Articles (future, not in initial build)
Placeholder structure for future editorial content.

## Category Taxonomy (22 Categories)

Organized by sales workflow: Find → Contact → Sell → Coach & Enable.

### FIND (Prospecting & Data)

**1. B2B Contact & Company Data**
- What: Verified contact info (emails, phones, titles) and company firmographics for prospecting
- Tools: ZoomInfo, Apollo.io, Cognism, Lusha, RocketReach, Seamless.ai
- Primary buyer: SDR/BDR, RevOps

**2. Data Enrichment & Workflow Orchestration**
- What: Enriches lead lists by waterfall-querying multiple data providers with automated workflow logic
- Tools: Clay, Clearbit/Breeze, Databar.ai, LeadIQ, FullEnrich, Dropcontact
- Primary buyer: RevOps, SDR/BDR

**3. Buyer Intent Data**
- What: Identifies accounts actively researching solutions based on content consumption signals
- Tools: Bombora, 6sense, G2 Buyer Intent, Demandbase, TrustRadius Intent, ZoomInfo Intent
- Primary buyer: VP Sales/CRO, RevOps

**4. Website Visitor Identification**
- What: De-anonymizes website visitors by matching IP/browser signals to companies or contacts
- Tools: RB2B, Warmly, Leadfeeder/Dealfront, Clearbit Reveal, Koala, 6sense
- Primary buyer: RevOps, Sales Manager

**5. LinkedIn Sales Tools**
- What: Extends LinkedIn for prospecting, automating outreach, and managing LinkedIn sequences
- Tools: LinkedIn Sales Navigator, Expandi, Dripify, Skylead, SalesRobot, Phantombuster
- Primary buyer: SDR/BDR, AE

### CONTACT (Outreach & Engagement)

**6. Sales Engagement Platforms**
- What: Multi-channel outreach sequences (email, phone, LinkedIn, SMS) with automation and analytics
- Tools: Salesloft, Outreach, Apollo.io, HubSpot Sales Hub, Groove, Mixmax
- Primary buyer: SDR/BDR, Sales Manager

**7. Cold Email & Deliverability**
- What: High-volume cold email with automated warmup, inbox rotation, deliverability optimization
- Tools: Instantly, Smartlead, Lemlist, Woodpecker, Mailshake, Reply.io
- Primary buyer: SDR/BDR, Sales Manager

**8. Sales Dialers & Call Software**
- What: Automated outbound calling with power/parallel dialing, local presence, voicemail drop
- Tools: Orum, Nooks, Koncert, PhoneBurner, Kixie, Aircall
- Primary buyer: SDR/BDR, Sales Manager

**9. AI SDR / Autonomous Outbound**
- What: AI agents that autonomously research prospects, write personalized messages, run outbound
- Tools: 11x, Artisan, Regie.ai, AiSDR, Salesforce Agentforce, Relevance AI
- Primary buyer: VP Sales/CRO, Sales Manager

**10. Meeting Scheduling & Routing**
- What: Automates meeting booking with calendar links, lead routing, round-robin assignment
- Tools: Calendly, Chili Piper, RevenueHero, Reclaim.ai, SavvyCal, HubSpot Meetings
- Primary buyer: SDR/BDR, RevOps

### SELL (Deal Execution)

**11. CRM**
- What: Central system of record for contacts, accounts, opportunities, pipeline
- Tools: Salesforce, HubSpot CRM, Pipedrive, Zoho CRM, Microsoft Dynamics 365, Close CRM
- Primary buyer: VP Sales/CRO, RevOps, Sales Manager

**12. Conversation Intelligence**
- What: Records, transcribes, and AI-analyzes sales calls for coaching insights and deal risks
- Tools: Gong, Chorus, Clari Copilot, Avoma, Fireflies.ai, Sybill
- Primary buyer: Sales Manager, VP Sales/CRO

**13. Revenue Intelligence & Forecasting**
- What: AI-driven pipeline analytics, deal health scoring, revenue forecasts
- Tools: Clari, Gong Forecast, BoostUp, Aviso, Salesforce Revenue Cloud, InsightSquared
- Primary buyer: VP Sales/CRO, RevOps

**14. Digital Sales Rooms**
- What: Shared workspaces for sellers and buyers to collaborate on content and deal progress
- Tools: Dock, Aligned, Trumpet, Flowla, GetAccept, Allego
- Primary buyer: AE, Sales Enablement Leader

**15. Proposal & Document Management**
- What: Create, send, track, and e-sign proposals/quotes with templates and analytics
- Tools: PandaDoc, Proposify, Qwilr, DocuSign, Better Proposals, DealHub
- Primary buyer: AE, Sales Manager

**16. CPQ (Configure, Price, Quote)**
- What: Automates product configuration, pricing rules, discount approvals, quote generation
- Tools: Salesforce CPQ, DealHub CPQ, Conga CPQ, Oracle CPQ, Vendavo, HubSpot CPQ
- Primary buyer: RevOps, AE

**17. Demo Automation**
- What: Self-guided interactive product demos prospects can explore without a live call
- Tools: Storylane, Navattic, Consensus, Walnut, Arcade, TestBox
- Primary buyer: Sales Enablement Leader, AE

**18. E-Signature & Contract Management**
- What: Electronic signatures and contract lifecycle management from drafting through renewal
- Tools: DocuSign, Adobe Sign, Ironclad, Juro, PandaDoc, HelloSign
- Primary buyer: AE, RevOps

### COACH & ENABLE (Team Performance)

**19. Sales Enablement & Content Management**
- What: Organizes, distributes, and tracks sales content so reps use the right material at the right stage
- Tools: Highspot, Seismic, Showpad, Allego, Mindtickle, Guru
- Primary buyer: Sales Enablement Leader, VP Sales/CRO

**20. Sales Coaching & Training**
- What: AI role-play, call scoring, onboarding, skill development to ramp reps faster
- Tools: Gong, Mindtickle, Allego, SalesHood, Brainshark, Second Nature
- Primary buyer: Sales Manager, Sales Enablement Leader

**21. Sales Commission Management**
- What: Calculates and tracks commissions, SPIFFs, variable comp across complex plan structures
- Tools: CaptivateIQ, Spiff, Xactly, Everstage, QuotaPath, Qobra
- Primary buyer: RevOps, VP Sales/CRO

**22. Sales Analytics & Dashboards**
- What: Unified dashboards on rep activity, pipeline velocity, conversion rates, attainment
- Tools: Salesforce Reports, HubSpot Reporting, Kluster, Atrium, Coefficient, Domo
- Primary buyer: VP Sales/CRO, Sales Manager, RevOps

## Top 20 X vs Y Comparisons (Build These First)

1. HubSpot vs Salesforce (CRM)
2. Outreach vs Salesloft (Sales Engagement)
3. ZoomInfo vs Apollo (B2B Data)
4. Gong vs Chorus (Conversation Intelligence)
5. Instantly vs Smartlead (Cold Email)
6. Apollo vs Outreach (Data + Engagement)
7. Calendly vs Chili Piper (Meeting Scheduling)
8. Highspot vs Seismic (Sales Enablement)
9. PandaDoc vs DocuSign (Proposals / E-Signature)
10. Pipedrive vs HubSpot (CRM SMB)
11. Salesforce CPQ vs DealHub (CPQ)
12. Clari vs Gong (Revenue Intelligence)
13. ZoomInfo vs Cognism (B2B Data)
14. Instantly vs Lemlist (Cold Email)
15. 11x vs Artisan (AI SDR)
16. PandaDoc vs Proposify (Proposals)
17. Clay vs Apollo (Data Enrichment)
18. Expandi vs Dripify (LinkedIn Automation)
19. Storylane vs Navattic (Demo Automation)
20. CaptivateIQ vs Spiff (Commission Management)

## Top 10 Alternatives Pages

1. ZoomInfo alternatives
2. Salesforce alternatives
3. Outreach alternatives
4. Gong alternatives
5. Salesloft alternatives
6. Clay alternatives
7. Apollo alternatives
8. Instantly alternatives
9. HubSpot alternatives
10. Chorus alternatives

## 6 ICP Guide Pages

1. Best Sales Tools for SDRs/BDRs
2. Best Sales Tools for Account Executives
3. Best Sales Tools for Sales Managers
4. Best Sales Tools for VPs of Sales & CROs
5. Best Sales Tools for RevOps
6. Best Sales Tools for Sales Enablement Leaders

## Newsletter Routing (Cross-Promotion)

The newsletter hub page and contextual CTAs throughout the site route visitors to owned newsletters based on their ICP:

| Visitor ICP | Newsletter | URL |
|---|---|---|
| CRO / VP Sales | The CRO Report | thecroreport.com |
| RevOps | The RevOps Report | therevopsreport.com |
| Data/Ops/Technical | DataStack Guide | datastackguide.com |
| Fractional Executives | Fractional Pulse | fractionalpulse.com |
| AI/Tech Professionals | AI Market Pulse | theaimarketpulse.com |

Each tool profile page and category page should include a contextual newsletter CTA based on which ICP that page targets.

## SEO Strategy

### URL Structure
- `/` — homepage
- `/categories/{slug}/` — category pages
- `/tools/{slug}/` — tool profiles
- `/compare/{tool-a}-vs-{tool-b}/` — comparisons
- `/alternatives/{tool}/` — alternatives pages
- `/guides/{slug}/` — ICP guides
- `/newsletters/` — newsletter hub

### Title Tag Patterns
- Category: "Best {Category} Tools (2026) — Ranked & Compared | B2B Sales Tools"
- Tool: "{Tool Name} Review 2026: Pricing, Features, Pros & Cons | B2B Sales Tools"
- Compare: "{Tool A} vs {Tool B} (2026): Which Is Better? | B2B Sales Tools"
- Alternatives: "Best {Tool} Alternatives (2026) — Top Picks Ranked | B2B Sales Tools"
- Guide: "Best Sales Tools for {ICP} (2026) | B2B Sales Tools"

### Meta Description Patterns
- Category: "Compare the best {category} tools for B2B sales teams. Side-by-side pricing, features, and honest reviews of {tool1}, {tool2}, and more."
- Tool: "{Tool} review with pricing, features, pros and cons. See how it compares to {alt1} and {alt2}."
- Compare: "{Tool A} vs {Tool B} — detailed comparison of features, pricing, and use cases. Find out which is better for your team."

### Internal Linking
- Every tool profile links to its category page
- Every tool profile links to its comparison pages
- Every comparison page links to both tool profiles + the alternatives page for each
- Every category page links to all its tool profiles + top comparisons in that category
- ICP guides link to relevant tools and categories

## Design Direction

### Brand System (COMPLETE — already built)
**Read `BRAND-SYSTEM.md` in the project root for the full spec.** It defines everything:
- Colors (CSS variables block ready to copy)
- Typography (type scale with sizes, weights, line-heights)
- Component patterns (tool card, VS comparison, nav, hero, footer — all with HTML + CSS)
- Icon system ("The Stack" — three descending bars)
- Logo lockups (horizontal, dark/light variants)
- Spacing system (4px base unit)

### Brand Assets (already in `assets/`)
- `assets/favicons/` — favicon.ico, PNGs at all sizes, apple-touch-icon, webmanifest
- `assets/icons/` — primary-light, primary-dark, mono-white, mono-dark, indigo-mono (16-512px PNGs)
- `assets/logos/` — horizontal-light-bg, horizontal-dark-bg (PNG + @2x)
- `assets/social/` — og-image-1200x630.png, twitter-card-1200x630.png, email headers
- `assets/svg/` — all icons, logos, social images as SVG source
- `assets/html-head-snippet.html` — ready-to-use `<head>` tags (favicon, fonts, OG)

### Key Design Elements (from BRAND-SYSTEM.md)
- **Tool cards** with score badge (cyan gradient), rating bars (indigo gradient), verdict text
- **VS comparison layout** with side-by-side grid, "Our Pick" badge, star ratings
- **Comparison tables** with clear visual hierarchy (winner highlighted in cyan)
- **CTA buttons** — indigo background, Space Grotesk 600, 8px radius
- **Verdict badges** ("Top Ranked", "Our Pick") — indigo on #EEF2FF
- **Newsletter signup** embedded contextually on relevant pages

## Build Order (Suggested)

### Phase 1: Foundation
1. Set up project structure (`build.py`, `assets/`, `templates/` if needed)
2. Define data model in `build.py` (tools dict, categories dict, comparisons list)
3. Build homepage template
4. Build category page template + generate all 22
5. Build tool profile template + generate all ~130

### Phase 2: High-Value Pages
6. Build comparison page template + generate top 20
7. Build alternatives page template + generate top 10
8. Build ICP guide template + generate all 6
9. Build newsletter hub page

### Phase 3: Polish
10. Internal linking pass (cross-link all pages)
11. Sitemap.xml generation
12. robots.txt
13. Open Graph / social meta tags
14. Favicon and brand assets
15. Mobile responsive check

## File Structure
```
b2bsalestools/
  build.py              # ALL data + templates + page generation
  assets/
    css/
      styles.css        # Main stylesheet
    js/
      main.js           # Any interactivity (filters, search, etc.)
    images/             # Logos, icons, screenshots
  output/               # Generated site (this gets deployed to GitHub Pages)
    index.html
    categories/
    tools/
    compare/
    alternatives/
    guides/
    newsletters/
    sitemap.xml
    robots.txt
  scripts/
    deploy.sh           # Optional deploy helper
  README.md
```

## Important Notes

- **All data lives in `build.py`.** Do not create separate JSON/YAML data files. This is the proven pattern from Provyx.
- **Content should be opinionated.** This is a review site, not a directory. Every category page should have a clear "our pick" and every comparison should have a verdict.
- **Pricing will be approximate.** Use publicly available pricing. Add "pricing as of [date]" disclaimers.
- **Affiliate links are placeholders for now.** Use `href="#"` or `href="{tool_url}"` with a CSS class like `affiliate-link` so they're easy to find-and-replace later.
- **Year in titles/content should be parameterized** so it's easy to update annually.
