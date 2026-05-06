"""Legal vertical: SaaS and AI tools for law firms.

Covers two scopes:
  - Practice management software (Clio, MyCase, etc.)
  - Vertical AI tools for legal (Harvey, Spellbook, EvenUp, etc.)
"""

LEGAL_INDUSTRY = {
    "slug": "legal",
    "name": "Legal",
    "scopes": ["practice-management", "ai"],
    "last_verified": "2026-05-05",

    "hero_intro": (
        "The US legal software market hit $4.8 billion in 2025 and keeps fragmenting along firm size and practice specialty. "
        "A solo immigration attorney runs nothing like a 200-attorney PI firm, and the software market reflects that reality. "
        "There are roughly 450,000 law firms in the US and at least 35 distinct vendors competing for them, organized into a "
        "half-dozen overlapping categories.\n\n"
        "Two shifts are reshaping the landscape this year. First, AI: Harvey raised at a $5 billion valuation and locked down "
        "most of the AmLaw 100, while a separate cluster of plaintiff-focused tools (EvenUp, Eve, Supio) racks up wins in "
        "personal injury. Lexis and Thomson Reuters are racing to bake AI into their research products before independent "
        "vendors can take market share. Second, the practice management category Clio dominated for a decade is fragmenting: "
        "CosmoLex pitches all-in-one with native trust accounting, Smokeball doubles down on document automation, Filevine and "
        "Litify own enterprise PI, and a wave of vertical AI tools is eating the workflow Clio used to own.\n\n"
        "If you are picking software for a US firm in 2026, three things shape the decision: firm size, practice area, and "
        "how aggressive you want to be on AI. This page walks through each."
    ),

    "saas_card_blurb": "Cloud practice management for solo through enterprise firms. Clio, MyCase, PracticePanther, Smokeball, Filevine, and seven more compared.",
    "ai_card_blurb": "AI-native legal tools for research, drafting, intake, and PI workflows. Harvey, Spellbook, EvenUp, Eve, Lexis+ AI, and others compared.",
    "index_card_blurb": "Practice management plus AI tool reviews for US law firms across solo, small, mid, and BigLaw segments.",

    "state_of_overview": (
        "Three patterns dominate legal software in 2026.\n\n"
        "AI is splitting the market by firm size, not by feature. BigLaw buys Harvey or Westlaw Precision with CoCounsel because "
        "they need broad capability across research, drafting, and due diligence with enterprise procurement comfort. Personal "
        "injury firms buy EvenUp, Eve, or Supio because demand letters and medical record review are the workflow bottleneck "
        "and these tools were built around it. Solo and small-firm attorneys buy Spellbook for contract drafting or Briefpoint "
        "for litigation responses, where the ROI per matter is obvious. The middle of the market (mid-size general practice) is "
        "the most contested zone, with Spellbook, Lexis+ AI, Westlaw Precision, and a handful of practice-area-specific tools "
        "all competing for the same buyers.\n\n"
        "Practice management is unbundling. Clio still leads on overall market share and integration depth, but specific "
        "weaknesses are pulling firms to specialists. CosmoLex has eaten share from firms that wanted to drop QuickBooks. "
        "Smokeball pulls firms with high document-template volume (family law, estate planning, certain PI shops). Filevine "
        "and Litify took most of the high-volume PI category, where Clio's general-purpose model never fit. The pricing wars "
        "at the bottom of the market (PracticePanther at $59/u/mo, MyCase at $39/u/mo Basic) are squeezing Clio's EasyStart "
        "tier hard.\n\n"
        "Trust accounting compliance is going through its biggest modernization in 20 years. State bars in California, Texas, "
        "Florida, and Illinois have all updated IOLTA reporting requirements between 2024 and 2026. The firms that built their "
        "stack on QuickBooks plus a separate trust ledger are finding compliance painful, which is why CosmoLex's all-in-one "
        "thesis keeps gaining traction. LawPay's IOLTA-compliant payments product moved from a nice-to-have to a buying criterion "
        "in roughly the same window.\n\n"
        "The Lexis-versus-Westlaw AI race is the highest-stakes incumbent battle in legal tech. Both products started shipping AI "
        "research add-ons in 2023 and have been improving them on roughly six-month cycles. Whichever side ends up with the "
        "more reliable citation grounding (and fewer hallucination incidents) will carry forward a 30-year customer-base lead "
        "into the AI era. As of mid-2026, the products are close enough that most firms pick based on which research platform "
        "they were already on, not which AI is better. That stickiness is exactly what Lexis and Westlaw were defending."
    ),

    "by_the_numbers": [
        {"number": "~450,000", "label": "active law firms in the US (Lexica brand data, 2025)"},
        {"number": "~1.3 million", "label": "active US attorneys (ABA, 2025)"},
        {"number": "74%", "label": "of US law firms are solo (one attorney). Most are underserved by enterprise software."},
        {"number": "~200", "label": "AmLaw 200 firms account for the bulk of legal AI enterprise spend"},
        {"number": "$4.8B", "label": "US legal software market size, 2025"},
    ],

    "most_compared": [
        ("/compare/clio-vs-mycase/", "Clio vs MyCase"),
        ("/compare/clio-vs-practicepanther/", "Clio vs PracticePanther"),
        ("/compare/smokeball-vs-clio/", "Smokeball vs Clio"),
        ("/compare/harvey-vs-spellbook/", "Harvey vs Spellbook"),
        ("/compare/evenup-vs-eve/", "EvenUp vs Eve"),
        ("/compare/lexis-ai-vs-westlaw-precision/", "Lexis+ AI vs Westlaw Precision"),
    ],

    "buyer_guides": [
        ("/guides/best-practice-management-software-solo-attorneys/", "Best Practice Management Software for Solo Attorneys"),
        ("/guides/best-legal-practice-management-small-firms/", "Best Legal Practice Management for Small Law Firms"),
        ("/guides/best-pms-personal-injury-law-firms/", "Best PMS for Personal Injury Firms"),
        ("/guides/best-clio-alternatives/", "Best Clio Alternatives"),
        ("/guides/best-legal-ai-personal-injury-firms/", "Best Legal AI for Personal Injury Firms"),
        ("/guides/best-ai-contract-review-software/", "Best AI Contract Review Software"),
        ("/guides/best-ai-legal-research-tools/", "Best AI Legal Research Tools"),
        ("/guides/best-ai-tools-solo-lawyers/", "Best AI Tools for Solo Lawyers"),
    ],

    "faqs": [
        {
            "question": "What is the best practice management software for a US law firm in 2026?",
            "answer": (
                "There is no universal winner. For solo attorneys, Clio EasyStart or MyCase Basic. For small firms (2-15 attorneys) "
                "general practice, Clio Essentials, MyCase Pro, or PracticePanther Essential. For document-heavy practices "
                "(family, estate, certain PI), Smokeball. For mid-firm general practice that wants to ditch QuickBooks, CosmoLex. "
                "For high-volume PI or mass tort (25+ attorneys), Filevine or Litify. The pick that matters less than people "
                "expect is general-purpose PMS within the same tier. Clio versus MyCase versus PracticePanther come down to "
                "preference, integration ecosystem, and whether you have time to migrate."
            ),
        },
        {
            "question": "Should my firm buy AI legal tools in 2026?",
            "answer": (
                "If you do contract drafting, contract review, demand letters, medical record summary, or high-volume discovery "
                "responses, yes. ROI is obvious in those workflows and pilot programs typically pay back within a quarter. If "
                "you do general practice with low-document-volume work, the case is weaker and most tools are still expensive "
                "or rough at the edges. The exception is research: if you already pay for Lexis or Westlaw, the AI add-ons are "
                "worth the extra cost for the time savings on case search and brief drafting."
            ),
        },
        {
            "question": "Are AI legal tools safe to use under bar ethics rules?",
            "answer": (
                "Yes, with diligence. The Florida Bar, California Bar, ABA, and others have published guidance on competent AI "
                "use that boils down to: do not rely on AI output without verification, protect client confidentiality (which "
                "means understanding where the tool processes data), supervise AI work product the same way you would supervise "
                "a paralegal, and bill for AI-assisted work at the lawyer rate, not the AI cost. Tools designed for legal use "
                "(Harvey, Spellbook, Lexis+ AI, Westlaw Precision) all publish privacy and data-handling documentation. Generic "
                "consumer AI tools (free ChatGPT, etc.) are riskier and several state bars have warned against using them for "
                "client matters."
            ),
        },
        {
            "question": "How do I evaluate IOLTA-compliant trust accounting in PMS?",
            "answer": (
                "Three things matter. First, can the system enforce three-way reconciliation (book balance, bank balance, client "
                "ledger sum) automatically and flag discrepancies? Second, does it generate the IOLTA reports your state bar "
                "requires without manual export-and-format work? Third, when you process client payments, does the platform "
                "route trust-applicable funds to the IOLTA account and operating funds to the operating account without manual "
                "intervention? CosmoLex, LawPay, and Smokeball all do this natively. Clio and MyCase do it well with their "
                "respective payments integrations. PracticePanther and Rocket Matter handle it but with more manual setup. If "
                "your firm has been bouncing between QuickBooks and a separate trust ledger, an all-in-one tool is worth the "
                "migration pain."
            ),
        },
    ],
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
     "Custom quotes; Standard / Premium / a la carte",
     "Customizable case management for high-volume PI and complex litigation.",
     "PI firms with 10+ attorneys and mass-tort practices"),
    ("cosmolex", "CosmoLex", "https://www.cosmolex.com", "all-in-one",
     "$89 per user/month flat",
     "All-in-one PMS with native IOLTA-compliant trust accounting and full general ledger.",
     "Firms that want PMS plus accounting in one tool, no QuickBooks dependency"),
    ("rocketmatter", "Rocket Matter", "https://www.rocketmatter.com", "general-pms",
     "$49 Essentials, $79 Pro, $99 Premier per user/month",
     "Cloud PMS plus billing for small/mid firms with the ProfitFuel module.",
     "Small/mid firms (5-50 attorneys) focused on profitability metrics"),
    ("centerbase", "Centerbase", "https://www.centerbase.com", "enterprise",
     "Custom enterprise pricing (~$80-130 per user/month equivalents)",
     "Customizable PMS for growing mid-size firms with workflow and billing engine.",
     "Mid-size firms (20-100 attorneys) outgrowing Clio"),
    ("litify", "Litify", "https://www.litify.com", "enterprise-pi",
     "Custom enterprise; typically $150-300+ per user/month",
     "Salesforce-native legal ops platform for high-volume PI and mass tort.",
     "Large PI firms (50+ attorneys), mass-tort, multi-state"),
    ("lawpay", "LawPay", "https://www.lawpay.com", "payments",
     "~2.95% plus $0.20 per transaction; tiered monthly fees",
     "Legal-specific payments platform with IOLTA compliance.",
     "Firms accepting card payments that need IOLTA-compliant trust handling"),
]

