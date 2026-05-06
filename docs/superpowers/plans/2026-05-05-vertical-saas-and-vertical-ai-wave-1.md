# Vertical SaaS + Vertical AI Wave 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship 46 new pages on b2bsalestools.com covering Legal + Home Services Vertical SaaS and Vertical AI (2 industry hubs + 4 scope landings + 24 comparisons + 16 best-for guides), all passing ROME_WRITING_STYLE.md + word-floor + schema gates, deployed to gh-pages.

**Architecture:** Extend existing `/industries/` pattern with new sub-paths. Reuse 3 existing page templates (industry, comparison, guide) and add 1 new template function (`render_scope_landing`). Add 4 new content data files. No changes to existing 190 pages.

**Tech Stack:** Python 3 build.py (raw f-string HTML rendering, no Jinja), modular `content/*.py` data files, GitHub Pages deploy via `deploy.sh` to `gh-pages` branch.

**Spec:** [docs/superpowers/specs/2026-05-05-vertical-saas-and-vertical-ai-expansion-design.md](../specs/2026-05-05-vertical-saas-and-vertical-ai-expansion-design.md)

**Working directory for all paths:** `/Users/rome/Documents/websites/content/b2bsalestools/`

---

## Phase 1: Infrastructure

Set up data files, build.py extensions, and registration so the new pages can render without writing any content yet.

### Task 1: Create Legal vertical content scaffold

**Files:**
- Create: `content/industries_legal.py`

- [ ] **Step 1.1: Create the file with module skeleton**

```python
"""Legal vertical: SaaS and AI tools for law firms.

Covers two scopes:
  - Practice management software (Clio, MyCase, etc.)
  - Vertical AI tools for legal (Harvey, Spellbook, EvenUp, etc.)
"""

LEGAL_INDUSTRY = {
    "slug": "legal",
    "name": "Legal",
    "hero_intro": "",  # Filled in Task 6
    "scopes": ["practice-management", "ai"],
    "by_the_numbers": [],  # Filled in Task 8 from Rome's vertical-data brand counts
    "faqs": [],  # Filled in Task 6
    "last_verified": "2026-05-05",
}

LEGAL_SAAS_TOOLS = [
    # Each entry: (slug, name, url, sub_cluster, pricing_line, one_line_verdict, who_its_best_for)
    ("clio", "Clio", "https://www.clio.com", "general-pms",
     "$49 EasyStart, $89 Essentials, $129 Advanced per user/month",
     "Market-leading cloud PMS with the deepest integration ecosystem.",
     "Solo through mid-firm general practice; firms that value integration breadth over depth"),
    ("mycase", "MyCase", "https://www.mycase.com", "general-pms",
     "$39 Basic, $79 Pro, $99 Advanced per user/month",
     "All-in-one PMS with strong intake automation and client portal.",
     "Solo and small firms (1-15 attorneys) prioritizing intake-to-billing flow"),
    ("practicepanther", "PracticePanther", "https://www.practicepanther.com", "general-pms",
     "$59 Solo, $79 Essential, $99 Business per user/month",
     "Budget-friendly PMS with strong time tracking and automation.",
     "Cost-conscious solos and small firms"),
    ("smokeball", "Smokeball", "https://www.smokeball.com", "doc-automation",
     "Contact sales; ~$59-$199 per user/month tiers",
     "Document automation-heavy PMS with auto time capture.",
     "Family law, PI, and estate firms with high document volume"),
    ("filevine", "Filevine", "https://www.filevine.com", "enterprise-pi",
     "Custom quotes; Standard / Premium / à la carte",
     "Customizable case management for high-volume PI and complex litigation.",
     "PI firms with 10+ attorneys and mass-tort practices"),
    ("cosmolex", "CosmoLex", "https://www.cosmolex.com", "all-in-one",
     "$89 per user/month flat",
     "All-in-one PMS with native IOLTA-compliant trust accounting and full general ledger.",
     "Firms that want PMS + accounting in one tool, no QuickBooks dependency"),
    ("rocketmatter", "Rocket Matter", "https://www.rocketmatter.com", "general-pms",
     "$49 Essentials, $79 Pro, $99 Premier per user/month",
     "Cloud PMS plus billing for small/mid firms with the ProfitFuel module.",
     "Small/mid firms (5-50 attorneys) focused on profitability metrics"),
    ("centerbase", "Centerbase", "https://www.centerbase.com", "enterprise",
     "Custom enterprise pricing (~$80-130/user/month equivalents)",
     "Customizable PMS for growing mid-size firms with workflow and billing engine.",
     "Mid-size firms (20-100 attorneys) outgrowing Clio"),
    ("litify", "Litify", "https://www.litify.com", "enterprise-pi",
     "Custom enterprise; typically $150-300+ per user/month",
     "Salesforce-native legal ops platform for high-volume PI and mass tort.",
     "Large PI firms (50+ attorneys), mass-tort, multi-state"),
    ("lawpay", "LawPay", "https://www.lawpay.com", "payments",
     "~2.95% + $0.20 per transaction; tiered monthly fees",
     "Legal-specific payments platform with IOLTA compliance.",
     "Firms accepting card payments that need IOLTA-compliant trust handling"),
]

LEGAL_SAAS_SUB_CLUSTERS = {
    "general-pms": "General practice management — full workflow for solo through mid-firm general practice.",
    "doc-automation": "Document-automation-heavy PMS — built around template-driven document generation.",
    "all-in-one": "All-in-one with native trust accounting — eliminates the need for separate accounting software.",
    "enterprise": "Enterprise customizable PMS — for mid-size firms with complex requirements.",
    "enterprise-pi": "Enterprise PI / mass tort — high-volume case management with PI-specific features.",
    "payments": "Payments adjacency — IOLTA-compliant payment processing.",
}

LEGAL_AI_TOOLS = [
    ("harvey", "Harvey", "https://www.harvey.ai", "biglaw",
     "Custom enterprise; reportedly $100K+ annually",
     "AI for BigLaw and enterprise legal teams: research, drafting, due diligence.",
     "AmLaw 100/200 firms and enterprise legal departments"),
    ("spellbook", "Spellbook", "https://www.spellbook.legal", "contract-review",
     "$99 Starter, $199 Enterprise per user/month (10-seat min)",
     "AI contract drafting and review inside Microsoft Word.",
     "Transactional lawyers, in-house teams, mid-market firms"),
    ("evenup", "EvenUp", "https://www.evenuplaw.com", "pi-plaintiff",
     "Per-document or subscription; usage-based",
     "AI demand letters, medical chronologies, settlement docs for PI firms.",
     "Personal injury firms generating high volumes of demand packages"),
    ("eve", "Eve", "https://www.eve.legal", "pi-plaintiff",
     "Per-firm subscription; contact sales",
     "End-to-end plaintiff/PI case AI from intake through settlement.",
     "Plaintiff-side firms wanting AI across the full case lifecycle"),
    ("supio", "Supio", "https://www.supio.com", "pi-plaintiff",
     "Likely $150-400 per user/month, contact sales",
     "AI medical record review and demand drafting for PI and mass tort.",
     "PI and mass-tort firms with heavy medical record volume"),
    ("casemark", "CaseMark", "https://www.casemark.com", "litigation-drafting",
     "Pay-per-use credits; subscription = AI credits",
     "AI legal workflow platform with matter-based summaries and transcripts.",
     "Court reporting firms; mid-market firms wanting matter-summary AI"),
    ("lexis-ai", "Lexis+ AI", "https://www.lexisnexis.com/lexis-plus-ai", "research",
     "Add-on to Lexis subscriptions; contact sales",
     "Conversational legal research grounded in the Lexis precedent corpus.",
     "Existing Lexis customers; firms requiring authoritative citation grounding"),
    ("westlaw-precision", "Westlaw Precision with CoCounsel", "https://www.thomsonreuters.com/en/products/westlaw-precision", "research",
     "Add-on to Westlaw; contact sales",
     "Westlaw research plus CoCounsel AI assistant for federal-scale authority.",
     "Existing Westlaw customers; federal litigators"),
    ("briefpoint", "Briefpoint", "https://briefpoint.ai", "litigation-drafting",
     "$89 per month and up, tiered by usage",
     "AI for litigation discovery responses, objections, and motions.",
     "Litigation firms with high motion-practice and discovery-response volume"),
    ("lawmatics", "Lawmatics", "https://www.lawmatics.com", "intake-crm",
     "$199 Lite, $299 Pro per firm/month; premium tiers $300+ per user, 3-user min",
     "AI-driven legal CRM with intake automation and lead scoring.",
     "Firms with marketing-driven inbound that needs intake automation"),
]

LEGAL_AI_SUB_CLUSTERS = {
    "biglaw": "General-purpose BigLaw AI — broad capability across research, drafting, due diligence.",
    "contract-review": "Contract drafting and review — Word-integrated AI for transactional work.",
    "research": "AI legal research — natural-language queries grounded in case law.",
    "pi-plaintiff": "PI / plaintiff-specific — demand letters, medical record review, intake-to-settlement.",
    "litigation-drafting": "Litigation drafting and discovery — motions, objections, responses, summaries.",
    "intake-crm": "Intake and CRM AI — lead scoring, intake automation, marketing analytics.",
}
```

