# Vertical SaaS and Vertical AI Expansion — Design

**Date:** 2026-05-05
**Site:** b2bsalestools.com
**Author:** Rome Thorndike (with Claude Code)
**Status:** Approved for implementation planning

## Goal

Extend b2bsalestools.com beyond its current B2B-sales-tool review scope to cover **Vertical SaaS** (industry-specific operational software) and **Vertical AI** (AI-native tools specific to an industry) across six verticals: Legal, Home Services, Veterinary, Financial Advisor, Construction, Agriculture.

Final destination: ~150 review pages across all six verticals × both scopes, deployed in three waves of two verticals each, with vendor profile pages added in a half-step deploy after each wave's structural pages rank.

## Decisions locked during brainstorming

These are settled. Do not relitigate during implementation.

1. **Architecture**: extend existing `/industries/` parent pattern. New verticals nest as `/industries/{vertical}/`, with scope sub-paths `/industries/{vertical}/{scope}/`.
2. **Phasing**: phased D — three deploy waves of two verticals, each preceded by a vendor research pass and each followed by a vendor-profile half-deploy (Wave 1.5, Wave 2.5, Wave 3.5).
3. **Wave 1 verticals**: Legal + Home Services. (Wave 2/3 industries chosen at the start of those waves based on fresh research.)
4. **Wave 1 page mix**: comparison-and-guide-first across all four scopes. Individual vendor profile pages deferred to Wave 1.5 because branded "X vs Y" and "best X for Y" queries rank fastest at low domain authority. Vendor profile pages compete with the vendors' own marketing sites and dominant review aggregators (G2, Capterra) and need ranking authority to land.
5. **Affiliate strategy**: vendor homepage URLs as link targets in Wave 1, swapped to affiliate URLs once programs activate. Matches existing site's Phase 1 pattern per HANDOFF.md.
6. **Audience capture**: deferred. Templates reserve a single email-capture slot wired to the existing newsletter cross-promo (route by ICP to The CRO Report / RevOps Report / DataStack Guide via the existing Formspree endpoint or equivalent). Dedicated b2bsalestools list is a phase-2 decision once traffic justifies it. GA4 currently shows ~22 weekly views with 0s avg engagement; capture is not the bottleneck, content quality + traffic are.
7. **Content quality bar**: every page passes ROME_WRITING_STYLE.md audit + marketingskills/programmatic-seo principles + minimum word-count floor before deploy.

## Architecture

### URL structure (Wave 1)

```
/industries/legal/                                      [hub]
├── practice-management/                                [scope landing]
└── ai/                                                 [scope landing]

/industries/home-services/                              [hub]
├── field-service-management/                           [scope landing]
└── ai/                                                 [scope landing]

/compare/{a-slug}-vs-{b-slug}/                          [×24]
/guides/{slug}/                                         [×16]
```

### Wave 1 page inventory (46 total)

**Industry hubs (2)**
- `/industries/legal/`
- `/industries/home-services/`

**Scope landings (4)**
- `/industries/legal/practice-management/`
- `/industries/legal/ai/`
- `/industries/home-services/field-service-management/`
- `/industries/home-services/ai/`

**Comparisons (24)** — six per scope, vendor pairs from research with high or medium-high search intent:

| Scope | Comparisons |
|---|---|
| Legal SaaS | clio-vs-mycase, clio-vs-practicepanther, mycase-vs-practicepanther, smokeball-vs-clio, filevine-vs-litify, clio-vs-smokeball |
| Legal AI | harvey-vs-spellbook, evenup-vs-eve, evenup-vs-supio, lexis-ai-vs-westlaw-precision, spellbook-vs-lexis-ai, harvey-vs-cocounsel |
| HS SaaS | servicetitan-vs-jobber, jobber-vs-housecallpro, servicetitan-vs-housecallpro, servicetitan-vs-fieldedge, workiz-vs-housecallpro, buildops-vs-servicetitan |
| HS AI | avoca-vs-hatch, goodcall-vs-rosie, avoca-vs-goodcall, sera-vs-servicetitan, hatch-vs-leadtruffle, avoca-vs-rilla |

**Best-for guides (16)** — four per scope:

| Scope | Guides |
|---|---|
| Legal SaaS | best-practice-management-software-solo-attorneys, best-legal-practice-management-small-firms, best-pms-personal-injury-law-firms, best-clio-alternatives |
| Legal AI | best-legal-ai-personal-injury-firms, best-ai-contract-review-software, best-ai-legal-research-tools, best-ai-tools-solo-lawyers |
| HS SaaS | best-hvac-software, best-plumbing-software, best-electrical-contractor-software, best-servicetitan-alternatives |
| HS AI | best-ai-call-answering-hvac, best-ai-receptionist-home-services, best-ai-tools-plumbing-companies, best-ai-sales-coaching-in-home-sales |

