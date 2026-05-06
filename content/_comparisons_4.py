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
