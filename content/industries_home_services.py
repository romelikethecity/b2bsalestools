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
    "by_the_numbers": [],  # Filled from TradeBridge brand
    "faqs": [],  # Filled in Task 7
    "last_verified": "2026-05-05",
}

HOME_SERVICES_SAAS_TOOLS = [
    ("servicetitan", "ServiceTitan", "https://www.servicetitan.com", "enterprise-residential",
     "Custom; ~$8K-15K+ per year per site for small ops, scales high",
     "Enterprise FSM for residential HVAC, plumbing, and electrical with full ops platform.",
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
     "Custom; typically ~$100 per user/month equivalents",
     "FSM for HVAC, plumbing, and electrical with deep QuickBooks integration.",
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
     "From ~$70 per user/month plus setup; quote-based",
     "Mid-market FSM for trade contractors covering service plus project work.",
     "Multi-trade contractors with both service work and longer-form projects (acquired BigChange)"),
    ("buildops", "BuildOps", "https://buildops.com", "commercial",
     "Custom enterprise, premium tier",
     "Commercial-focused FSM and project management for HVAC, electrical, and plumbing.",
     "Commercial trades contractors (10-200 techs)"),
]

HOME_SERVICES_SAAS_SUB_CLUSTERS = {
    "enterprise-residential": "Enterprise residential trades. Full ops platforms for $5M+ revenue businesses.",
    "smb-residential": "SMB residential trades. FSM for 1-15 person shops.",
    "mid-market-flat": "Mid-market with flat pricing. Predictable cost as team grows.",
    "niche": "Niche services. Pest control, lawn care, recurring-service-specific FSM.",
    "mid-market-multi-trade": "Mid-market multi-trade. Service plus project work.",
    "commercial": "Commercial contractor focus. Non-residential job complexity, larger crews.",
}

HOME_SERVICES_AI_TOOLS = [
    ("avoca", "Avoca AI", "https://www.avoca.ai", "ai-receptionist",
     "Custom; usage-based",
     "AI voice agents for inbound calls in home services, ServiceTitan-integrated.",
     "Mid-to-large HVAC, plumbing, and roofing operations with high inbound call volume"),
    ("hatch", "Hatch", "https://www.usehatchapp.com", "csr-platform",
     "Per-seat / contact sales",
     "AI CSR platform handling voice, SMS, and email across 2,000+ home service customers.",
     "Multi-channel-customer-service home service businesses"),
    ("sera", "Sera Systems", "https://sera.tech", "ai-fsm",
     "$399 per month for 4 users plus $149 per extra tech",
     "AI-powered FSM with auto-dispatcher for HVAC, plumbing, and electrical.",
     "Trades teams who want AI dispatch without leaving their primary FSM"),
    ("rilla", "Rilla", "https://www.rilla.com", "sales-coaching",
     "~$199-349 per rep/month (~$40K+ per year for 10 reps)",
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
     "Smallest trades shops where $49 per month is the budget ceiling"),
    ("chirp", "Chirp", "https://chirpchat.com", "csr-platform",
     "Contact sales",
     "Text automation with AI for home service businesses.",
     "Trades businesses wanting SMS-first customer comms"),
]

HOME_SERVICES_AI_SUB_CLUSTERS = {
    "ai-receptionist": "AI receptionist / inbound voice. Answers calls when humans cannot.",
    "csr-platform": "Customer service platforms. Multi-channel inbound and outbound comms.",
    "sales-coaching": "AI sales coaching. Speech analytics and ride-along for in-home reps.",
    "ai-fsm": "AI-native FSM. Dispatch and scheduling AI built into the FSM itself.",
}

# Scope landing content (filled in Tasks 10-11)
HOME_SERVICES_SAAS_LANDING = {}
HOME_SERVICES_AI_LANDING = {}
