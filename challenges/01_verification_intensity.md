# Challenge 1: Verification Intensity by Weapon Type

**Complexity:** Medium

## The Question

Do more dangerous weapon categories receive more intensive verification under existing treaties? Policy discussions often assume "risk-proportionate governance," where higher-risk technologies warrant stronger oversight. But does this hold empirically across 80 years of arms control?

## Why It Matters

Within the nuclear domain, verification ranges from vague provisions (e.g., Nuclear Weapon-Free Zones) to highly intrusive regimes (e.g., INF Treaty, New START). Outside nuclear weapons, the picture is strikier: the Chemical Weapons Convention has extensive verification, while the Biological Weapons Convention has almost none. If risk-proportionate governance is more assumption than reality, that has implications for how we design oversight for new technologies.

## Your Task

Using the AMC datasets, construct a measure of verification intensity and compare it across weapon categories. You might consider mechanism counts, access depth, inspector arrangements, or some combination. Are there patterns? Outliers? What explains cases where high-risk weapons have weak verification, or vice versa?

**Datasets to start with:** `agreement_info`, `vercom`, `weapons_facilities`

**Tip:** The `item` field in `weapons_facilities` describes what each agreement regulates (e.g., "Nuclear Weapons", "Chemical Weapons", "Small Arms and Light Weapons"). Strip trailing whitespace with `.str.strip()` before matching. Note that `summary_category` is a binary flag (0 = real item, 1 = summary row added by AMC), not a weapon type label. Link datasets using `agreement_id`.

## AI Governance Extension (Optional)

If a risk-verification gradient exists in arms control, does that support capability-based AI regulation (more oversight for frontier models)? If the gradient is absent, what does that tell us about the political feasibility of risk-proportionate AI governance?
