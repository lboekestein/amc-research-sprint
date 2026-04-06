"""
AMC Research Sprint - Getting Started
======================================
Load the AMC datasets, explore their structure, and run a basic analysis.

Requirements: pandas, matplotlib
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --- Load datasets ---
data_dir = Path(__file__).parent.parent / "data"

info = pd.read_csv(data_dir / "amcdata_agreement_info_V2.csv")
vercom = pd.read_csv(data_dir / "amcdata_vercom_V2.csv")
demcom = pd.read_csv(data_dir / "amcdata_demcom_V2.csv")
consultation = pd.read_csv(data_dir / "amcdata_consultation_V2.csv")
weapons = pd.read_csv(data_dir / "amcdata_weapons_facilities_V2.csv")

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

# --- Example: Weapon categories ---
print("=== Weapon categories in dataset ===")
print(weapons['summary_category'].value_counts())
print()

# --- Example: Join datasets ---
print("=== Example join: Verification mechanisms with weapon categories ===")
merged = vercom.merge(info[['agreement_id', 'agreement_name', 'year']],
                      on='agreement_id', how='left')
# Get unique weapon categories per agreement
weapon_cats = weapons.groupby('agreement_id')['summary_category'].first().reset_index()
merged = merged.merge(weapon_cats, on='agreement_id', how='left')
print(f"Merged dataset: {len(merged)} rows")
print(merged[['agreement_name', 'year', 'summary_category',
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
plt.show()
print("Saved: overview_plots.png")