### Wave 1.5 page inventory (vendor profiles, ~39 pages)

Deployed after Wave 1 ranks signal (typically 4-8 weeks post-deploy, monitor via GSC).

| Scope | Vendors covered (research-validated) |
|---|---|
| Legal SaaS (10) | Clio, MyCase, PracticePanther, Smokeball, Filevine, CosmoLex, Rocket Matter, Centerbase, Litify, LawPay |
| Legal AI (10, with Robin AI dropped per research) | Harvey, Spellbook, EvenUp, Eve, Supio, CaseMark, Lexis+ AI, Westlaw Precision AI / CoCounsel, Briefpoint, Lawmatics |
| HS SaaS (10, BigChange folded into simPRO entry per research) | ServiceTitan, Jobber, Housecall Pro, FieldEdge, Workiz, Service Fusion, RazorSync, GorillaDesk, simPRO, BuildOps |
| HS AI (9, with ServiceTitan Vera covered as a section inside ServiceTitan rather than standalone) | Avoca, Hatch, Sera, Rilla, Goodcall, Rosie, LeadTruffle, Trillet, Chirp |

Path pattern: `/tools/{slug}/` (existing site convention).

### Skipped vendors (research-flagged risks)

| Vendor | Reason |
|---|---|
| Robin AI | Managed services arm sold to Scissero (Dec 2025); engineering team acquihired by Microsoft (Jan 2026). SaaS continuity uncertain. |
| BigChange | Acquired by simPRO Group; cover under simPRO entry, no standalone page. |
| ServiceTitan Vera | Feature within ServiceTitan, not standalone vendor; cover as section within ServiceTitan profile. |

## Templates

| Page type | Existing template? | Work required |
|---|---|---|
| Industry hub | Yes — existing `/industries/{slug}/` template | Extend existing function; add 2 new industry entries (legal, home-services) |
| Scope landing | New — close to existing category-landing template | New function `render_scope_landing()` taking industry + scope + tool list; reuses category-page chrome, breadcrumb, footer |
| Comparison | Yes — existing `/compare/` template | No template change; data entries in `_comparisons_4.py` |
| Best-for guide | Yes — existing ICP-guide template fits this shape | Extension to handle non-ICP guide indexing; data in `guides_vertical.py` |

**Net new template work**: 1 function (`render_scope_landing`). All other pages reuse existing templates with new data.

### Email-capture slot in templates

Add to scope landing + comparison + guide templates: a single `<form>` block (email field + button) wired to existing newsletter cross-promo Formspree endpoint. Routes by page-context to most-relevant existing newsletter (DataStack Guide for SaaS pages, RevOps Report for AI tooling pages, etc.). One template addition reused across all four page types.

## Data file plan

```
content/industries_legal.py            [new]   Legal SaaS + AI tool entries, sub-cluster defs
content/industries_home_services.py    [new]   HS SaaS + AI tool entries, sub-cluster defs
content/_comparisons_4.py              [new]   24 new comparison entries (sequel to existing _1/_2/_3)
content/guides_vertical.py             [new]   16 new guide entries
build.py                               [edit]  Register new industries, render scope landings, wire imports, render guides via vertical guide template
```

Five files touched in Wave 1. No changes to existing data.

## Content patterns per page type

### Industry hub — `/industries/{vertical}/`
**Length: 1,500-2,000 words. Floor: 1,500.**

Required sections:
- H1 + intro paragraph framing the industry's software landscape (~150-200 words)
- "Top sub-categories in [industry]" cards linking to the two scope landings, each card with a 2-3 sentence positioning blurb
- "State of [industry] software 2026" overview paragraph covering market dynamics, regulatory backdrop where relevant, common buyer triggers
- "Most-compared tools" callout linking to the top 4-6 comparison pages in this industry
- "Buyer guides for [industry]" list linking to all 8 best-for guides
- FAQ block (3-5 industry-level questions: pricing typicals, deployment patterns, integration norms)

Schema: BreadcrumbList, ItemList for sub-category cards, FAQPage if FAQs present.

Internal linking minimum: 10 (both scope landings, all 12 comparisons in industry, all 8 guides in industry).

### Scope landing — `/industries/{vertical}/{scope}/`
**Length: 2,000-3,000 words. Floor: 2,000.**

