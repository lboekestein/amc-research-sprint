# Challenge 9: Inspector Types

**Complexity:** Lower quantitative, higher qualitative

## The Question

Who conducts verification? How common are international inspectors compared to bilateral arrangements or national technical means? What predicts which inspector model an agreement uses?

## Why It Matters

Inspector identity is central to compliance theory: who watches matters as much as what they watch. The AI governance space is actively debating whether oversight should come from international bodies, national regulators, industry self-assessment, or independent third parties. Arms control has tried all of these, and the data can show what predicts each arrangement.

## Your Task

Categorize inspector types across verified compliance mechanisms and examine what agreement characteristics predict different arrangements. Be aware that inspector type may be strongly associated with whether treaties are bilateral or multilateral, so consider controlling for this. The quantitative analysis is descriptive; the value-add is developing a qualitative typology with concrete examples.

**Datasets to start with:** `vercom`, `agreement_info`

**Tip:** `vercom` contains inspector type variables including `verified_compliance_mechanism_inspector_type`, `*_established_body`, and `*_utlilized_body`. Link to `agreement_info` for `laterality` (bilateral vs. multilateral) and other agreement characteristics.

## AI Governance Extension (Optional)

Apply findings to AI auditing debates:

| Inspector Model | Arms Control Example | AI Analogue |
|----------------|---------------------|-------------|
| International body | IAEA, OPCW | International AI safety body |
| Bilateral | US-Russia inspectors | Government-to-lab oversight |
| National technical means | Satellite monitoring | National compute monitoring |
| Third-party | — | Independent auditors, red teams |

If multilateral agreements favour international inspectors, what does this suggest for global AI governance architecture?
