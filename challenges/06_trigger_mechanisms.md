# Challenge 6: Trigger Mechanisms

**Complexity:** High

## The Question

How are compliance mechanisms activated across arms control agreements? When does monitoring happen automatically on a schedule, when does it require a state to request it, and when is it triggered by specific circumstances?

## Why It Matters

No systematic taxonomy of trigger mechanisms across arms control exists. Building one would fill a gap in the compliance literature and provide a direct mapping to AI oversight design, where the question of *when* monitoring activates (scheduled audits vs. complaint-based vs. anomaly-triggered) is actively debated.

## Your Task

Categorize the trigger mechanisms in the AMC dataset into a typology. A natural starting point:

1. **Scheduled/routine**: Cyclical inspections, quota-based monitoring
2. **State-party-initiated**: Triggered by a state party's request
3. **Circumstance-triggered**: Activated by specific events or conditions

The data already codes trigger types in both the demonstrated compliance (`demcom`) and verified compliance (`vercom`) datasets. Your task is to build a taxonomy from these, analyse how trigger types distribute across agreement types and time periods, and interpret the patterns.

**Datasets to start with:** `demcom`, `vercom`, `agreement_info`

**Tip:** Look at the `*trigger*` columns in both `demcom` and `vercom`. The data structure already distinguishes trigger types, so extraction is straightforward. The analytical value lies in the taxonomy you build and the patterns you find across weapon categories and eras.

## AI Governance Extension (Optional)

Map trigger types to AI oversight activation models:

| Arms Control | AI Oversight |
|-------------|-------------|
| Scheduled/routine | Periodic audits, scheduled evaluations |
| State-party-initiated | Complaint-based investigations, whistleblower reports |
| Circumstance-triggered | Anomaly detection, capability thresholds |

What does arms control experience suggest about which trigger designs are most effective, and under what conditions?
