# Challenge 8: The Compliance Architecture Spectrum

**Complexity:** Lower quantitative, higher qualitative

## The Question

How do arms control agreements vary in their compliance monitoring architecture? The AMC dataset distinguishes three levels: consultation, demonstrated compliance, and verified compliance. What patterns emerge across weapon types and over time?

## Why It Matters

Not all oversight is created equal. Consultation mechanisms (treaty review conferences) differ fundamentally from demonstrated compliance (states show they are complying) and verified compliance (third parties check). Understanding how arms control allocates these different levels of oversight can inform debates about appropriate tiers of AI oversight.

## Your Task

Construct an ordinal scale of compliance architecture intensity and examine how it distributes across weapon categories and over time. The quantitative analysis is relatively straightforward. The depth in this challenge comes from the qualitative side: for each compliance level, identify concrete examples from specific treaties and describe how the mechanism operates in practice.

**Datasets to start with:** `agreement_info`, `weapons_facilities`

**Tip:** `agreement_info` has binary flags for `consultation_mechanism`, `demonstrated_compliance_mechanism`, and `verified_compliance_mechanism`. To compare across weapon categories, join with `weapons_facilities` via `agreement_id` and use the `item` field (after `.str.strip()`) to classify agreements by weapon type. Note that `summary_category` is a binary flag (0 = real item, 1 = summary row), not a weapon category label.

## AI Governance Extension (Optional)

Map the compliance spectrum to proposed AI oversight frameworks:

| Compliance Level | Arms Control Example | Possible AI Analogue |
|-----------------|---------------------|---------------------|
| Consultation | Treaty review conferences | Industry self-reporting, voluntary commitments |
| Demonstrated compliance | State-submitted reports | Model cards, safety cases, public benchmarks |
| Verified compliance | IAEA inspections | Independent audits, red-teaming, interpretability review |

What does the arms control pattern suggest about which oversight intensity is appropriate for which level of AI risk?
