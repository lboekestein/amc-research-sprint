# Challenge 5: Dual-Use Technology Coverage

**Complexity:** Medium

## The Question

How do arms control agreements handle dual-use technologies, items with both civilian and military applications? What patterns emerge in how different lifecycle phases (development, production, transfer) are restricted?

## Why It Matters

AI is paradigmatically dual-use, and debates about regulating AI training, deployment, and model sharing echo long-standing arms control dilemmas. Understanding how existing treaties manage the civilian-military boundary across different phases of a technology's lifecycle offers concrete precedents for AI governance design.

## Your Task

Examine how treaties restrict items across lifecycle phases using the ban and restriction variables in `weapons_facilities`. Look at whether agreements tend to restrict development, production, or transfer, and whether patterns differ across weapon categories. You may want to identify items that have plausible civilian applications (e.g., enrichment technology, chemical precursors, delivery systems) and examine whether they are governed differently.

**Note:** The AMC dataset does not explicitly code items as "dual-use." Part of this challenge involves developing a reasonable way to identify or approximate dual-use status, possibly using external references (Wassenaar Arrangement, Nuclear Suppliers Group, Australia Group).

**Datasets to start with:** `weapons_facilities`, `agreement_info`

**Tip:** The `ban_*` and `restriction_*` columns in `weapons_facilities` cover development, production, and transfer phases. The `item` and `subcategory` fields describe what is being regulated.

## AI Governance Extension (Optional)

Map arms control lifecycle restrictions to AI governance phases: training (development), deployment (production/use), and model sharing or open-sourcing (transfer). Which AI governance interventions have arms control precedent? Which are genuinely novel?