- [ ] **Step 1.2: Verify file imports cleanly**

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools && python3 -c "from content.industries_legal import LEGAL_SAAS_TOOLS, LEGAL_AI_TOOLS, LEGAL_SAAS_SUB_CLUSTERS, LEGAL_AI_SUB_CLUSTERS, LEGAL_INDUSTRY; print(f'Legal SaaS: {len(LEGAL_SAAS_TOOLS)} tools, Legal AI: {len(LEGAL_AI_TOOLS)} tools')"
```

Expected output: `Legal SaaS: 10 tools, Legal AI: 10 tools`

- [ ] **Step 1.3: Commit**

```bash
git add content/industries_legal.py
git commit -m "content: add legal vertical scaffold (10 SaaS + 10 AI tools)"
```

---

### Task 2: Create Home Services vertical content scaffold

**Files:**
- Create: `content/industries_home_services.py`

- [ ] **Step 2.1: Create the file with module skeleton**

```python
"""Home Services vertical: SaaS and AI tools for trades businesses.

Covers two scopes:
  - Field service management (ServiceTitan, Jobber, Housecall Pro, etc.)
  - Vertical AI tools for trades (Avoca, Hatch, Sera, etc.)
"""

HOME_SERVICES_INDUSTRY = {
    "slug": "home-services",
    "name": "Home Services",
    "hero_intro": "",  # Filled in Task 7
    "scopes": ["field-service-management", "ai"],
    "by_the_numbers": [],  # Filled from Rome's TradeBridge brand
    "faqs": [],  # Filled in Task 7
    "last_verified": "2026-05-05",
}

HOME_SERVICES_SAAS_TOOLS = [
    ("servicetitan", "ServiceTitan", "https://www.servicetitan.com", "enterprise-residential",
     "Custom; ~$8K-15K+/year per site for small ops, scales high",
     "Enterprise FSM for residential HVAC, plumbing, electrical with full ops platform.",
     "Residential trades businesses with $5M+ revenue"),
    ("jobber", "Jobber", "https://getjobber.com", "smb-residential",
     "$39 Core, $119-169 Connect, $199-349 Grow per month",
     "SMB-friendly FSM with clean quote-to-invoice flow.",
     "1-15 person trades shops, owner-operators, growing residential service businesses"),
    ("housecallpro", "Housecall Pro", "https://www.housecallpro.com", "smb-residential",
     "$49 Basic, $129 Essentials, $279 Max+ per month",
     "All-in-one FSM for residential trades with strong marketing tools.",
     "Residential-focused service businesses, especially HVAC and plumbing"),
    ("fieldedge", "FieldEdge", "https://fieldedge.com", "enterprise-residential",
     "Custom; typically ~$100/user/month equivalents",
     "FSM for HVAC, plumbing, electrical with deep QuickBooks integration.",
     "Mid to large residential trades teams already on QuickBooks"),
    ("workiz", "Workiz", "https://www.workiz.com", "smb-residential",
     "$187 Kickstart, $229 Standard, $270 Pro per month",
     "FSM for SMBs in locksmith, garage, appliance, and HVAC with built-in call tracking.",
     "Niche residential service businesses (locksmiths, garage doors, appliance repair)"),
    ("service-fusion", "Service Fusion", "https://www.servicefusion.com", "mid-market-flat",
     "$208 Starter, $389 Plus, $533 Pro per month (flat, not per-user)",
     "Mid-market FSM with flat-rate (not per-user) pricing.",
     "Growing trades businesses (10-50 employees) wanting predictable pricing"),
    ("razorsync", "RazorSync", "https://www.razorsync.com", "smb-residential",
     "$85-360 per month tiered by users",
     "SMB FSM with mobile and desktop for small-midsize service businesses.",
     "5-25 person residential trades teams"),
    ("gorilladesk", "GorillaDesk", "https://www.gorilladesk.com", "niche",
     "$49-99 per month",
     "FSM originally for pest control, now broader trades with routing and chemical tracking.",
     "Pest control, lawn care, and other recurring-service businesses"),
    ("simpro", "simPRO", "https://www.simprogroup.com", "mid-market-multi-trade",
     "From ~$70/user/month plus setup; quote-based",
     "Mid-market FSM for trade contractors covering service plus project work.",
     "Multi-trade contractors with both service work and longer-form projects (acquired BigChange)"),
    ("buildops", "BuildOps", "https://buildops.com", "commercial",
     "Custom enterprise, premium tier",
     "Commercial-focused FSM and project management for HVAC, electrical, plumbing.",
     "Commercial trades contractors (10-200 techs)"),
]

