# AMC Research Sprint: Arms Control Governance and AI

**Dates:** April 13-14, 2026  
**Organizers:** Sophia Hatz (Uppsala University / Alva Myrdal Centre) & Amritanshu Prasad

## Overview

This repository contains research challenges and datasets for the AMC Research Sprint. Teams of 2-4 participants will work over two days to produce empirical analyses using the Alva Myrdal Centre Arms Control Agreement Database (V2).

Each challenge has two parts:

- **Part A (Empirical):** Data analysis using AMC datasets. This is the core deliverable.
- **Part B (AI Governance Extension, optional):** Participants draw analogies between their empirical findings and current debates in AI governance. Teams that attempt Part B should explain their reasoning (e.g., identifying analogous governance structures, transferable design principles).

## Repository Structure

```
├── challenges/          # 10 research challenges with analysis plans
│   ├── overview.md      # Summary table and sprint logistics
│   └── 01-10            # Individual challenge specifications
├── data/                # AMC datasets (CSV) and codebook
│   ├── README.md        # Dataset descriptions and column reference
│   └── codebook/        # Full variable documentation (86-page PDF)
├── examples/            # Starter code for loading and exploring data
├── SETUP.md             # Python, Git, and environment setup guide
└── requirements.txt     # Python package dependencies
```

## Getting Started

**New to Python or Git?** See [`SETUP.md`](SETUP.md) for installation and setup instructions.

1. Browse [`challenges/overview.md`](challenges/overview.md) for the full list of challenges
2. Read the [`data/README.md`](data/README.md) for dataset descriptions
3. Pick a challenge and review its specification in `challenges/`
4. Run `pip install -r requirements.txt` to install dependencies
5. Use the starter code in `examples/` to load the data

**Note:** The CSV files use `latin-1` encoding. See [`data/README.md`](data/README.md) for details.

## Datasets

The AMC Arms Control Agreement Database (V2) contains structured data on international arms control agreements, covering verification mechanisms, compliance architectures, weapons categories, and participation patterns.

| Dataset | Rows | Description |
|---------|------|-------------|
| `agreement_info` | 128 | Core agreement metadata, dates, participation, compliance mechanism flags |
| `vercom` | 99 | Verified compliance mechanisms (inspectors, access, triggers) |
| `demcom` | 136 | Demonstrated compliance mechanisms |
| `consultation` | 159 | Consultation mechanisms |
| `weapons_facilities` | 434 | Weapons types, lifecycle restrictions, categories |
| `agreement_associations` | 137 | Links between related agreements |

Full codebook: [`data/codebook/amc_agreementdatasets_codebook.pdf`](data/codebook/amc_agreementdatasets_codebook.pdf)

## Deliverables

Teams choose their preferred output format:

- Data visualization (chart, map, or interactive)
- 1-page policy brief
- Blog post

All teams should produce a cleaned, documented dataset and statistical analysis for Part A.

## Data Access

The AMC datasets are shared for sprint participants only. Do not redistribute without permission from the Alva Myrdal Centre for Nuclear Disarmament, Uppsala University.

## Contact

- Sophia Hatz: sophia.hatz@pcr.uu.se
- Amritanshu Prasad: amritanshuprasad2001@gmail.com
