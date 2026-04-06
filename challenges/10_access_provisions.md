# Challenge 10: Access Provisions

**Complexity:** Lower quantitative, higher qualitative

## The Question

What access do verification mechanisms provide? The AMC dataset codes four levels of depth, from broad area access down to item-section (component-level) inspection. What predicts different access levels, and does greater intrusiveness affect participation?

## Why It Matters

States face a fundamental tension: they want maximum intrusiveness into *others* but minimal into *themselves*. The same dynamic plays out with AI labs navigating transparency requirements. Understanding how arms control agreements have resolved this tension across different contexts offers lessons for designing AI audit regimes that are both effective and acceptable.

## Your Task

Construct a "ladder of verification intrusiveness" from the access variables in `vercom` and examine how access depth varies across weapon categories and agreement types. You might also test whether more intrusive access provisions are associated with fewer state parties (connecting to Challenge 2). The qualitative component involves describing what each access level looks like in practice and identifying what makes some agreements grant deeper access than others.

**Datasets to start with:** `vercom`, `agreement_info`, `weapons_facilities`

**Tip:** `vercom` has binary flags for `*_area_access`, `*_facility_access`, `*_item_access`, and `*_item_section_access`, with accompanying specification fields. These give you a natural four-level scale.

## AI Governance Extension (Optional)

Map the intrusiveness ladder to AI audit access levels:

| Access Level | Arms Control | AI Analogue |
|-------------|-------------|-------------|
| Area | Geographic region monitoring | External behavioural testing (API-level) |
| Facility | Site inspection | Training infrastructure review |
| Item | Weapon/material inspection | Model weights access |
| Item-section | Component-level inspection | Internal activations, interpretability |

What does the arms control trade-off between intrusiveness and participation suggest for mandatory AI transparency requirements?