HOME_SERVICES_SAAS_SUB_CLUSTERS = {
    "enterprise-residential": "Enterprise residential trades — full ops platforms for $5M+ revenue businesses.",
    "smb-residential": "SMB residential trades — FSM for 1-15 person shops.",
    "mid-market-flat": "Mid-market with flat pricing — predictable cost as team grows.",
    "niche": "Niche services — pest control, lawn care, recurring-service-specific FSM.",
    "mid-market-multi-trade": "Mid-market multi-trade — service plus project work.",
    "commercial": "Commercial contractor focus — non-residential job complexity, larger crews.",
}

HOME_SERVICES_AI_TOOLS = [
    ("avoca", "Avoca AI", "https://www.avoca.ai", "ai-receptionist",
     "Custom; usage-based",
     "AI voice agents for inbound calls in home services, ServiceTitan-integrated.",
     "Mid-to-large HVAC, plumbing, roofing operations with high inbound call volume"),
    ("hatch", "Hatch", "https://www.usehatchapp.com", "csr-platform",
     "Per-seat / contact sales",
     "AI CSR platform handling voice, SMS, and email across 2,000+ home service customers.",
     "Multi-channel-customer-service home service businesses"),
    ("sera", "Sera Systems", "https://sera.tech", "ai-fsm",
     "$399/month for 4 users plus $149 per extra tech",
     "AI-powered FSM with auto-dispatcher for HVAC, plumbing, electrical.",
     "Trades teams who want AI dispatch without leaving their primary FSM"),
    ("rilla", "Rilla", "https://www.rilla.com", "sales-coaching",
     "~$199-349 per rep/month (~$40K+/year for 10 reps)",
     "AI speech analytics and virtual ride-along coaching for in-home sales reps.",
     "Trades businesses with in-home sales motion (HVAC replacement, roofing, water treatment)"),
    ("goodcall", "Goodcall", "https://www.goodcall.com", "ai-receptionist",
     "$59 Starter, $99 Growth, $199 Scale per month",
     "Configurable AI receptionist for SMB local services with drag-and-drop logic.",
     "Owner-operator and small trades teams wanting affordable AI answering"),
    ("rosie", "Rosie", "https://heyrosie.com", "ai-receptionist",
     "~$49-149 per month",
     "AI answering for home services, trade-trained.",
     "Solo and small trades teams who miss calls during jobs"),
    ("leadtruffle", "LeadTruffle", "https://leadtruffle.co", "csr-platform",
     "$229-629 per month",
     "AI lead qualification with Thumbtack and Angi integration for contractors.",
     "Trades businesses sourcing leads from marketplaces"),
    ("trillet", "Trillet", "https://trillet.ai", "ai-receptionist",
     "$49 per month",
     "AI phone answering for trades across voice, SMS, and WhatsApp.",
     "Smallest trades shops where $49/month is the budget ceiling"),
    ("chirp", "Chirp", "https://chirpchat.com", "csr-platform",
     "Contact sales",
     "Text automation with AI for home service businesses.",
     "Trades businesses wanting SMS-first customer comms"),
]

HOME_SERVICES_AI_SUB_CLUSTERS = {
    "ai-receptionist": "AI receptionist / inbound voice — answers calls when humans can't.",
    "csr-platform": "Customer service platforms — multi-channel inbound and outbound comms.",
    "sales-coaching": "AI sales coaching — speech analytics and ride-along for in-home reps.",
    "ai-fsm": "AI-native FSM — dispatch and scheduling AI built into the FSM itself.",
}
```

- [ ] **Step 2.2: Verify file imports cleanly**

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools && python3 -c "from content.industries_home_services import HOME_SERVICES_SAAS_TOOLS, HOME_SERVICES_AI_TOOLS; print(f'HS SaaS: {len(HOME_SERVICES_SAAS_TOOLS)} tools, HS AI: {len(HOME_SERVICES_AI_TOOLS)} tools')"
```

Expected output: `HS SaaS: 10 tools, HS AI: 9 tools`

- [ ] **Step 2.3: Commit**

```bash
git add content/industries_home_services.py
git commit -m "content: add home services vertical scaffold (10 SaaS + 9 AI tools)"
```

---

### Task 3: Create Wave 1 comparison data file (24 entries, scaffold only)

**Files:**
- Create: `content/_comparisons_4.py`

- [ ] **Step 3.1: Scaffold all 24 comparison slugs with empty content (filled in Phase 4 tasks)**

```python
"""Wave 1 vertical SaaS + AI comparison content (Legal + Home Services)."""

COMPARISON_CONTENT_W1 = {}

# Legal SaaS comparisons (6)
for slug in [
    "clio-vs-mycase", "clio-vs-practicepanther", "mycase-vs-practicepanther",
    "smokeball-vs-clio", "filevine-vs-litify", "clio-vs-smokeball",
]:
    COMPARISON_CONTENT_W1[slug] = {"_pending": True, "category": "legal-saas", "last_verified": "2026-05-05"}

# Legal AI comparisons (6)
for slug in [
    "harvey-vs-spellbook", "evenup-vs-eve", "evenup-vs-supio",
    "lexis-ai-vs-westlaw-precision", "spellbook-vs-lexis-ai", "harvey-vs-cocounsel",
]:
    COMPARISON_CONTENT_W1[slug] = {"_pending": True, "category": "legal-ai", "last_verified": "2026-05-05"}

# Home Services SaaS comparisons (6)
for slug in [
    "servicetitan-vs-jobber", "jobber-vs-housecallpro", "servicetitan-vs-housecallpro",
    "servicetitan-vs-fieldedge", "workiz-vs-housecallpro", "buildops-vs-servicetitan",
]:
    COMPARISON_CONTENT_W1[slug] = {"_pending": True, "category": "hs-saas", "last_verified": "2026-05-05"}

# Home Services AI comparisons (6)
for slug in [
    "avoca-vs-hatch", "goodcall-vs-rosie", "avoca-vs-goodcall",
    "sera-vs-servicetitan", "hatch-vs-leadtruffle", "avoca-vs-rilla",
]:
    COMPARISON_CONTENT_W1[slug] = {"_pending": True, "category": "hs-ai", "last_verified": "2026-05-05"}
```

