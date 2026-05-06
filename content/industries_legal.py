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
    "by_the_numbers": [],  # Filled in Task 6 from Lexica vertical-data brand counts
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
