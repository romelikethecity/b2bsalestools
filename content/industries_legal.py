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

# Scope landing content (filled in Tasks 8-9)
LEGAL_SAAS_LANDING = {}
LEGAL_AI_LANDING = {}
