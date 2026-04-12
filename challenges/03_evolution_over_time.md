# Challenge 3: Evolution of Verification Design Over Time

**Complexity:** High

## The Question

Have arms control agreements become more sophisticated in their verification and compliance mechanisms over time? The conventional narrative assumes increasing sophistication, but some scholars argue that post-Cold War treaties actually *reduced* verification rigor. What does the data show?

## Why It Matters

Understanding how governance institutions evolve over decades is essential for anticipating the trajectory of AI governance. If verification becomes more sophisticated as trust builds and experience accumulates, we might expect AI oversight to follow a similar path. If sophistication declines when geopolitical conditions change, that raises questions about the durability of governance standards.

## Your Task

Build a time-series of verification sophistication across the 80+ years covered by the AMC dataset. You might track mechanism counts, the prevalence of different compliance levels (consultation, demonstrated, verified), or the types of verification used (remote vs. in-person). Look for structural breaks, especially around major geopolitical shifts (end of Cold War, post-9/11). Are there periods of innovation? Regression?

**Datasets to start with:** `agreement_info`

**Tip:** `agreement_info` contains `year` alongside binary flags for each compliance mechanism type (`consultation_mechanism`, `demonstrated_compliance_mechanism`, `verified_compliance_mechanism`). Count variants are available for demonstrated (`demonstrated_compliance_mechanism_nr`) and verified (`verified_compliance_mechanism_nr`) mechanisms. This challenge can go far with just this one dataset.

## AI Governance Extension (Optional)

If verification evolves from simple to complex over time, what does that suggest about where AI governance is on this trajectory? If there was a post-Cold War decline, what would it take to maintain governance standards as geopolitical conditions shift?
