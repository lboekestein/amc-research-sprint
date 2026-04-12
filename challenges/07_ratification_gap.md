# Challenge 7: The Ratification Gap

**Complexity:** High

## The Question

Which arms control agreements have the largest gap between the number of states that signed and the number that actually ratified? What predicts whether states follow through?

## Why It Matters

Ratification gap research is well-established in human rights and environmental law, but it has not been systematically applied to arms control. Understanding what drives the gap between stated commitment and binding implementation matters for any domain where actors make governance pledges, including AI.

## Your Task

Calculate the signature-to-ratification gap across agreements and identify which ones show the largest shortfalls. Then investigate what predicts the gap: is it agreement characteristics (verification intensity, weapon type, scope), or is it primarily about domestic political factors (which may be harder to observe in this dataset)?

You might also explore timing: how long does it take for agreements to move from adoption to entry into force? Are there agreements that stalled?

**Datasets to start with:** `agreement_info`

**Tip:** Key variables include `nr_signatory_states` (~80% populated), `nr_states_parties_total` (~83%), `nr_states_parties_ratification` (~70%), `adoption_date` (~34%, so timing analysis will be limited to a subset), and `entry_into_force_date` (~77%). Note that the gap between signing and ratifying is typically driven by domestic political procedures rather than agreement content, so interpret carefully.

## AI Governance Extension (Optional)

Many AI governance commitments are "signed" (publicly announced) but not "ratified" (implemented with binding mechanisms). Think of the Bletchley Declaration, voluntary commitments by labs, or AI ethics principles. What does the arms control ratification gap suggest about predicting which AI governance commitments will actually be implemented?

Note: be precise about which phenomenon you are studying. The signing-ratification gap is distinct from non-compliance after ratification.