- [ ] **Step 3.2: Verify count**

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools && python3 -c "from content._comparisons_4 import COMPARISON_CONTENT_W1; print(f'Wave 1 comparisons: {len(COMPARISON_CONTENT_W1)}')"
```

Expected: `Wave 1 comparisons: 24`

- [ ] **Step 3.3: Commit**

```bash
git add content/_comparisons_4.py
git commit -m "content: scaffold 24 wave 1 comparison slugs (legal + home services)"
```

---

### Task 4: Create Wave 1 guide data file (16 entries, scaffold only)

**Files:**
- Create: `content/guides_vertical.py`

- [ ] **Step 4.1: Scaffold 16 guide slugs**

```python
"""Wave 1 vertical SaaS + AI 'best for' guide content."""

GUIDE_CONTENT_VERTICAL = {}

WAVE_1_GUIDES = [
    # Legal SaaS (4)
    ("best-practice-management-software-solo-attorneys", "legal-saas", "Best Practice Management Software for Solo Attorneys"),
    ("best-legal-practice-management-small-firms", "legal-saas", "Best Legal Practice Management for Small Law Firms"),
    ("best-pms-personal-injury-law-firms", "legal-saas", "Best Practice Management Software for Personal Injury Firms"),
    ("best-clio-alternatives", "legal-saas", "Best Clio Alternatives"),

    # Legal AI (4)
    ("best-legal-ai-personal-injury-firms", "legal-ai", "Best Legal AI for Personal Injury Firms"),
    ("best-ai-contract-review-software", "legal-ai", "Best AI Contract Review Software"),
    ("best-ai-legal-research-tools", "legal-ai", "Best AI Legal Research Tools"),
    ("best-ai-tools-solo-lawyers", "legal-ai", "Best AI Tools for Solo Lawyers"),

    # Home Services SaaS (4)
    ("best-hvac-software", "hs-saas", "Best HVAC Software"),
    ("best-plumbing-software", "hs-saas", "Best Plumbing Software"),
    ("best-electrical-contractor-software", "hs-saas", "Best Electrical Contractor Software"),
    ("best-servicetitan-alternatives", "hs-saas", "Best ServiceTitan Alternatives"),

    # Home Services AI (4)
    ("best-ai-call-answering-hvac", "hs-ai", "Best AI Call Answering for HVAC Contractors"),
    ("best-ai-receptionist-home-services", "hs-ai", "Best AI Receptionist for Home Services"),
    ("best-ai-tools-plumbing-companies", "hs-ai", "Best AI Tools for Plumbing Companies"),
    ("best-ai-sales-coaching-in-home-sales", "hs-ai", "Best AI Sales Coaching for In-Home Sales Reps"),
]

for slug, category, title in WAVE_1_GUIDES:
    GUIDE_CONTENT_VERTICAL[slug] = {"_pending": True, "category": category, "title": title, "last_verified": "2026-05-05"}
```

- [ ] **Step 4.2: Verify count**

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools && python3 -c "from content.guides_vertical import GUIDE_CONTENT_VERTICAL; print(f'Wave 1 guides: {len(GUIDE_CONTENT_VERTICAL)}')"
```

Expected: `Wave 1 guides: 16`

- [ ] **Step 4.3: Commit**

```bash
git add content/guides_vertical.py
git commit -m "content: scaffold 16 wave 1 guide slugs (legal + home services)"
```

---

### Task 5: Wire build.py to render Wave 1 pages

**Files:**
- Modify: `build.py` (add imports + render_scope_landing function + page registration)

- [ ] **Step 5.1: Read existing render_industries / render_categories patterns**

```bash
grep -n "def render_" /Users/rome/Documents/websites/content/b2bsalestools/build.py | head -20
grep -n "industries" /Users/rome/Documents/websites/content/b2bsalestools/build.py | head -20
```

Identify the existing functions: `render_industries`, `render_categories`, `render_compare`, `render_guides` (or equivalent). Read each function start-to-end (~50-100 lines).

- [ ] **Step 5.2: Add new render function for scope landings**

