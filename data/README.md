# AMC Arms Control Agreement Database (V2)

Source: Alva Myrdal Centre for Nuclear Disarmament, Uppsala University

Full documentation: see [`codebook/amc_agreementdatasets_codebook.pdf`](codebook/amc_agreementdatasets_codebook.pdf) (86 pages)

## Encoding

The CSV files use **latin-1** encoding (due to accented characters in treaty names). Always specify this when loading:

```python
df = pd.read_csv('amcdata_agreement_info_V2.csv', encoding='latin-1')
```

The one exception is `agreement_associations`, which uses **utf-8-sig** encoding:

```python
assoc = pd.read_csv('amcdata_agreement_associations_V2.csv', encoding='utf-8-sig')
```

In R, `read.csv()` handles the encoding automatically. In MATLAB, `readtable()` works without issues.

## Datasets

### `amcdata_agreement_info_V2.csv` (128 rows)

Core agreement metadata. One row per agreement.

**Key columns:**
- `agreement_id` - Unique identifier (use for joins)
- `title_short` - Short agreement name
- `title_full` - Full agreement name
- `year` - Year of agreement
- `adoption_date`, `entry_into_force_date` - Key dates
- `laterality` - Bilateral (1) vs. multilateral (2)
- `nr_signatory_states` - Number of signatories
- `nr_states_parties_total` - Total state parties
- `nr_states_parties_ratification` - Ratified parties
- `nr_states_parties_accession` - Acceded parties
- `status` - Agreement status
- `consultation_mechanism` - Consultation present (binary)
- `demonstrated_compliance_mechanism` - Demonstrated compliance present (binary)
- `demonstrated_compliance_mechanism_nr` - Count of demonstrated compliance mechanisms
- `verified_compliance_mechanism` - Verified compliance present (binary)
- `verified_compliance_mechanism_nr` - Count of verified compliance mechanisms

### `amcdata_vercom_V2.csv` (99 rows)

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

### `amcdata_demcom_V2.csv` (136 rows)

Demonstrated compliance mechanisms. One row per mechanism.

**Key columns:**
- `agreement_id` - Link to agreement_info
- `demonstrated_compliance_mechanism_trigger_type` - Trigger type
- `demonstrated_compliance_mechanism_trigger_cyclical` - Cyclical trigger
- `demonstrated_compliance_mechanism_trigger_state_party_action` - State party trigger
- `demonstrated_compliance_mechanism_trigger_circumstance` - Circumstance trigger

### `amcdata_consultation_V2.csv` (159 rows)

Consultation mechanisms. One row per mechanism.

- `agreement_id` - Link to agreement_info

### `amcdata_weapons_facilities_V2.csv` (434 rows)

Weapons types, lifecycle restrictions, and categories. One row per weapon/facility item.

**Key columns:**
- `agreement_id` - Link to agreement_info
- `item_type` - Type of item (see codebook p.43 for codes)
- `item` - Weapon or item description (e.g., "Nuclear Weapons", "Small Arms and Light Weapons"). This is the main field for identifying what is regulated. Note: some values have trailing whitespace, so apply `.str.strip()` before matching
- `summary_category` - Binary flag: 0 = real item from the treaty text, 1 = summary category added by AMC for aggregation. Rows where `summary_category=1` have labels like "Summary Category A (Nuclear Weapons)" in the `item` field
- `ban_development`, `restriction_development` - Development phase
- `ban_production`, `restriction_production` - Production phase
- `ban_transfer`, `restriction_transfer` - Transfer phase

### `amcdata_agreement_associations_V2.csv` (137 rows)

Links between related agreements. Uses **utf-8-sig** encoding (see above).

- `agreement_id` - Source agreement
- Related agreement identifiers and association metadata

## Joining Datasets

All datasets share `agreement_id` as the linking variable. Note that `weapons_facilities` has multiple rows per agreement (up to ~50), so joins will be one-to-many.

Example in Python:

```python
import pandas as pd

info = pd.read_csv('amcdata_agreement_info_V2.csv', encoding='latin-1')
vercom = pd.read_csv('amcdata_vercom_V2.csv', encoding='latin-1')
weapons = pd.read_csv('amcdata_weapons_facilities_V2.csv', encoding='latin-1')

# Clean trailing whitespace in item names
weapons['item'] = weapons['item'].str.strip()

# Join verification mechanisms with agreement metadata
merged = vercom.merge(info[['agreement_id', 'title_short', 'year']],
                      on='agreement_id', how='left')

# To add weapon info per agreement, first aggregate (one row per agreement)
# since weapons_facilities has many rows per agreement
weapon_summary = (weapons.groupby('agreement_id')['item']
                  .apply(lambda x: ', '.join(x.dropna().unique()[:3]))
                  .reset_index()
                  .rename(columns={'item': 'weapon_types'}))
merged = merged.merge(weapon_summary, on='agreement_id', how='left')
```

## Data Access

This data is shared for AMC Research Sprint participants only. Do not redistribute without permission from the Alva Myrdal Centre for Nuclear Disarmament, Uppsala University.
