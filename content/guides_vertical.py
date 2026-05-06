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


# =============================================================================
# Legal SaaS guides
# =============================================================================

GUIDE_CONTENT_VERTICAL["best-practice-management-software-solo-attorneys"] = {
    "category": "legal-saas",
    "title": "Best Practice Management Software for Solo Attorneys",
    "last_verified": "2026-05-05",
    "intro": (
        "Solo attorneys face a different software calculation than larger firms. You are the practice, "
        "the bookkeeper, the marketer, the IT department, and the rainmaker. The right practice "
        "management software has to handle every workflow without requiring a dedicated admin to set "
        "it up or maintain it. Pricing matters more at this end of the market because there is no "
        "scale from spreading the cost across multiple attorneys. And IOLTA compliance is non-"
        "negotiable: the bar grievance risk of mishandled trust accounts is the same whether you are "
        "a solo or a 500-attorney firm.\n\n"
        "This guide covers the practice management platforms that work well for solo practitioners "
        "in 2026, with specific pricing and feature comparisons for the solo use case. We exclude "
        "enterprise-only platforms (Litify, Centerbase) because their pricing and complexity do not "
        "fit a solo budget. We include payment-only adjacencies (LawPay) because solos often run them "
        "alongside a basic PMS rather than buying a full all-in-one."
    ),
    "verdict": (
        "Top pick: **Clio EasyStart** ($49/u/mo) for general-practice solos who want the broadest "
        "integration ecosystem. **MyCase Basic** ($39/u/mo) is the cheapest credible option with strong "
        "intake automation. **PracticePanther Solo** ($59/u/mo) is the value pick if you want stronger "
        "automation without paying Clio's tier prices. **Smokeball** if your practice is document-"
        "template-heavy (family, estate, immigration). **CosmoLex** at $89/u/mo if you want to drop "
        "QuickBooks and run trust accounting natively."
    ),
    "methodology": (
        "We evaluated each platform against solo-specific criteria: total monthly cost at a single seat, "
        "implementation time without a dedicated admin, IOLTA compliance depth, mobile experience for an "
        "attorney working out of court and from home, and the ability to grow with the practice without "
        "an expensive migration if you add a second attorney. Pricing is verified against vendor sites "
        "as of 2026-05-05."
    ),
    "recommendations": [
        {
            "slug": "clio", "rank": "1.",
            "review": (
                "Clio EasyStart at $49 per user per month is the most-balanced solo option. The "
                "integration ecosystem (250+ partners) means you can wire in calendar, email, "
                "accounting, e-filing, and payment processing without compromise. Clio Draft (the "
                "rebranded Lawyaw acquisition) closed the document automation gap that used to be "
                "Smokeball's distinguishing feature. Mobile experience is solid. IOLTA compliance "
                "through the integrated Clio Payments product handles trust routing without manual "
                "intervention.\n\n"
                "The two weak points: EasyStart caps document storage at 100GB and excludes some "
                "advanced reporting features that show up at the Essentials tier ($89/u/mo). For a "
                "general-practice solo doing standard work, those limits do not bite. If you are doing "
                "high-volume document work or want firm-level reporting, you upgrade tiers fast."
            ),
        },
        {
            "slug": "mycase", "rank": "2.",
            "review": (
                "MyCase Basic at $39 per user per month is the cheapest credible PMS for solos. The "
                "intake automation and client portal are stronger than Clio EasyStart at this price "
                "point. MyCase Payments handles IOLTA-compliant trust routing with proper three-way "
                "reconciliation. Mobile app is comparable to Clio.\n\n"
                "Trade-offs: integration ecosystem is narrower than Clio (around 100 partners versus "
                "250+), document automation is weaker (no built-in template builder at Basic tier), "
                "and the Pro upgrade ($79/u/mo) is more expensive than Clio Essentials at $89. For "
                "solos who care about price first and intake flow second, MyCase wins."
            ),
        },
        {
            "slug": "practicepanther", "rank": "3.",
            "review": (
                "PracticePanther Solo at $59 per user per month sits between Clio EasyStart and "
                "MyCase Basic on price but with stronger workflow automation than either. The "
                "automation engine (workflow rules, document automation, client portal) is the most "
                "developed at this price tier. IOLTA compliance is solid.\n\n"
                "Where PracticePanther loses ground: the UI is older-feeling than Clio or MyCase, "
                "the mobile app is the weakest of the three, and the integration ecosystem is "
                "smaller. If you spend most of your time at a desk and care about automation power, "
                "PracticePanther beats both Clio and MyCase. If you want a polished mobile experience "
                "or work in court a lot, the others fit better."
            ),
        },
        {
            "slug": "smokeball", "rank": "4.",
            "review": (
                "Smokeball is the document-heavy specialist. Pricing for solos is contact-sales but "
                "lands around $69-$99/u/mo in the lower tiers. The standout feature is auto-time-"
                "capture: Smokeball records billable time spent in Word and Outlook on a matter "
                "automatically, eliminating the time-leakage problem most solos have. For family "
                "law, estate planning, immigration, and certain PI workflows, Smokeball's template "
                "library is deeper than Clio Draft.\n\n"
                "Trade-off: the platform is heaviest of the bunch and assumes Word + Outlook usage "
                "patterns. Solos who run on Google Workspace or who do mostly litigation work get "
                "less benefit from the platform."
            ),
        },
        {
            "slug": "cosmolex", "rank": "5.",
            "review": (
                "CosmoLex at $89 per user per month is the all-in-one trust-accounting pick. It "
                "includes a full general ledger, IOLTA-compliant trust accounting, and PMS in one "
                "platform, eliminating the need for QuickBooks. For solos who currently maintain a "
                "PMS plus QuickBooks plus a separate trust ledger and find the three-way "
                "reconciliation painful, CosmoLex collapses the stack.\n\n"
                "It is overbuilt for solos who do not handle large trust transactions and is more "
                "expensive than Clio EasyStart, MyCase Basic, or PracticePanther Solo. Pick CosmoLex "
                "specifically because of the accounting integration, not as a general-purpose PMS."
            ),
        },
        {
            "slug": "lawpay", "rank": "6.",
            "review": (
                "LawPay is not a PMS but a payments adjacency worth covering for solos. It runs "
                "IOLTA-compliant card payments at ~2.95% + $0.20 per transaction with proper trust "
                "routing. Most solos using a basic PMS (or even running on QuickBooks plus paper) "
                "layer LawPay on top to accept card payments without bar-grievance risk.\n\n"
                "If you want IOLTA-compliant payment processing and your existing PMS handles "
                "everything else, LawPay is the cleanest answer. If you want a single platform doing "
                "PMS plus payments plus trust accounting, CosmoLex covers all of that."
            ),
        },
    ],
    "what_to_look_for": (
        "Eight criteria matter when picking PMS as a solo attorney.\n\n"
        "**Total monthly cost.** At one seat, cost matters more than any feature comparison. Tier "
        "carefully: EasyStart, Basic, or Solo plans cover most solo workflows; the upgrade tiers "
        "double or triple cost without adding features most solos use.\n\n"
        "**IOLTA compliance depth.** Three-way reconciliation, automatic trust routing on payments, "
        "state-bar-specific report generation. Manual workarounds compound bar-grievance risk and "
        "consume hours of monthly bookkeeping time.\n\n"
        "**Implementation time without a dedicated admin.** You will be the admin. Look for platforms "
        "that ship with sensible defaults, video tutorials, and intake setup wizards. Clio, MyCase, "
        "and PracticePanther all clear this bar; CosmoLex requires more setup work because of the "
        "accounting integration.\n\n"
        "**Mobile experience.** Court appearances, client meetings, depositions: you need the PMS to "
        "work on a phone. Clio and MyCase have polished mobile apps. PracticePanther mobile is "
        "functional but feels older. Smokeball and CosmoLex are weaker on mobile.\n\n"
        "**Document automation.** Template logic, court-rules-aware drafts, automatic merge from "
        "matter data. Smokeball is strongest. Clio Draft (post-Lawyaw acquisition) is a credible "
        "second. PracticePanther has solid automation. MyCase document automation requires the Pro "
        "tier upgrade.\n\n"
        "**Time tracking model.** Manual entry, timer-based, or auto-capture? Smokeball auto-captures "
        "from Word and Outlook. Most others require manual or timer entry. For solos billing hourly, "
        "auto-capture eliminates 10-25% time leakage that compounds over a year.\n\n"
        "**Integration ecosystem.** Calendar (Google or Outlook), accounting (QuickBooks or native), "
        "e-filing, payments. Clio leads on raw count. The integrations a solo needs are smaller: "
        "calendar plus payments plus accounting cover 80% of solo use cases.\n\n"
        "**Growth path.** If you add a second attorney or paralegal in 18 months, will the platform "
        "scale without a painful migration? Clio, MyCase, and PracticePanther all have higher tiers "
        "that scale. CosmoLex is fixed-price per user. Smokeball custom-quotes."
    ),
    "pricing_scenarios": (
        "**Solo with low document volume:** Clio EasyStart at $49 or MyCase Basic at $39 per month. "
        "All-in first-year cost including bar-association payment processing through the integrated "
        "vendor: $700-$1,000.\n\n"
        "**Solo with heavy document templates (family, estate, immigration):** Smokeball at "
        "$69-$99/u/mo or Clio Essentials with Clio Draft at $89/u/mo. All-in first year: "
        "$1,000-$1,500.\n\n"
        "**Solo handling significant trust transactions (real estate, PI, retainer-heavy litigation):** "
        "CosmoLex at $89/u/mo. All-in first year including bookkeeper time to migrate: $1,500-$3,000."
    ),
    "what_to_avoid": (
        "**Free or near-free PMS without IOLTA compliance.** Bar grievance risk eats any cost savings. "
        "If a tool cannot articulate three-way reconciliation and proper trust routing, do not use it "
        "for client funds.\n\n"
        "**Enterprise-tier PMS (Litify, Centerbase, large Filevine deployments).** Pricing assumes 25+ "
        "attorneys. Solo budget will not work and the implementation overhead is a waste of time.\n\n"
        "**Generic small business CRM (HubSpot, Salesforce Starter).** They cover contact management "
        "but lack IOLTA compliance, court-rules awareness, and legal-specific document automation. The "
        "duct tape required to make them work for legal practice is not worth the savings.\n\n"
        "**Promised AI features that do not yet exist.** Several PMS platforms market AI capabilities "
        "that are pre-release or limited beta. Buy based on shipping features, not roadmap promises."
    ),
    "questions_to_ask": [
        "What is the total monthly cost at one user, including required add-ons for IOLTA compliance and document storage?",
        "Does the platform support three-way IOLTA reconciliation, and can it generate the report my state bar requires without manual export?",
        "How does trust-applicable payment routing work? Is it automatic or manual on every transaction?",
        "What is the document automation capability at the tier I am buying? Are templates included or are they an add-on?",
        "Does time tracking auto-capture from Word and Outlook, or do I need to manually log entries?",
        "What is the mobile app like in the field? Can I do everything I do on desktop?",
        "What is the upgrade path if I add a second attorney or paralegal in 12-18 months?",
        "What is the data export and migration story if I switch platforms?",
        "Are there bar-association discounts available through ABA, state, or local bar memberships?",
        "What does customer support look like at this tier, and what is the response time SLA?",
    ],
    "faqs": [
        {
            "question": "Can I start on a free or trial PMS and upgrade later?",
            "answer": (
                "Most platforms offer 7-30 day free trials, not free tiers. Clio, MyCase, "
                "PracticePanther, Smokeball, and CosmoLex all run trials. The trials are useful for "
                "validating workflow fit before committing. Plan to spend 3-5 hours during the trial "
                "configuring the platform with realistic data so the evaluation is meaningful. After "
                "the trial, expect to commit at least monthly; annual plans usually save 10-20% if "
                "the platform is the right fit."
            ),
        },
        {
            "question": "What if I switch PMS platforms after a year?",
            "answer": (
                "Switching costs are real. Plan for 40-80 hours of admin time to migrate matters, "
                "contacts, time entries, billing history, and trust accounting records. Most platforms "
                "have data export capabilities (CSV, sometimes API) but not all of the data structure "
                "translates cleanly. Pick a platform you can stay on for at least 2-3 years to amortize "
                "the migration cost. Most solos who switch do so within the first 6 months when the "
                "data is still light, not after a year of accumulated history."
            ),
        },
        {
            "question": "Do I need both PMS and QuickBooks?",
            "answer": (
                "Most solos run both: PMS for matter management, time tracking, billing, and trust "
                "accounting; QuickBooks for general-ledger accounting (operating account, payroll if "
                "applicable, tax preparation). The exception is CosmoLex, which includes full general "
                "ledger and eliminates QuickBooks. For solos doing simple tax returns and not running "
                "payroll, CosmoLex is sufficient. For solos with more complex accounting needs, the "
                "PMS-plus-QuickBooks model still wins."
            ),
        },
        {
            "question": "How much should a solo budget for legal software in year one?",
            "answer": (
                "Plan for $1,000-$3,000 in year one for PMS plus payment processing plus essential "
                "integrations. The lower end of that range is achievable with MyCase Basic or Clio "
                "EasyStart plus standard payment processing. The upper end includes Smokeball or "
                "CosmoLex with deeper feature sets. Bar-association discounts can save 10-20% on "
                "several platforms. Adding e-filing, document storage, or specialized add-ons "
                "(Lawmatics for intake, Spellbook for AI drafting) can add another $500-$2,000 "
                "annually depending on practice mix."
            ),
        },
        {
            "question": "Is Clio worth more than MyCase for a solo?",
            "answer": (
                "Often yes, narrowly. The $10/month price difference between EasyStart ($49) and "
                "MyCase Basic ($39) buys you a meaningfully larger integration ecosystem (250+ vs "
                "~100), Clio Draft document automation, and a polish in the product experience that "
                "matters when you spend hours per day in the platform. If your top priority is intake "
                "automation specifically, MyCase wins. If you value general flexibility, Clio's slight "
                "premium is justified for most solos."
            ),
        },
    ],
    "related_comparisons": [
        ("/compare/clio-vs-mycase/", "Clio vs MyCase"),
        ("/compare/clio-vs-practicepanther/", "Clio vs PracticePanther"),
        ("/compare/mycase-vs-practicepanther/", "MyCase vs PracticePanther"),
        ("/compare/smokeball-vs-clio/", "Smokeball vs Clio"),
    ],
    "related_guides": [
        ("/guides/best-legal-practice-management-small-firms/", "Best PMS for Small Law Firms"),
        ("/guides/best-clio-alternatives/", "Best Clio Alternatives"),
        ("/guides/best-ai-tools-solo-lawyers/", "Best AI Tools for Solo Lawyers"),
    ],
}