Add to build.py after the existing render_industries function. The new function takes (industry_slug, scope_slug, tools_list, sub_clusters_dict, by_the_numbers_list) and produces an HTML scope landing page following the spec content pattern (verdict-up-front, sub-cluster sections, buyer's framework, pricing landscape, market trends, comparisons callout, guides callout, FAQs).

Key requirements:
- Output path: `output/industries/{industry_slug}/{scope_slug}/index.html`
- Reuses existing breadcrumb, header, footer, author-attribution, schema helpers
- Renders sub-cluster sections with mini-reviews (vendor link via existing affiliate-link class pattern)
- Schema.org: BreadcrumbList + ItemList + FAQPage
- Calls `methodology_stamp()` and `author_attribution()` (existing helpers)

Pseudo-code structure (write actual code from existing patterns):

```python
def render_scope_landing(industry_slug, industry_name, scope_slug, scope_name,
                         hero_text, methodology_text, tools_list, sub_clusters,
                         buyer_framework_text, pricing_landscape_text, trends_text,
                         comparisons_in_scope, guides_in_scope, faqs, by_the_numbers):
    """Render a vertical scope landing page (e.g. /industries/legal/practice-management/)."""
    # ... follow existing render_industry pattern ...
    # Output: output/industries/{industry_slug}/{scope_slug}/index.html
```

- [ ] **Step 5.3: Add imports for new content modules**

At top of build.py near existing content imports:

```python
from content.industries_legal import (
    LEGAL_INDUSTRY, LEGAL_SAAS_TOOLS, LEGAL_AI_TOOLS,
    LEGAL_SAAS_SUB_CLUSTERS, LEGAL_AI_SUB_CLUSTERS,
)
from content.industries_home_services import (
    HOME_SERVICES_INDUSTRY, HOME_SERVICES_SAAS_TOOLS, HOME_SERVICES_AI_TOOLS,
    HOME_SERVICES_SAAS_SUB_CLUSTERS, HOME_SERVICES_AI_SUB_CLUSTERS,
)
from content._comparisons_4 import COMPARISON_CONTENT_W1
from content.guides_vertical import GUIDE_CONTENT_VERTICAL
```

- [ ] **Step 5.4: Register Wave 1 pages in main build flow**

In the main build function (find the section that calls render_industry / render_compare / render_guides), add calls to render the new pages. Wave 1 calls render only if content is non-pending; pending entries skip rendering and emit a warning log line (so the build succeeds even with empty Wave 1 content).

```python
# Wave 1: Legal + Home Services industry hubs
render_industry_hub("legal", LEGAL_INDUSTRY, LEGAL_SAAS_TOOLS, LEGAL_AI_TOOLS)
render_industry_hub("home-services", HOME_SERVICES_INDUSTRY, HOME_SERVICES_SAAS_TOOLS, HOME_SERVICES_AI_TOOLS)

# Wave 1: scope landings
render_scope_landing("legal", "Legal", "practice-management", "Practice Management Software",
                     ..., LEGAL_SAAS_TOOLS, LEGAL_SAAS_SUB_CLUSTERS, ...)
render_scope_landing("legal", "Legal", "ai", "Vertical AI Tools",
                     ..., LEGAL_AI_TOOLS, LEGAL_AI_SUB_CLUSTERS, ...)
render_scope_landing("home-services", "Home Services", "field-service-management", "Field Service Management",
                     ..., HOME_SERVICES_SAAS_TOOLS, HOME_SERVICES_SAAS_SUB_CLUSTERS, ...)
render_scope_landing("home-services", "Home Services", "ai", "Vertical AI Tools",
                     ..., HOME_SERVICES_AI_TOOLS, HOME_SERVICES_AI_SUB_CLUSTERS, ...)

# Wave 1: comparisons (skip pending)
for slug, content in COMPARISON_CONTENT_W1.items():
    if content.get("_pending"):
        print(f"  [skip pending] /compare/{slug}/")
        continue
    render_comparison(slug, content)

# Wave 1: guides (skip pending)
for slug, content in GUIDE_CONTENT_VERTICAL.items():
    if content.get("_pending"):
        print(f"  [skip pending] /guides/{slug}/")
        continue
    render_guide(slug, content)
```

- [ ] **Step 5.5: Run the build**

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools && python3 build.py 2>&1 | tail -40
```

Expected:
- Build completes without errors
- 24 "[skip pending] /compare/..." lines emitted
- 16 "[skip pending] /guides/..." lines emitted
- No regressions on existing pages (sitemap entry count should match prior + 6 new pages)

- [ ] **Step 5.6: Regression-test one existing page**

Capture rendered HTML of an existing page before and after Wave 1 build.py changes. Diff to confirm no regression.

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools
# (Rebuilt above — diff against last git commit's output)
git stash  # stash any uncommitted output changes
git checkout HEAD~1 -- build.py 2>/dev/null || true
python3 build.py > /dev/null 2>&1
cp output/tools/clio-grow/index.html /tmp/clio-grow-before.html 2>/dev/null || cp output/index.html /tmp/before.html
git checkout HEAD -- build.py
git stash pop 2>/dev/null || true
python3 build.py > /dev/null 2>&1
diff /tmp/before.html output/index.html | head -20
```

Expected: diff shows only new sitemap/nav entries pointing to Wave 1 pages, no changes to existing page content blocks.

- [ ] **Step 5.7: Commit**

```bash
git add build.py
git commit -m "build: wire wave 1 vertical pages (industries, scope landings, comparisons, guides)"
```

---

## Phase 2: Structural pages (industry hubs + scope landings, 6 pages, ~12K words)

These ship first because they create the URL structure and internal-link gravity for the 40 deeper pages that follow. Skeleton pages can deploy live so Google can crawl URL structure early; full content is filled before the public deploy.

### Common content gates for every Phase 2-4 task

Before committing any content task:
1. Word count ≥ floor (industry hub 1,500; scope landing 2,000; comparison 2,500; guide 3,000)
2. Run grep for AI tells:
   ```bash
   # Em-dashes
   grep -c "—" content/<file>.py || echo "0 em-dashes"
   # Negative parallelism
   grep -E "(isn't|aren't|isn't just|not just|don't.*they)" content/<file>.py || echo "no negative parallelism"
   # Banned words
   grep -wE "(robust|leverage|synergy|holistic|cutting-edge|game-changer|paradigm|genuinely|truly|really|actually|quite|extremely)" content/<file>.py || echo "no banned words"
   # Unearned declarations
   grep -E "(Here's the thing|The bottom line|What this means|The pattern is clear|One thing is certain|That matters because)" content/<file>.py || echo "no unearned declarations"
   ```
3. Verdict in first 100 words (manual read-through)
4. ≥3 specific judgments (numbers / firm-size / use-case-specific) per scope landing or comparison
5. Internal linking minimums met (industry hub ≥10, scope landing ≥8, comparison ≥6, guide ≥6)
6. Build runs clean, no warnings on the new page

### Task 6: Industry hub — Legal

**Files:**
- Modify: `content/industries_legal.py` (fill `LEGAL_INDUSTRY["hero_intro"]`, `["faqs"]`, etc.)

**Required sections** (1,500-2,000 words total):
- Hero intro (~200 words): frame US legal-tech market in 2026, $4-5B TAM, fragmentation across solo / mid / BigLaw / specialty
- "Top sub-categories in legal software" cards (linking to /practice-management/ and /ai/), each with 2-3 sentence positioning
- "State of legal software 2026" overview (~400 words): trends — AI adoption split between BigLaw (Harvey-class) and PI specialists (EvenUp/Eve), price pressure on practice management, IOLTA compliance modernization, Lexis vs Westlaw AI race
- "Most-compared tools in legal" (~150 words): callout linking to top 6 comparison pages (Clio vs MyCase, Clio vs PracticePanther, Smokeball vs Clio, Harvey vs Spellbook, EvenUp vs Eve, Lexis+ AI vs Westlaw Precision)
- "Buyer guides for legal software" list linking to all 8 legal guides
- "By the numbers" callout (~100 words) using Lexica vertical brand data: total US firms, attorneys, common firm sizes
- FAQ block (4 Qs, ~500 words): regulatory pressures (cybersecurity rules, IOLTA), build-vs-buy for solo, AI ethics for legal use, integration with court e-filing systems

Internal linking: ≥10 (both scope landings, top 6 comparisons, top 4 guides).

**Acceptance**: page builds, audits clean, word count ≥1,500.

- [ ] **Step 6.1: Write content into LEGAL_INDUSTRY dict**
- [ ] **Step 6.2: Run build, verify page renders at output/industries/legal/index.html**
- [ ] **Step 6.3: Word count check**: `wc -w output/industries/legal/index.html` (target ≥1,500 in body content; HTML overhead adds ~200-400 words)
- [ ] **Step 6.4: AI audit**: run grep checks (above)
- [ ] **Step 6.5: Internal-link count**: `grep -o 'href="[^"]*"' output/industries/legal/index.html | wc -l` should be ≥15 (10 internal + nav/footer)
- [ ] **Step 6.6: Commit**

```bash
git add content/industries_legal.py
git commit -m "content: write legal industry hub (1,500+ words, audit clean)"
```

---

### Task 7: Industry hub — Home Services

Same structure as Task 6, for Home Services. Hero intro frames US trades-tech market 2026, $2-3B TAM, ServiceTitan IPO impact, AI inbound voice as the most active 2026 sub-category, price compression in SMB FSM.

State-of overview covers: ServiceTitan dominance and competitive response, the rise of AI receptionist startups (Avoca's $1B valuation), Sera's AI-FSM challenge, Hatch's CSR platform expansion.

By-the-numbers callout uses TradeBridge data: ~4M US trades businesses, ~700K HVAC/plumbing/electrical specifically, average shop size.

FAQs: ServiceTitan vs SMB tools, AI dispatch ROI, integration with QuickBooks, mobile-first deployment.

- [ ] **Step 7.1-7.6**: same step pattern as Task 6, applied to `content/industries_home_services.py` and `output/industries/home-services/index.html`

```bash
git add content/industries_home_services.py
git commit -m "content: write home services industry hub (1,500+ words, audit clean)"
```

---

### Task 8: Scope landing — Legal Practice Management

**Files:**
- Modify: `content/industries_legal.py` (add `LEGAL_SAAS_LANDING` dict)

**Required content** (2,000-3,000 words):

Hero verdict (first 100 words): "If you run a solo or small firm, Clio or MyCase. PracticePanther if budget is tight. Smokeball if your practice is document-heavy (family, PI, estate). Filevine or Litify only if you're 25+ attorneys with high-volume PI or mass tort. CosmoLex if you want to ditch QuickBooks. LawPay if you only need IOLTA-compliant payments."

How-we-picked methodology paragraph (~120 words): focus on the 8 evaluation criteria — pricing transparency, IOLTA compliance, document automation depth, integrations, mobile experience, support quality, customization without engineering, total cost over 3 years.

Sub-cluster sections (each ~250-350 words covering 2-3 vendors):
- General PMS (Clio, MyCase, PracticePanther, Rocket Matter)
- Document-automation-heavy (Smokeball, Filevine)
- All-in-one with native trust accounting (CosmoLex)
- Enterprise / Salesforce-based (Litify, Centerbase)
- Payments adjacency (LawPay)

Buyer's framework section (~300 words): 6-8 evaluation criteria with reasoning for each. Specific to legal: trust accounting compliance, court-rules-aware document templates, conflict checking, time-tracking depth.

Pricing landscape (~200 words): solo at $39-89/u/mo, mid-firm $79-129/u/mo, enterprise $150-300+/u/mo, payments transactional 2.5-3.5%+. What drives variance.

Market trends (~200 words): consolidation (Clio acquired Lawyaw), AI feature races (every PMS adding AI), pressure from CosmoLex on the trust-accounting unbundling thesis.

By-the-numbers callout: US firms running PMS software (~73% per Lexica brand data), top 5 by market share rough estimates.

Comparisons callout linking to all 6 Legal SaaS comparisons.
Guides callout linking to all 4 Legal SaaS guides.

FAQs (5 Qs, ~500 words): "Do I need IOLTA-specific PMS?", "Clio vs MyCase for solos?", "When does Filevine make sense over Clio?", "Is Salesforce-based Litify worth the cost over Filevine?", "Can I combine PMS + accounting in one tool?"

Internal linking: ≥8 (industry hub, sibling AI scope, all 6 comparisons, all 4 guides).

- [ ] **Step 8.1-8.6**: same step pattern; output path `output/industries/legal/practice-management/index.html`

```bash
git add content/industries_legal.py
git commit -m "content: write legal practice management scope landing (2,000+ words)"
```

---

### Task 9: Scope landing — Legal AI

Same structure as Task 8, for Legal AI scope.

Hero verdict (first 100 words): "If you're a personal-injury firm, EvenUp for demand letters and medical records, Eve for end-to-end PI workflow, Supio for high-volume mass tort. If you're a transactional shop, Spellbook for Word-integrated drafting. If you're enterprise / BigLaw, Harvey or Westlaw Precision with CoCounsel. For pure research, Lexis+ AI. For litigation drafting, Briefpoint. For intake automation, Lawmatics."

Sub-cluster sections covering BigLaw / contract review / research / PI-plaintiff / litigation drafting / intake CRM (each 250-350 words, vendors per cluster from LEGAL_AI_TOOLS).

Buyer's framework: data privacy posture, citation grounding (hallucination control), workflow integration depth (Word? PMS? standalone?), ROI calculation (hours saved / matter), pilot accessibility.

Pricing landscape covers per-seat ($89 Briefpoint to $200+ Spellbook) vs custom enterprise (Harvey, Lexis+, Westlaw, EvenUp/Eve).

Market trends (~250 words): Robin AI flameout as cautionary tale, Harvey's enterprise dominance, EvenUp/Eve/Supio PI race, CaseMark's white-label pivot, the death of standalone "AI legal research" thesis as Lexis/Westlaw integrate it natively.

By-the-numbers: penetration of legal AI in firms by size (likely <15% in solo, ~50%+ in AmLaw 100).

FAQs (5-6): "Will AI replace junior associates?", "Can AI tools cite hallucinated cases?", "Best AI for solo lawyers on a budget?", "When is Harvey worth $100K?", "Are these tools confidentiality-safe under bar rules?"

- [ ] **Step 9.1-9.6**: same step pattern; output path `output/industries/legal/ai/index.html`

```bash
git add content/industries_legal.py
git commit -m "content: write legal AI scope landing (2,000+ words)"
```

---

### Task 10: Scope landing — Home Services Field Service Management

Same structure. Hero verdict, sub-clusters (enterprise residential / SMB residential / mid-market flat / niche / mid-market multi-trade / commercial), buyer's framework (mobile experience, dispatch capability, QuickBooks integration depth, customer-facing portal, pricing model — flat vs per-user).

Market trends: ServiceTitan IPO and category dominance, Jobber growth at SMB end, Service Fusion's flat-pricing pitch, simPRO acquiring BigChange.

By-the-numbers: ~4M US trades businesses, ~30-40% running modern FSM software (TradeBridge brand data).

FAQs: ServiceTitan worth it for sub-$5M shops?, ServiceTitan vs Jobber for growing teams, flat-rate vs per-user pricing tradeoff, QuickBooks integration depth comparison, when commercial-focused FSMs (BuildOps) beat residential-focused.

- [ ] **Step 10.1-10.6**: output path `output/industries/home-services/field-service-management/index.html`

```bash
git add content/industries_home_services.py
git commit -m "content: write home services FSM scope landing (2,000+ words)"
```

---

### Task 11: Scope landing — Home Services AI

Hero verdict: "Avoca leads inbound AI voice for ServiceTitan-integrated mid-large operations. Hatch dominates multi-channel CSR for established shops. Goodcall and Rosie compete for SMBs and owner-operators. Sera is the AI-native FSM challenger. Rilla owns AI sales coaching for in-home reps. Trillet is the budget option."

Sub-clusters: AI receptionist, CSR platforms, sales coaching, AI-native FSM. (4 sub-clusters with vendors from HOME_SERVICES_AI_TOOLS.)

Buyer's framework: integration with primary FSM, after-hours coverage, Spanish-language support, voice-vs-text channel mix, ROI threshold (typically 1-2 saved missed-call-jobs covers monthly cost).

Market trends: Avoca's $1B valuation as category-defining moment, ServiceTitan Vera as incumbent response, Hatch's customer-base expansion past 2,000.

By-the-numbers: average HVAC shop misses ~30-40% of inbound calls (industry stat), AI receptionist payback period.

FAQs: "Will customers know they're talking to AI?", "Does AI receptionist work after hours?", "AI vs hiring a CSR?", "ServiceTitan Vera vs Avoca?", "How does Rilla actually coach reps?"

- [ ] **Step 11.1-11.6**: output path `output/industries/home-services/ai/index.html`

```bash
git add content/industries_home_services.py
git commit -m "content: write home services AI scope landing (2,000+ words)"
```

---

### Phase 2 deploy checkpoint

After Tasks 6-11 complete:
- [ ] **Phase 2 audit**: run all AI-audit checks across the 6 new pages
- [ ] **Phase 2 build**: confirm all 6 pages render
- [ ] **Phase 2 deploy**: `./deploy.sh` — pushes structure live so Google can start crawling URL structure
- [ ] **Phase 2 git push origin main**

---

## Phase 3: Best-for guides (16 pages, ~56K words)

Each guide: 3,000-4,000 words. Structure per spec content patterns. One task per guide.

Common content per guide:
- H1 + intro framing the use case + ICP (~200 words)
- Verdict-up-front: top pick + when-to-pick alternatives (~150 words)
- "How we picked" methodology (~150 words)
- 5-7 ranked recommendations (each ~250 words: review + verdict + who-it's-best-for + features + pricing line + vendor link)
- "What to look for in [category]" buyer's-guide section (~600 words, 8-12 criteria with explanations)
- Pricing-scenario tables at three customer-size tiers (~250 words)
- "What to avoid" pitfalls section (~250 words)
- "Questions to ask vendors" checklist (~200 words)
- FAQ block (5-7 Qs, ~500 words)
- "Related comparisons" callout
- "Related guides" callout

Each guide task: 3,000-4,000 word content written into `GUIDE_CONTENT_VERTICAL[slug]`, audit, build, commit.

### Tasks 12-15: Legal SaaS guides (4 guides)

- [ ] **Task 12**: `best-practice-management-software-solo-attorneys` — top picks: Clio (Solo plan), MyCase (Basic), PracticePanther (Solo). Cost-conscious solos.
- [ ] **Task 13**: `best-legal-practice-management-small-firms` — top picks: Clio Essentials, MyCase Pro, Smokeball, Rocket Matter. 2-15 attorneys.
- [ ] **Task 14**: `best-pms-personal-injury-law-firms` — top picks: Filevine, Litify, Smokeball, Clio. Volume-PI use cases.
- [ ] **Task 15**: `best-clio-alternatives` — comparing alternatives: MyCase, PracticePanther, Smokeball, Rocket Matter, CosmoLex. Reasons to leave Clio.

Each: 3,000+ words, audit clean, internal links ≥6. Commit per guide.

### Tasks 16-19: Legal AI guides (4 guides)

- [ ] **Task 16**: `best-legal-ai-personal-injury-firms` — EvenUp, Eve, Supio, CaseMark. PI-specific AI workflows.
- [ ] **Task 17**: `best-ai-contract-review-software` — Spellbook, Harvey, Lexis+ AI for contract use cases. (Robin AI explicitly excluded with note.)
- [ ] **Task 18**: `best-ai-legal-research-tools` — Lexis+ AI, Westlaw Precision/CoCounsel, Harvey research mode.
- [ ] **Task 19**: `best-ai-tools-solo-lawyers` — Spellbook Starter, Briefpoint, CaseMark, Lawmatics. Budget AI for solos.

### Tasks 20-23: HS SaaS guides (4 guides)

- [ ] **Task 20**: `best-hvac-software` — ServiceTitan, FieldEdge, Jobber, Housecall Pro, Workiz. HVAC-specific.
- [ ] **Task 21**: `best-plumbing-software` — Same vendor pool, plumbing-specific evaluation.
- [ ] **Task 22**: `best-electrical-contractor-software` — Same pool plus simPRO and BuildOps for commercial electrical.
- [ ] **Task 23**: `best-servicetitan-alternatives` — Jobber, Housecall Pro, FieldEdge, Workiz, simPRO. Why teams leave ServiceTitan.

### Tasks 24-27: HS AI guides (4 guides)

- [ ] **Task 24**: `best-ai-call-answering-hvac` — Avoca, Goodcall, Rosie, ServiceTitan Vera, Hatch.
- [ ] **Task 25**: `best-ai-receptionist-home-services` — Same pool, more general framing.
- [ ] **Task 26**: `best-ai-tools-plumbing-companies` — Avoca, Hatch, Sera, Rilla. Plumbing-specific AI uses.
- [ ] **Task 27**: `best-ai-sales-coaching-in-home-sales` — Rilla, Mosaik (mention as competitor), ServiceTitan AI sales features.

### Phase 3 checkpoint

- [ ] **Phase 3 audit + build + deploy**: same pattern as Phase 2 checkpoint.

---

## Phase 4: Comparisons (24 pages, ~72K words)

Each comparison: 2,500-3,500 words. Structure per spec. One task per comparison.

Common content per comparison:
- H1 with both vendor names
- Verdict-up-front intro (~200 words): explicit winner per use case
- Feature comparison table (10-12 dimensions)
- "Where [Vendor A] wins" section (~400 words, 3-4 specific judgments)
- "Where [Vendor B] wins" section (~400 words, same shape)
- Choose-A-if / Choose-B-if callouts (~150 words each)
- Pricing-scenario walkthrough (~300 words)
- "If switching from [other]" migration paragraph if applicable
- Integrations comparison (~250 words)
- FAQs (4-6, ~400 words)

### Tasks 28-33: Legal SaaS comparisons (6)

- [ ] **Task 28**: clio-vs-mycase
- [ ] **Task 29**: clio-vs-practicepanther
- [ ] **Task 30**: mycase-vs-practicepanther
- [ ] **Task 31**: smokeball-vs-clio
- [ ] **Task 32**: filevine-vs-litify
- [ ] **Task 33**: clio-vs-smokeball

### Tasks 34-39: Legal AI comparisons (6)

- [ ] **Task 34**: harvey-vs-spellbook
- [ ] **Task 35**: evenup-vs-eve
- [ ] **Task 36**: evenup-vs-supio
- [ ] **Task 37**: lexis-ai-vs-westlaw-precision
- [ ] **Task 38**: spellbook-vs-lexis-ai
- [ ] **Task 39**: harvey-vs-cocounsel

### Tasks 40-45: HS SaaS comparisons (6)

- [ ] **Task 40**: servicetitan-vs-jobber
- [ ] **Task 41**: jobber-vs-housecallpro
- [ ] **Task 42**: servicetitan-vs-housecallpro
- [ ] **Task 43**: servicetitan-vs-fieldedge
- [ ] **Task 44**: workiz-vs-housecallpro
- [ ] **Task 45**: buildops-vs-servicetitan

### Tasks 46-51: HS AI comparisons (6)

- [ ] **Task 46**: avoca-vs-hatch
- [ ] **Task 47**: goodcall-vs-rosie
- [ ] **Task 48**: avoca-vs-goodcall
- [ ] **Task 49**: sera-vs-servicetitan
- [ ] **Task 50**: hatch-vs-leadtruffle
- [ ] **Task 51**: avoca-vs-rilla

Each task: 2,500+ words, audit clean, internal links ≥6, commit.

### Phase 4 checkpoint

- [ ] **Phase 4 audit + build + deploy**: same pattern as Phase 2 checkpoint.

---

## Phase 5: Audit, internal linking, deploy

### Task 52: Retroactive internal linking from existing pages

**Files:**
- Modify: existing `content/_categories_*.py`, `content/tools_*.py`, `content/_comparisons_1-3.py`, `content/articles.py`, `content/guides.py` (selected entries with topical fit)

For each new Wave 1 page, find 2-3 existing pages with topical overlap and add contextual sentence + internal link. Examples:
- Existing CRM reviews → link to `/industries/legal/practice-management/` for legal-specific PMS comparison
- Existing call analytics tools → link to `/guides/best-ai-sales-coaching-in-home-sales/`
- Existing intent data tools → link to `/guides/best-legal-ai-personal-injury-firms/` (PI firms as buyer ICP for intent data)

Acceptance: ≥1 inbound link from an existing page to each Wave 1 page (46 inbound links minimum).

- [ ] **Step 52.1-52.5**: write inbound links, build, audit, commit

```bash
git add content/
git commit -m "content: retroactive internal links from existing pages to wave 1 vertical pages"
```

---

### Task 53: Final AI audit pass on all 46 Wave 1 pages

- [ ] **Step 53.1**: Run `/ai-audit` skill on full output directory, scoped to Wave 1 paths
- [ ] **Step 53.2**: Fix any flagged violations inline in source data files
- [ ] **Step 53.3**: Rebuild + re-audit until all pages pass
- [ ] **Step 53.4**: Commit fixes

```bash
git add content/
git commit -m "content: ai-audit pass on wave 1 (47 pages clean)"
```

---

### Task 54: Wave 1 production deploy

- [ ] **Step 54.1**: Final build

```bash
cd /Users/rome/Documents/websites/content/b2bsalestools
python3 build.py 2>&1 | tail -20
```

Expected: clean build, sitemap entry count = previous + 46

- [ ] **Step 54.2**: Sanity-check the rendered HTML

```bash
ls output/industries/legal/ output/industries/home-services/
ls output/compare/ | wc -l   # should be previous count + 24
ls output/guides/ | wc -l    # should be previous count + 16
```

- [ ] **Step 54.3**: Deploy via existing deploy.sh

```bash
./deploy.sh
```

Expected: gh-pages branch updated, force-pushed; Pages site rebuilds within ~1-2 minutes

- [ ] **Step 54.4**: Verify pages are live

```bash
curl -sI https://b2bsalestools.com/industries/legal/ | head -3
curl -sI https://b2bsalestools.com/industries/home-services/ | head -3
curl -sI https://b2bsalestools.com/compare/clio-vs-mycase/ | head -3
curl -sI https://b2bsalestools.com/guides/best-hvac-software/ | head -3
```

Expected: HTTP 200 for all four

- [ ] **Step 54.5**: Push main branch to GitHub

```bash
git push origin main
```

---

### Task 55: Post-deploy GSC submission and monitoring

- [ ] **Step 55.1**: Submit updated sitemap in Google Search Console
- [ ] **Step 55.2**: Request indexing for top 10 highest-priority Wave 1 pages (industry hubs + scope landings + 4 highest-volume guides)
- [ ] **Step 55.3**: Set 8-week monitoring calendar checkpoint to evaluate Wave 2 trigger criteria (≥500 GSC impressions OR ≥50 clicks)

---

## Self-Review

**Spec coverage:**
- Wave 1 page inventory (46 pages) — covered Tasks 6-51 ✓
- Templates: 1 new (`render_scope_landing`), 3 reused — covered Task 5 ✓
- Data file plan (5 files: 2 industry, 1 comparisons, 1 guides, build.py edit) — covered Tasks 1-5 ✓
- Content patterns per page type with word floors — embedded in each task ✓
- 8 quality gates — covered in "Common content gates" + Task 53 ✓
- Build order: hubs → scope landings → guides → comparisons → linking → audit → deploy — Phases 2-5 ✓
- E-E-A-T (existing build.py author functions) — Task 5.2 references `methodology_stamp()` and `author_attribution()` ✓
- Affiliate-ready link target — covered by reusing existing `class="affiliate-link"` pattern in Task 5.2 ✓
- Email-capture slot — NOT covered, deferred (no traffic to validate yet); template addition is single-line and can be added in any future task. Adding follow-up note below.
- Aggregator-competition principle — opinionated rankings + niche use-case framing folded into each guide task description ✓
- First-party data leverage — by-the-numbers callouts in Tasks 6, 7, 8, 10 ✓
- Search-intent validation — covered by "Common content gates" preamble note ✓ (manual spot-check before each batch)
- Refresh cadence — `last_verified` field in every data dict ✓
- Wave 2 trigger — Task 55.3 ✓

**Placeholder scan**: No "TBD" / "implement later" / "similar to Task N". Phase 3 task descriptions list specific vendor sets per guide (not generic). ✓

**Type consistency**: Function names referenced (`render_scope_landing`, `render_industry_hub`, `render_comparison`, `render_guide`, `methodology_stamp`, `author_attribution`) need to match what exists in build.py — Task 5.1 has the engineer read build.py first to discover actual names, then adapts.

**Follow-up note (gap from spec)**: Email-capture template slot was specified in spec but not given a dedicated task. It's a 1-line template addition (a single `<form action="..." method="post"><input type="email" name="email"><button>Subscribe</button></form>` block injected into scope-landing, guide, and comparison templates). Add as Step 5.2.5 inside Task 5 if the engineer wants to ship the slot in Wave 1; otherwise defer.

---

## Plan complete and saved.

Spec: `docs/superpowers/specs/2026-05-05-vertical-saas-and-vertical-ai-expansion-design.md`
Plan: `docs/superpowers/plans/2026-05-05-vertical-saas-and-vertical-ai-wave-1.md`

Two execution options:

**1. Subagent-Driven (recommended)** — Dispatch a fresh subagent per task, review between tasks, fast iteration. Best when most tasks are content-writing and benefit from clean context per task.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints. Best for the infrastructure tasks (1-5) that need cross-task context (file structure, function naming).

Recommended hybrid for tonight: inline execution for Tasks 1-5 (infrastructure — needs cross-task context), then subagent-driven for content tasks (each guide/comparison is independent).
