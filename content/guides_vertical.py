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
