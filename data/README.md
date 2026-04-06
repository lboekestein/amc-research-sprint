# AMC Arms Control Agreement Database (V2)

Source: Alva Myrdal Centre for Nuclear Disarmament, Uppsala University

Full documentation: see [`codebook/amc_agreementdatasets_codebook.pdf`](codebook/amc_agreementdatasets_codebook.pdf) (86 pages)

## Datasets

### `amcdata_agreement_info_V2.csv` (127 rows)

Core agreement metadata. One row per agreement.

**Key columns:**
- `agreement_id` - Unique identifier (use for joins)
- `agreement_name` - Full name
- `year` - Year of agreement
- `adoption_date`, `entry_into_force_date` - Key dates
- `laterality` - Bilateral vs. multilateral
- `nr_signatory_states` - Number of signatories
- `nr_states_parties_total` - Total state parties
- `nr_states_parties_ratification` - Ratified parties
- `nr_states_parties_accession` - Acceded parties
- `status` - Agreement status
- `consultation_mechanism` - Consultation present (binary)
- `demonstrated_compliance_mechanism` - Demonstrated compliance present (binary)
- `demonstrated_compliance_mechanism_nr` - Count
- `verified_compliance_mechanism` - Verified compliance present (binary)
- `verified_compliance_mechanism_nr` - Count

### `amcdata_vercom_V2.csv` (98 rows)

Verified compliance mechanisms. One row per mechanism.

**Key columns:**
- `agreement_id` - Link to agreement_info
- `verified_compliance_mechanism_type` - Mechanism type
- `verified_compliance_mechanism_category` - Category
- `verified_compliance_mechanism_inspector_type` - Inspector type
- `verified_compliance_mechanism_inspector_type_established_body` - Established body
- `verified_compliance_mechanism_inspector_type_utlilized_body` - Utilized body
- `verified_compliance_mechanism_area_access` - Area access (binary)
- `verified_compliance_mechanism_facility_access` - Facility access (binary)
- `verified_compliance_mechanism_item_access` - Item access (binary)
- `verified_compliance_mechanism_item_section_access` - Item-section access (binary)
- `verified_compliance_mechanism_trigger_type` - Trigger type
- `verified_compliance_mechanism_agreement_trigger_cyclical` - Cyclical trigger

### `amcdata_demcom_V2.csv` (~300 rows)

Demonstrated compliance mechanisms. One row per mechanism.

**Key columns:**
- `agreement_id` - Link to agreement_info
- `demonstrated_compliance_mechanism_trigger_type` - Trigger type
- `demonstrated_compliance_mechanism_trigger_cyclical` - Cyclical trigger
- `demonstrated_compliance_mechanism_trigger_state_party_action` - State party trigger
- `demonstrated_compliance_mechanism_trigger_circumstance` - Circumstance trigger

### `amcdata_consultation_V2.csv` (~150 rows)

Consultation mechanisms. One row per mechanism.

- `agreement_id` - Link to agreement_info

### `amcdata_weapons_facilities_V2.csv` (~300 rows)

Weapons types, lifecycle restrictions, and categories. One row per weapon/facility item.

**Key columns:**
- `agreement_id` - Link to agreement_info
- `item` - Specific item description
- `subcategory` - Item subcategory
- `summary_category` - High-level classification (Nuclear Weapons, Conventional Weapons Land, etc.)
- `ban_development`, `restriction_development` - Development phase
- `ban_production`, `restriction_production` - Production phase
- `ban_transfer`, `restriction_transfer` - Transfer phase

### `amcdata_agreement_associations_V2.csv`

Links between related agreements.

- `agreement_id` - Source agreement
- Related agreement identifiers

## Joining Datasets

All datasets share `agreement_id` as the linking variable. Example in Python:

```python
import pandas as pd

info = pd.read_csv('amcdata_agreement_info_V2.csv')
vercom = pd.read_csv('amcdata_vercom_V2.csv')
weapons = pd.read_csv('amcdata_weapons_facilities_V2.csv')

# Join verification mechanisms with agreement metadata
merged = vercom.merge(info, on='agreement_id', how='left')

# Add weapon categories
merged = merged.merge(weapons[['agreement_id', 'summary_category']].drop_duplicates(),
                      on='agreement_id', how='left')
```

## Data Access

This data is shared for AMC Research Sprint participants only. Do not redistribute without permission from the Alva Myrdal Centre for Nuclear Disarmament, Uppsala University.
