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

LEGAL_AI_LANDING = {
    "hero_verdict": (
        "If you are a personal-injury firm, EvenUp for demand letters and medical chronologies, Eve for end-to-end "
        "PI workflow, Supio for high-volume mass tort. If you are a transactional shop drafting contracts, Spellbook "
        "wins inside Microsoft Word. If you are BigLaw or enterprise legal, Harvey or Westlaw Precision with CoCounsel. "
        "For pure legal research, Lexis+ AI or Westlaw Precision with CoCounsel depending on which platform you "
        "already use. For litigation drafting and discovery responses, Briefpoint. For intake automation and lead "
        "scoring, Lawmatics. For matter-summary AI and court-reporting workflow, CaseMark.\n\n"
        "Two notes on what is missing from the Wave 1 set. Robin AI was sold to Scissero in late 2025 with the "
        "engineering team going to Microsoft, so we omit it pending product continuity confirmation. Free or "
        "consumer-grade AI tools (free ChatGPT, Claude.ai consumer) are excluded because state-bar guidance is "
        "warning against using them for client work."
    ),

    "methodology": (
        "We evaluated each AI tool on six criteria. Citation grounding (does it hallucinate cases? what is the "
        "guardrail design?). Workflow integration (Word, Outlook, your PMS, your DMS). Data privacy and "
        "confidentiality posture (where is data processed? are inputs used for training?). ROI math at the firm "
        "level (hours saved, throughput per matter). Pricing model and pilot accessibility. State-bar ethics "
        "compliance (does the tool publish guidance, audit trails, supervision controls?). Pricing and feature "
        "data verified against vendor sites and recent customer reports as of 2026-05-05."
    ),

    "cluster_intros": {
        "biglaw": (
            "BigLaw AI is Harvey's category. Westlaw Precision with CoCounsel is the credible alternative for firms "
            "already on Westlaw. Both target the AmLaw 100/200 procurement cycle, both publish enterprise-grade "
            "privacy and audit documentation, and both are priced at custom annual contracts in the six- and "
            "seven-figure range. Mid-market firms that buy Harvey or CoCounsel typically do so when partner billing "
            "rates above $700/hour make the time savings pay back fast."
        ),
        "contract-review": (
            "Contract drafting and review AI moved fast in the last 18 months. Spellbook leads inside Microsoft Word "
            "with strong template logic, clause libraries, and a solid pricing tier for transactional teams. Harvey "
            "covers contract use cases inside the broader BigLaw platform. The category is volatile: Robin AI was "
            "the third major player and effectively shut down its core SaaS in late 2025. Watch for new entrants "
            "in 2026-2027 as venture funding flows into vertical legal AI."
        ),
        "research": (
            "Legal research AI is the highest-stakes incumbent battle. Lexis+ AI and Westlaw Precision with CoCounsel "
            "both offer conversational query, deep citation grounding, and integration into the research products "
            "lawyers already use. Pricing is add-on to existing Lexis or Westlaw subscriptions. The decision usually "
            "comes down to which research platform your firm already runs on. Independent AI research tools struggle "
            "to compete because the citation-grounding moat requires the underlying case-law corpus."
        ),
        "pi-plaintiff": (
            "Personal injury and plaintiff AI is the most active sub-category in 2026. EvenUp leads with AI demand "
            "letters and medical chronologies, used at scale across hundreds of PI firms. Eve covers the full PI "
            "case lifecycle from intake through settlement. Supio specializes in heavy medical record review for "
            "PI and mass tort. The buyers here have very specific ROI math: a single AI-generated demand package "
            "that would have taken a paralegal 8-12 hours costs $200-$500 and is ready in minutes. The category "
            "has more vendor differentiation than any other legal AI segment."
        ),
        "litigation-drafting": (
            "Litigation drafting and discovery is a pragmatic, less-glamorous AI category. Briefpoint focuses on "
            "discovery responses, objections, and motion practice. CaseMark covers matter summaries, court-reporter "
            "transcript work, and a credit-based usage model that fits unpredictable case loads. Both are priced "
            "for mid-market litigation firms ($89-$300+ per user per month) and both pay back within a few matters "
            "for firms with consistent discovery-response volume."
        ),
        "intake-crm": (
            "Intake and CRM AI is shaped by the marketing-driven inbound that personal injury, family, and certain "
            "criminal-defense firms run on. Lawmatics is the leader, with intake automation, lead scoring (QualifyAI), "
            "and marketing analytics. The category is adjacent to PMS (Clio Grow, MyCase intake) but with deeper "
            "marketing and lead-quality features. Firms running paid acquisition (Google Ads, Facebook, billboards) "
            "with material ad spend tend to need a dedicated intake CRM regardless of PMS choice."
        ),
    },

    "buyer_framework": (
        "Six things matter when picking AI for a US law firm.\n\n"
        "Citation grounding and hallucination control. AI that invents case citations is a bar-grievance machine. "
        "Tools designed for legal use (Harvey, Lexis+ AI, Westlaw Precision, Spellbook) have engineered citation "
        "validation into the workflow. Generic consumer AI does not. The first vendor question: how does this tool "
        "prevent hallucinated citations and what is the audit trail when something slips through?\n\n"
        "Data privacy and confidentiality. Where is client data processed? Is it used for training? What contractual "
        "protections exist? Enterprise legal AI tools all publish data-handling documentation. If a tool cannot "
        "answer 'we do not train on your data and our processing is documented for SOC 2 audit,' do not put privileged "
        "matter content into it.\n\n"
        "Workflow integration depth. AI that lives outside your existing workflow (Word, Outlook, Lexis, your PMS) "
        "is AI you forget to use. Spellbook's Word integration is the canonical example of doing this well. Lexis+ "
        "AI and Westlaw Precision both integrate inside their research products. CaseMark and Briefpoint integrate "
        "with PMS systems. Standalone web apps are harder to drive adoption on.\n\n"
        "ROI math at the matter level. The serious AI tools all let you calculate hours saved per matter or per "
        "drafting task. Spellbook reports 6-9 hours saved per contract on average. EvenUp reports a 70-90% time "
        "reduction on demand letters. Briefpoint reports 50-70% reduction on discovery response drafting. Get the "
        "vendor's claims, then run a 30-60 day pilot on real matters and measure for yourself.\n\n"
        "Pricing model fit. Per-user-per-month is fine for tools used daily by every attorney. Usage-based or per-"
        "credit is better for tools used episodically (CaseMark, Briefpoint at lower volumes). Custom enterprise "
        "annual contracts make sense above 50 attorneys with dedicated procurement. Free tiers are rare in legal "
        "AI and usually limited to demos.\n\n"
        "Bar ethics compliance. Florida, California, ABA, and most other state bars have published guidance on "
        "competent AI use. Tools that publish their own ethics-compliance documentation, supervision controls, and "
        "billing-rate guidance make the supervisory work easier. Tools that do not put the burden on you to figure "
        "it out matter by matter."
    ),

    "pricing_landscape": (
        "Per-seat AI tools cluster in two bands. Solo and small-firm tools (Briefpoint at $89/mo, Spellbook Starter "
        "at $99 per user/mo, CaseMark on credit packages) target individual or small-team buyers and ship for "
        "two-figure to low-three-figure monthly cost. Mid-market AI (Spellbook Enterprise at $199 per user/mo with "
        "10-seat minimum, Lawmatics premium at $300+ per user/mo) sits in the high-three-figure to low-four-figure "
        "range per user per month.\n\n"
        "Enterprise legal AI is a different pricing world. Harvey custom enterprise contracts run $100,000+ annually "
        "minimum, scaling well into seven figures for AmLaw 100 deployments. Westlaw Precision with CoCounsel and "
        "Lexis+ AI are both add-ons to existing Lexis or Westlaw research subscriptions, with custom pricing usually "
        "in the $20,000-$200,000 annual range depending on firm size and seat count. EvenUp, Eve, and Supio all run "
        "custom firm-level subscriptions with usage-based add-ons; typical PI firms doing 100-500 demands per year "
        "spend $30,000-$150,000 annually all-in.\n\n"
        "Pilot programs are common (Harvey, EvenUp, Supio all run them) and typically last 30-60 days at reduced "
        "or zero cost. Most enterprise legal AI buyers should run a real pilot before signing a multi-year contract."
    ),

    "market_trends": (
        "Three trends shape legal AI in 2026.\n\n"
        "BigLaw consolidation around Harvey is largely over. Harvey is in most AmLaw 100 firms and a meaningful "
        "share of the AmLaw 200. Westlaw Precision with CoCounsel and Lexis+ AI are competitive on research-focused "
        "use cases but Harvey owns the broader BigLaw platform position. The next BigLaw battle is on specific "
        "workflow tools that integrate with Harvey rather than try to replace it.\n\n"
        "PI vendor wars are getting expensive. EvenUp, Eve, and Supio all raised at unicorn or near-unicorn "
        "valuations between 2024 and 2026 and are spending aggressively on PI-firm sales. Mass tort, class action, "
        "and high-volume PI firms are the prime targets. Firms running 1,000+ matters annually report saving 6-7 "
        "figures per year on combined paralegal time and demand-package quality. Smaller PI firms (under 200 "
        "matters/yr) see less ROI and the pricing math is tighter.\n\n"
        "Legal research AI is settling into incumbent dominance. Independent vendors that tried to build standalone "
        "AI research products with limited case-law corpus access struggled to match the citation grounding that "
        "Lexis and Westlaw deliver. Watch this space if AI vendors find ways to license or build comparable corpus "
        "access. Otherwise, Lexis and Westlaw will keep the research category for the foreseeable future."
    ),

    "by_the_numbers": [
        {"number": "~70%", "label": "of AmLaw 100 firms have adopted Harvey or a comparable AI platform by mid-2026"},
        {"number": "<15%", "label": "of solo and small-firm attorneys actively use legal-specific AI tools"},
        {"number": "6-9 hours", "label": "average time saved per contract review using AI (Spellbook customer reports)"},
        {"number": "70-90%", "label": "time reduction on demand letter drafting using EvenUp or Eve (vendor-reported)"},
    ],

    "comparisons": [
        ("/compare/harvey-vs-spellbook/", "Harvey vs Spellbook"),
        ("/compare/evenup-vs-eve/", "EvenUp vs Eve"),
        ("/compare/evenup-vs-supio/", "EvenUp vs Supio"),
        ("/compare/lexis-ai-vs-westlaw-precision/", "Lexis+ AI vs Westlaw Precision"),
        ("/compare/spellbook-vs-lexis-ai/", "Spellbook vs Lexis+ AI"),
        ("/compare/harvey-vs-cocounsel/", "Harvey vs CoCounsel"),
    ],

    "guides": [
        ("/guides/best-legal-ai-personal-injury-firms/", "Best Legal AI for PI Firms"),
        ("/guides/best-ai-contract-review-software/", "Best AI Contract Review Software"),
        ("/guides/best-ai-legal-research-tools/", "Best AI Legal Research Tools"),
        ("/guides/best-ai-tools-solo-lawyers/", "Best AI Tools for Solo Lawyers"),
    ],

    "faqs": [
        {
            "question": "Will AI replace junior associates and paralegals?",
            "answer": (
                "Not in the wholesale way the headlines imply. AI is taking specific tasks (first-draft document review, "
                "demand letter drafting, citation lookup, summary generation) where the work was repetitive and "
                "throughput-limited. Junior associates whose value was in those tasks are seeing their workload "
                "shift toward higher-judgment work earlier in their careers. Firms that adopted AI aggressively in "
                "2024-2025 report leaner first-year associate classes (10-20% smaller) but not wholesale layoffs. "
                "Paralegals doing high-volume document and discovery work are seeing more pressure, especially in PI."
            ),
        },
        {
            "question": "Can AI tools cite cases that do not exist?",
            "answer": (
                "Yes, and several lawyers have been sanctioned for filing AI-drafted briefs with hallucinated citations. "
                "Legal-specific AI tools (Harvey, Lexis+ AI, Westlaw Precision, Spellbook) have engineered citation "
                "validation into the product to make this much harder, but no tool eliminates the risk completely. "
                "Always verify citations before filing. Bar ethics rules require it as part of competent supervision, "
                "and the high-profile sanction cases have all involved generic consumer AI used without verification."
            ),
        },
        {
            "question": "What is the best AI for solo lawyers on a budget?",
            "answer": (
                "For drafting, Spellbook Starter at $99/mo or a Briefpoint subscription. For research, the AI add-on "
                "to your existing Lexis or Westlaw subscription if you have one. For intake, Lawmatics Lite at $199 "
                "per firm/mo if you have inbound flow worth automating. CaseMark's credit packages are useful for "
                "matter summaries on an episodic basis. Harvey, Eve, EvenUp, and Supio are not built for solo budgets "
                "(custom enterprise pricing). A solo PI attorney handling 5-15 matters per year is better off with "
                "EvenUp's per-document pricing than a full subscription."
            ),
        },
        {
            "question": "When is Harvey worth $100,000+ per year?",
            "answer": (
                "When your firm has 50+ attorneys, partner billing rates above $700/hour, and consistent volume on "
                "research-heavy matters (M&A, complex litigation, regulatory work). At those rates, Harvey saving "
                "100-200 hours per year per attorney pays back the cost several times over. Smaller firms paying "
                "Harvey enterprise pricing rarely make the math work because the partner-rate-times-hours-saved "
                "calculation drops below the contract cost. The price-to-firm-size sweet spot for Harvey starts "
                "around 25-50 attorneys depending on rate structure."
            ),
        },
        {
            "question": "Are these tools confidentiality-safe under bar rules?",
            "answer": (
                "Yes if you pick a tool designed for legal use with documented data-handling practices. Harvey, "
                "Spellbook, Lexis+ AI, Westlaw Precision, and the major PI-AI platforms (EvenUp, Eve, Supio) all "
                "publish privacy documentation, do not train on your inputs, and offer SOC 2 audit reports. The risk "
                "is generic consumer AI (free ChatGPT, Claude.ai consumer) where data handling is less protected and "
                "several state bars have published warnings against using them for client work. ABA Model Rule 1.6 "
                "and the corresponding state rules all apply to AI use, and the supervisory burden is on you, not "
                "on the tool."
            ),
        },
    ],
}