LEGAL_SAAS_SUB_CLUSTERS = {
    "general-pms": "General practice management. Full workflow for solo through mid-firm general practice.",
    "doc-automation": "Document-automation-heavy PMS. Built around template-driven document generation.",
    "all-in-one": "All-in-one with native trust accounting. Eliminates the need for separate accounting software.",
    "enterprise": "Enterprise customizable PMS. For mid-size firms with complex requirements.",
    "enterprise-pi": "Enterprise PI and mass tort. High-volume case management with PI-specific features.",
    "payments": "Payments adjacency. IOLTA-compliant payment processing.",
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
     "AI demand letters, medical chronologies, and settlement docs for PI firms.",
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
    ("lexis-ai", "Lexis+ AI", "https://www.lexisnexis.com/en-us/products/lexis-plus-ai.page", "research",
     "Add-on to Lexis subscriptions; contact sales",
     "Conversational legal research grounded in the Lexis precedent corpus.",
     "Existing Lexis customers; firms requiring authoritative citation grounding"),
    ("westlaw-precision", "Westlaw Precision with CoCounsel", "https://www.thomsonreuters.com/en/products/westlaw-precision.html", "research",
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
    "biglaw": "General-purpose BigLaw AI. Broad capability across research, drafting, and due diligence.",
    "contract-review": "Contract drafting and review. Word-integrated AI for transactional work.",
    "research": "AI legal research. Natural-language queries grounded in case law.",
    "pi-plaintiff": "PI / plaintiff-specific. Demand letters, medical record review, intake-to-settlement.",
    "litigation-drafting": "Litigation drafting and discovery. Motions, objections, responses, summaries.",
    "intake-crm": "Intake and CRM AI. Lead scoring, intake automation, marketing analytics.",
}

LEGAL_SAAS_LANDING = {
    "hero_verdict": (
        "If you run a solo or small firm general practice, Clio or MyCase. PracticePanther if budget is tight. "
        "Smokeball if your practice is document-heavy (family, PI, estate). Filevine or Litify if you are a 25+ "
        "attorney high-volume PI or mass tort firm. CosmoLex if you want to drop QuickBooks and run trust accounting "
        "natively. Rocket Matter if you obsess about firm-level profitability metrics. Centerbase if you have "
        "outgrown Clio but Salesforce-based Litify is overkill. LawPay if you only need IOLTA-compliant payments "
        "as a layer on top of your existing PMS.\n\n"
        "The choice that matters less than people expect: general PMS within the same tier. Clio versus MyCase "
        "versus PracticePanther come down to integration ecosystem preferences and migration cost more than "
        "feature differentiation. Pick once, set up properly, do not relitigate."
    ),

    "methodology": (
        "We evaluated each platform on eight criteria. Pricing transparency (is the rate card public? are tiers "
        "honest?). IOLTA compliance depth (three-way reconciliation? state-bar-specific reports? automatic trust "
        "fund routing on payments?). Document automation (template power, conditional logic, court-rules-aware "
        "drafts). Integration ecosystem (CRM, accounting, e-filing, payments, court systems). Mobile experience "
        "(does it work for an attorney in the field, or is it desktop-only with a phone shim?). Support quality "
        "and self-service learning. Customization without engineering (can a non-technical admin configure custom "
        "fields, automations, intake forms?). Total cost over three years including implementation, training, "
        "and add-ons. Pricing data verified against vendor sites and recent customer reports as of 2026-05-05."
    ),

    "cluster_intros": {
        "general-pms": (
            "General-practice PMS is the largest sub-category and the most contested. Clio, MyCase, PracticePanther, "
            "and Rocket Matter all serve solo through mid-firm general practice with broadly similar feature sets. "
            "The differences are in tier pricing (PracticePanther and Rocket Matter run cheaper), integration "
            "breadth (Clio leads with 250+ partners), intake automation (MyCase is strongest), and overall ecosystem "
            "stickiness (Clio's lawyer-marketplace and accounting partners create switching costs)."
        ),
        "doc-automation": (
            "Document-automation-heavy PMS makes sense when your practice generates more documents than legal work. "
            "Family law, estate planning, certain PI workflows, and immigration all fit this profile. Smokeball's "
            "auto-time-capture (which records time spent in Word and Outlook on a matter) is the standout feature "
            "here, and it eliminates a chunk of the time-tracking gap most firms have. Filevine sits between this "
            "category and enterprise PI, with stronger document automation than Clio and stronger case management "
            "than Smokeball."
        ),
        "all-in-one": (
            "All-in-one PMS with native trust accounting is the answer for firms that want to drop QuickBooks. "
            "CosmoLex is the only platform in this category at scale. The pitch lands hardest with firms that have "
            "been double-keying transactions between PMS and QuickBooks, or struggling with three-way reconciliation. "
            "Migration is real work (typically 4-8 weeks of bookkeeper time) but the long-term operational simplification "
            "is the trade."
        ),
        "enterprise": (
            "Enterprise PMS for mid-size firms outgrowing Clio. Centerbase is the cleanest option for firms that "
            "want enterprise-grade workflow, billing, and reporting without going to Salesforce-based Litify. The "
            "common buyer here is a 30-100 attorney firm with multiple practice areas, complex billing arrangements, "
            "and a dedicated ops or finance person who can run the platform."
        ),
        "enterprise-pi": (
            "Enterprise PI and mass tort is its own world. The volume math is different: a firm running 5,000 PI "
            "matters needs intake-to-settlement automation that general PMS was not built for. Filevine and Litify "
            "split the market, with Filevine winning more on usability and Litify winning on Salesforce-ecosystem "
            "fit and enterprise procurement comfort. Pricing is custom and typically lands 2-5x what general PMS costs."
        ),
        "payments": (
            "Payments adjacency is the LawPay-shaped hole in the legal stack. Most full-featured PMS platforms have "
            "payment processing, but if you only need IOLTA-compliant card payments and your firm is happy on its "
            "current PMS or even on QuickBooks plus a separate trust ledger, LawPay layers on top without forcing "
            "a PMS migration. It is also the integration backbone for Clio, MyCase, PracticePanther, and most other "
            "legal payment flows."
        ),
    },

    "buyer_framework": (
        "Six criteria matter more than the others when evaluating PMS for a US law firm.\n\n"
        "Trust accounting depth. If you handle client funds, your PMS or its accounting integration must enforce "
        "three-way reconciliation, generate IOLTA reports your state bar accepts without manual reformatting, and "
        "route trust-applicable payments to the IOLTA account automatically. Manual workarounds compound bar-grievance "
        "risk and add hours of monthly bookkeeping work.\n\n"
        "Integration ecosystem. PMS lives at the center of your stack. Calendar (Google or Outlook), email, accounting "
        "(QuickBooks or native), payments, e-filing (state-court-specific), CRM-style intake, and document storage "
        "(Box, OneDrive, NetDocuments) all need to work cleanly. Clio leads on raw count of integrations; Smokeball "
        "and Filevine are deeper on Word and Outlook specifically.\n\n"
        "Document automation. Templates with conditional logic, court-rules-aware drafts (where venue-specific rules "
        "are baked in), automatic merge from matter data, and reusable clause libraries. Smokeball is strongest. "
        "Clio Draft (the rebranded Lawyaw acquisition) closed much of the gap. Other vendors lag and most firms "
        "supplement with NetDocuments, HotDocs, or Spellbook.\n\n"
        "Time tracking model. Manual entry, timer-based, or auto-capture? Smokeball's auto-capture is unique. "
        "Most other vendors offer timers and manual entry, which means time leakage in the 10-25% range for typical "
        "firms. If your firm bills hourly, time tracking is revenue.\n\n"
        "Conflict checking. Built-in across most PMS but with varying depth. Larger firms running more matters "
        "and more parties need full conflict-database features (party search, related-party detection, prior-matter "
        "lookups). Smaller firms can get by with simpler implementations.\n\n"
        "Total cost over three years. License cost is the headline. Implementation, training, integration setup, "
        "data migration from your current system, ongoing add-on costs, and the bookkeeper or admin time to run "
        "the platform are the rest. For a 10-attorney firm, all-in three-year cost typically runs $35,000-$120,000 "
        "depending on platform tier and add-ons."
    ),

    "pricing_landscape": (
        "Solo and entry-tier general PMS runs $39-89 per user per month (MyCase Basic at $39, PracticePanther Solo "
        "at $59, Clio EasyStart at $49). Mid-tier runs $79-129 per user per month (the bulk of working firms land "
        "here). Enterprise general practice runs $129-199 per user per month with feature-loaded plans. Document-"
        "heavy or PI-specialized PMS like Smokeball and Filevine sit in the $80-200 range with more variance based "
        "on firm size and add-ons. CosmoLex is a flat $89 per user per month including the trust-accounting depth.\n\n"
        "Enterprise PI and mass-tort PMS (Litify, Centerbase, large Filevine deployments) run $150-300+ per user per "
        "month with custom enterprise pricing, multi-year contracts, and meaningful implementation fees ($15,000-$75,000 "
        "in year one). Payments-only LawPay charges per-transaction (~2.95% plus $0.20) plus a small monthly fee.\n\n"
        "What drives variance within a tier: number of users, included document storage, integration tier "
        "(API access often costs extra), advanced reporting, and bundled training credits. Mid-firm and enterprise "
        "deals usually have negotiating room of 10-25% off list, especially on annual prepay."
    ),

    "market_trends": (
        "Three trend lines matter in 2026. First, the all-in-one trust-accounting thesis is winning in the mid-market. "
        "CosmoLex is growing faster than the general-PMS category and pulling firms that hit the limits of QuickBooks "
        "plus a separate ledger. Smaller PMS vendors are adding deeper trust accounting in response, but native built-in "
        "is a different product than QuickBooks-integrated.\n\n"
        "Second, AI is leaking into PMS at the edges. Clio added Clio Duo (AI chat summaries, draft assistance), MyCase "
        "added IQ (intake automation, lead scoring), PracticePanther added AI-assisted time entry. These additions are "
        "marginal but signal where the platforms want to go. The bigger story is that the PMS-adjacent AI tools "
        "(Spellbook for drafting, Lawmatics for intake, EvenUp for PI demand letters) are pulling workflow out of "
        "the PMS rather than into it.\n\n"
        "Third, pricing pressure at the bottom is forcing tier consolidation. PracticePanther's Solo at $59 and "
        "MyCase Basic at $39 are aggressive enough that Clio's EasyStart at $49 is losing share. Expect either "
        "Clio to introduce a sub-$40 tier or quietly stop competing for the smallest firms in 2027."
    ),

    "by_the_numbers": [
        {"number": "~73%", "label": "of US law firms run a modern cloud PMS in 2026 (up from ~58% in 2022)"},
        {"number": "~30%", "label": "estimated combined market share of Clio, MyCase, and PracticePanther in cloud PMS"},
        {"number": "10-25%", "label": "average time leakage from manual time tracking versus auto-capture solutions"},
        {"number": "$35K-$120K", "label": "all-in three-year PMS cost for a 10-attorney firm including implementation"},
    ],

    "comparisons": [
        ("/compare/clio-vs-mycase/", "Clio vs MyCase"),
        ("/compare/clio-vs-practicepanther/", "Clio vs PracticePanther"),
        ("/compare/mycase-vs-practicepanther/", "MyCase vs PracticePanther"),
        ("/compare/smokeball-vs-clio/", "Smokeball vs Clio"),
        ("/compare/filevine-vs-litify/", "Filevine vs Litify"),
        ("/compare/clio-vs-smokeball/", "Clio vs Smokeball"),
    ],

    "guides": [
        ("/guides/best-practice-management-software-solo-attorneys/", "Best PMS for Solo Attorneys"),
        ("/guides/best-legal-practice-management-small-firms/", "Best PMS for Small Law Firms"),
        ("/guides/best-pms-personal-injury-law-firms/", "Best PMS for PI Firms"),
        ("/guides/best-clio-alternatives/", "Best Clio Alternatives"),
    ],

    "faqs": [
        {
            "question": "What's the cheapest PMS that handles IOLTA compliance properly?",
            "answer": (
                "MyCase Basic at $39 per user per month is the cheapest general PMS with credible trust accounting, but the "
                "trust handling there is integration-based (through MyCase Payments) rather than fully native. PracticePanther "
                "Solo at $59 has similar capability. CosmoLex at $89 has the deepest native trust accounting at the lowest "
                "price point in that category. If you handle small-volume client funds, MyCase or PracticePanther work fine. "
                "If you handle large-volume trust transactions or run a high-IOLTA-activity practice (real estate closings, "
                "PI settlements, retainer-heavy litigation), CosmoLex pays back the price difference."
            ),
        },
        {
            "question": "When does it make sense to leave Clio for a specialist?",
            "answer": (
                "Leave for Smokeball if your practice is document-template-heavy and Clio Draft does not cover your templates "
                "well. Leave for Filevine or Litify if you have grown past 25 attorneys and run high-volume PI or mass tort "
                "where Clio's general-purpose model is awkward. Leave for CosmoLex if you are tired of running QuickBooks "
                "alongside Clio and want native trust accounting. Stay on Clio if your firm is general-purpose, mid-size or "
                "smaller, and your existing setup works. Migration costs typically run 80-200 hours of admin and bookkeeper "
                "time, and most firms underestimate it."
            ),
        },
        {
            "question": "How does Clio's recent Lawyaw acquisition affect document automation?",
            "answer": (
                "Lawyaw became Clio Draft and significantly closed the document-automation gap with Smokeball. Clio Draft "
                "supports template logic, court-rules awareness for major US states, automatic merge from matter data, and "
                "clause libraries. It is not as deep as Smokeball on family law and certain probate templates, but for general "
                "practice it eliminates the previous reason firms picked Smokeball over Clio. The acquisition also brought "
                "Clio closer to feature parity with Filevine on case-management workflow, though Filevine's customization "
                "depth and PI-specific feature set still win for high-volume PI."
            ),
        },
        {
            "question": "Is Salesforce-based Litify worth the cost over Filevine?",
            "answer": (
                "Only if your firm already lives on Salesforce or has a dedicated Salesforce admin. Litify's value compounds "
                "when other parts of the firm (marketing, BD, finance) run on Salesforce ecosystem tools. For pure case-"
                "management value, Filevine delivers similar capability at lower cost and with a smaller learning curve. The "
                "real test: list your top 15 case-management requirements. If five or more require multi-object Salesforce "
                "logic, Litify wins. If most are workflow and document-driven, Filevine is the better buy."
            ),
        },
        {
            "question": "Can I combine PMS and accounting in one tool?",
            "answer": (
                "Yes, in two distinct ways. CosmoLex bundles full accounting (general ledger, trust accounting, billing, "
                "financial statements) into the PMS itself, eliminating QuickBooks. Clio, MyCase, and PracticePanther bundle "
                "their own billing, invoicing, and trust accounting but rely on QuickBooks for general-ledger work. Most "
                "firms below 50 attorneys can run on either model. Above 50 attorneys, you typically end up with a dedicated "
                "accounting platform regardless of PMS choice."
            ),
        },
    ],
}

LEGAL_AI_LANDING = {}