Required sections:
- H1 + verdict-up-front intro (~150 words). Example for legal/ai/: "If you're a personal-injury firm, EvenUp or Eve. If you're a transactional shop, Spellbook. If you're enterprise, Harvey."
- "How we picked" methodology paragraph (~100 words)
- Sub-cluster sections — each sub-cluster from research gets its own 200-300 word framing, with 2-4 vendors mini-reviewed inside (each mini-review ~80-120 words: verdict, who it's best for, key differentiator, pricing line, vendor link)
- Buyer's framework section (~250 words) — how to evaluate vendors in this category (5-7 evaluation criteria with reasoning)
- Pricing landscape overview (~150 words) — typical price ranges by tier, what drives pricing variance
- Market trends paragraph (~150 words) — what's changing in this category, who's gaining ground, who's losing
- "Comparisons in this category" callout linking to all 6 in-scope comparisons
- "Guides for this category" linking to all 4 in-scope guides
- FAQ block (4-6 Qs)

Schema: BreadcrumbList, ItemList of vendors, FAQPage.

Internal linking minimum: 8 (industry hub, sibling scope, all 6 in-scope comparisons, all 4 in-scope guides).

### Comparison — `/compare/{a-slug}-vs-{b-slug}/`
**Length: 2,500-3,500 words. Floor: 2,500.**

Required sections:
- H1 with both vendor names
- Verdict-up-front intro (~200 words): explicit winner per use case ("Clio wins on integrations and BigLaw fit; MyCase wins on intake automation and price for solos")
- Feature-by-feature comparison table (10-12 dimensions): pricing, user model, document automation, trust accounting / compliance, mobile experience, integrations, reporting, support, security, deployment model, learning curve, customer concentration
- "Where [Vendor A] wins" section (~400 words): 3-4 specific judgments with reasoning. Each judgment must contain unique signal not findable on the vendor's own marketing site.
- "Where [Vendor B] wins" section (~400 words, same shape)
- "Choose [A] if..." / "Choose [B] if..." callouts (~150 words each)
- Pricing-scenario walkthrough (~300 words): real cost for a typical customer profile (e.g. "for a 5-attorney firm with one paralegal")
- "If you're switching from [other tool]" migration paragraph if applicable
- Integrations comparison section (~250 words)
- FAQs (4-6, ~400 words)

Schema: BreadcrumbList, FAQPage, two SoftwareApplication entries (one per vendor).

Internal linking minimum: 6 (scope landing, industry hub, related comparisons involving either vendor, related guides where both appear).

### Best-for guide — `/guides/{slug}/`
**Length: 3,000-4,000 words. Floor: 3,000.**

Required sections:
- H1, intro framing the use case + ICP (~200 words: who this guide is for, what they're solving)
- Verdict-up-front: top pick + when-to-pick alternatives (~150 words)
- "How we picked" methodology paragraph (~150 words)
- Ranked recommendations (5-7 vendors). Each: 2-paragraph review (~250 words), verdict, who it's best for, key features, pricing line, vendor link.
- "What to look for in [category]" buyer's-guide section (~600 words): 8-12 evaluation criteria, each with 2-paragraph explanation
- Pricing-scenario tables (~250 words): typical cost at three customer-size tiers
- "What to avoid" pitfalls section (~250 words): common bad-vendor patterns specific to this category
- "Questions to ask vendors" checklist (~200 words)
- FAQ block (5-7 Qs, ~500 words)
- "Related comparisons" callout linking to the relevant `/compare/` pages
- "Related guides" callout linking to other in-scope guides

Schema: BreadcrumbList, ItemList of recommendations, FAQPage.

Internal linking minimum: 6.

## Content quality gates

Every page passes all eight gates before deploy.

### Gate 1: Writing-style audit (ROME_WRITING_STYLE.md)
Run `/ai-audit` skill or manual scan. Page fails if any of:
- Em-dashes present
- Negative parallelism: "not X, it's Y", "not just X, but Y", "isn't X, it's Y", "don't X. They Y."
- Unearned declarations: "Here's the thing", "The bottom line is", "What this means is", "The pattern is clear", "X made one thing clear", "One thing is certain", "The numbers:", "The takeaway:", "That matters because"
- Banned words: robust, leverage, synergy, holistic, cutting-edge, game-changer, paradigm shift, genuinely, truly, really, actually, quite, extremely, "continues to", "in today's market", "navigate the landscape"
- Dramatic fragment triads (three short punchy sentences in sequence for manufactured emphasis)
- Anaphora abuse (parallel sentence openings repeating same structure)
- Manufactured surprise ("This caught me off guard", "I didn't expect this")
- Self-answered rhetorical questions
- Tautologies ("Time will tell", "Success depends on execution")
- Pompous verb substitutions for "is" (serves as, stands as, marks, represents, signals)
- Bold-first bullet lists in prose

### Gate 2: Verdict-up-front
Comparisons and guides state their recommendation in the first 100 words. No throat-clearing. Industry hubs and scope landings still need a clear positioning statement in the intro.

### Gate 3: Specific numbers
- Pricing in dollars where publicly available ("$49/u/mo Essentials" not "affordable pricing")
- Employee counts and funding rounds where known and material
- Specific dates for product launches, funding events, major releases

### Gate 4: Unique value (programmatic-SEO defensibility)
- Each comparison contains ≥3 specific judgments not findable on either vendor's marketing site
- Each guide has a real ranked recommendation with reasoning, not a feature dump
- No two pages share more than ~30% prose (run a similarity check at audit time)

### Gate 5: Internal linking minimums
- Industry hub: ≥10 internal links
- Scope landing: ≥8
- Comparison: ≥6
- Guide: ≥6

### Gate 6: Affiliate-ready link target
Every vendor mention links once per page via `<a href="{vendor_url}" class="affiliate-link" rel="nofollow noopener" target="_blank">`. Vendor URL is the homepage now; swap to affiliate URL when programs activate (one find-replace per vendor per data file).

### Gate 7: Schema.org markup
- BreadcrumbList universal
- FAQPage where FAQs exist
- ItemList for ranked vendor lists (scope landings, guides)
- SoftwareApplication on comparison pages (one entry per vendor)

### Gate 8: Word count floor
Page below floor (per page-type table above) fails audit. Floor enforcement is a build-script grep on rendered HTML word count, with a warning emitted at build time.

## Build order inside Wave 1

1. **Day 1 — structure deploy**: industry hubs + scope landings as skeletons (intro + sub-cluster sections + internal-link scaffolding). Deploy live so Google can crawl URL structure early.
2. **Days 2-7 — best-for guides**: write all 16. Highest-volume search intent, longest pages, most content effort.
3. **Days 8-14 — comparisons**: write all 24. Branded "X vs Y" search has the lowest authority gate, ranks fastest.
4. **Day 15 — internal linking pass**: every page links to relevant siblings per Gate 5 minimums.
5. **Day 16 — content quality audit**: run all 8 gates on every page. Fix failures inline.
6. **Day 17 — deploy via `./deploy.sh`**. Monitor GSC + GA4 daily for ranking signal.

Total Wave 1 ship time: ~17 days at full focus, longer at part-time.

## Wave 2 + Wave 3 outline

Identical structure to Wave 1, with industries chosen via fresh research at the start of each wave.

- **Wave 2** (provisional): Veterinary + Financial Advisor. ~46 structural pages + ~36 vendor profiles in Wave 2.5.
- **Wave 3** (provisional): Construction + Agriculture. Same structure.

Provisional industry order is reviewable post-Wave 1 based on which sub-categories are showing ranking signal.

## Out of scope for this expansion

- Vendor profile pages in Wave 1 (deferred to Wave 1.5)
- Dedicated b2bsalestools email list (deferred to phase 2 once traffic justifies)
- A redesigned homepage or new top-level navigation (existing nav extends naturally via the new `/industries/` entries)
- The other six contact-data brands (Vettica, Lexica, etc.) — separate codebases, not touched
- Any Provyx-side changes — Provyx CTA template slot is the only b2bsalestools-side acknowledgment; copy and conversion logic for Provyx live in the Provyx codebase
- Affiliate-program signups (deferred until traffic justifies application acceptance)

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| 140K words is a content-quality risk: rushed prose fails Gate 1 + Gate 4 | Write in batches (per scope, not all-at-once), audit each batch before moving on. If more than 20% of pages in a batch fail any of Gates 1-4 on the first audit pass, stop writing the next batch and recalibrate (revise prompts, regenerate failing pages individually, or re-scope). |
| Vertical-AI vendor landscape shifts (acquisitions, shutdowns) between research and ship | Re-verify vendor URLs and status the day before deploy. Robin AI is the current example. |
| Existing build.py is 5K lines of inline f-strings — modifications risk regressions in the existing 190 pages | Add new render functions alongside existing ones. Don't refactor existing tool/comparison/guide rendering. Diff the rendered output of an existing page before and after Wave 1 to confirm no regression. |
| Affiliate links empty (homepage URLs) means no monetization in Wave 1 | Accepted. Site convention. Apply for programs once traffic justifies. |
| GA4 currently shows 22 weekly views, 0s engagement — Wave 1 may not change ranking quickly | Accepted. Programmatic SEO ranks on a 3-6 month horizon, not days. Deploy and wait. |

## Acceptance criteria for Wave 1 implementation plan

The implementation plan (next step, via writing-plans skill) must:
1. Break the 17-day build into discrete tasks
2. Identify which `/content/*.py` files each task touches
3. Specify the audit command for each gate
4. Include a regression-test step (rendered-HTML diff for one existing tool page before/after build.py changes) to confirm no Wave 1 changes broke existing 190 pages
5. Include the deploy step + GSC/GA4 monitoring plan for the 8 weeks following deploy

## Constraint refinements (2026-05-05 review)

After self-evaluation, the following constraints were clarified:

- **No affiliate revenue currently**, so FTC affiliate disclosure copy is not a launch blocker. Existing `class="affiliate-link"` markup is sufficient. Add disclosure copy when affiliate programs activate.
- **No current traffic** (~22 weekly views per GA4). The whole purpose of this expansion is to build content that captures traffic over a 3-12 month horizon. Don't optimize for conversion-rate or audience-capture mechanisms that require traffic to validate.
- **E-E-A-T / authorship is already handled** by existing `build.py` author functions. New render functions for scope landings, comparisons, and guides must call the same author/methodology helpers (`By Rome Thorndike` + LinkedIn link + "Reviewed by... Last verified {BUILD_DATE}" + methodology paragraph). No new bio content needed.
- **Image strategy deferred to a later wave.** No vendor logos, hero images, or OG cards in Wave 1. Pages are text-only with existing site CSS. Run `/image-seo-audit` after Wave 1 ships to plan a retro image pass.
- **Aggregator-competition principle (added per gap-3 review)**: every guide and scope landing must use **opinionated rankings + niche use-case framing** to differentiate from G2/Capterra/Software Advice. Generic "best [category] software" framing is forbidden — every guide must specify a use case, firm size, or buyer profile in its angle. Sort by editorial verdict, not by user-rating proxies.
- **First-party data leverage**: where Rome's vertical contact-data brands (Vettica/Lexica/SubForge/etc.) have publishable counts (e.g. "12,847 personal-injury law firms in the US per our database"), surface them in scope landings as a "by-the-numbers" callout. One per scope landing, sourced + dated.
- **Search-intent validation**: before writing each batch, spot-check the slug against actual search-volume data (Lookout / Ahrefs / SEMrush / Keyword Planner). If a comparison or guide returns 0 monthly searches, drop it and substitute a higher-volume alternative from the research output.
- **Internal linking from existing pages**: after Wave 1 deploys, run a retroactive linking pass — scan existing 190 pages for topical fit with new pages and add 2-3 contextual links per relevant existing page. Captured as a Day-15+1 follow-up task.
- **Wave 2 trigger criteria**: proceed to Wave 2 if Wave 1 hits ≥500 GSC impressions OR ≥50 clicks within 8 weeks of deploy. If neither metric hits, diagnose what's not ranking before adding more pages.
- **Refresh cadence**: each new content data entry includes a `last_verified` field (defaulting to BUILD_DATE). Quarterly refresh review for all Wave 1 pages, with stale-data verification before each rebuild.

## References

- **Site repo**: `/Users/rome/Documents/websites/content/b2bsalestools/`
- **Build system**: `/Users/rome/Documents/websites/content/b2bsalestools/build.py` (~5K lines, monolithic raw f-string renderer)
- **Existing convention doc**: `/Users/rome/Documents/websites/content/b2bsalestools/HANDOFF.md`
- **Deploy script**: `/Users/rome/Documents/websites/content/b2bsalestools/deploy.sh` (force-pushes `output/` to `gh-pages` branch)
- **Existing content modules**: `/Users/rome/Documents/websites/content/b2bsalestools/content/` (tools_*.py, _categories_*.py, _comparisons_*.py, alternatives.py, guides.py, articles.py)
- **Writing style guide**: `/Users/rome/Documents/AI News Digest/Claude/ROME_WRITING_STYLE.md`
- **AI audit catalog**: `/Users/rome/Documents/marketingskills/skills/seo-audit/references/ai-writing-detection.md`
- **Programmatic SEO playbook**: `/Users/rome/Documents/marketingskills/skills/programmatic-seo/SKILL.md`
- **AI audit skill**: `/ai-audit` (Claude Code user-invocable skill)
- **Wave 1 vendor research output**: captured in this spec's tables; re-run research for Wave 2 and Wave 3 at the start of those waves.
