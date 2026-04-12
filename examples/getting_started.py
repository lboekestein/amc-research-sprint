"""
AMC Research Sprint - Getting Started
======================================
Load the AMC datasets, explore their structure, and run a basic analysis.

Requirements: pandas, matplotlib
    pip install pandas matplotlib

Note: The CSVs use latin-1 encoding. Always pass encoding='latin-1' to read_csv().
The agreement_associations file uses utf-8-sig encoding (it has a BOM header).
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# --- Load datasets ---
data_dir = Path(__file__).parent.parent / "data"

info = pd.read_csv(data_dir / "amcdata_agreement_info_V2.csv", encoding='latin-1')
vercom = pd.read_csv(data_dir / "amcdata_vercom_V2.csv", encoding='latin-1')
demcom = pd.read_csv(data_dir / "amcdata_demcom_V2.csv", encoding='latin-1')
consultation = pd.read_csv(data_dir / "amcdata_consultation_V2.csv", encoding='latin-1')
weapons = pd.read_csv(data_dir / "amcdata_weapons_facilities_V2.csv", encoding='latin-1')

print("=== Dataset sizes ===")
print(f"Agreement info:    {len(info)} agreements")
print(f"Verified compl.:   {len(vercom)} mechanisms")
print(f"Demonstrated compl.: {len(demcom)} mechanisms")
print(f"Consultation:      {len(consultation)} mechanisms")
print(f"Weapons/facilities: {len(weapons)} items")
print()

# --- Explore agreement_info ---
print("=== Compliance mechanism prevalence ===")
for col in ['consultation_mechanism', 'demonstrated_compliance_mechanism',
            'verified_compliance_mechanism']:
    count = info[col].sum()
    print(f"  {col}: {count}/{len(info)} agreements ({count/len(info)*100:.0f}%)")
print()

# --- Example: Compliance architecture over time ---
print("=== Example analysis: Compliance by decade ===")
info['decade'] = (info['year'] // 10) * 10
decade_summary = info.groupby('decade').agg({
    'consultation_mechanism': 'mean',
    'demonstrated_compliance_mechanism': 'mean',
    'verified_compliance_mechanism': 'mean',
    'agreement_id': 'count'
}).rename(columns={'agreement_id': 'n_agreements'})
print(decade_summary.round(2))
print()

# --- Example: Weapon items in dataset ---
# Note: summary_category is a binary flag (0 = real item, 1 = summary category
# added by AMC for aggregation). The actual weapon descriptions are in the
# 'item' column. Strip trailing whitespace before doing string matching.
weapons['item'] = weapons['item'].str.strip()

print("=== Weapon items (top 15 most common) ===")
print(weapons['item'].value_counts().head(15))
print()

# --- Example: Join datasets ---
print("=== Example join: Verification mechanisms with agreement metadata ===")
merged = vercom.merge(info[['agreement_id', 'title_short', 'year']],
                      on='agreement_id', how='left')
print(f"Merged dataset: {len(merged)} rows")
print(merged[['title_short', 'year',
              'verified_compliance_mechanism_type']].head(10))
print()

# --- Plot: Agreements over time ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Timeline of agreements
info.groupby('year')['agreement_id'].count().plot(
    kind='bar', ax=axes[0], color='steelblue', alpha=0.7)
axes[0].set_title('Arms Control Agreements by Year')
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Number of Agreements')
axes[0].tick_params(axis='x', rotation=45)

# Compliance mechanisms by decade
decade_summary[['consultation_mechanism', 'demonstrated_compliance_mechanism',
                'verified_compliance_mechanism']].plot(
    kind='bar', ax=axes[1], color=['#2ecc71', '#3498db', '#e74c3c'], alpha=0.7)
axes[1].set_title('Compliance Mechanism Prevalence by Decade')
axes[1].set_xlabel('Decade')
axes[1].set_ylabel('Proportion of Agreements')
axes[1].legend(['Consultation', 'Demonstrated', 'Verified'], loc='upper left')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('overview_plots.png', dpi=150, bbox_inches='tight')
print("Saved: overview_plots.png")
