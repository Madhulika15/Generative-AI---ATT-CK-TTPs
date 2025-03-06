# Load Excel Files
relationships_df = pd.read_excel("/content/enterprise-attack-v16.1-relationships.xlsx")
tactics_df = pd.read_excel("/content/enterprise-attack-v16.1-tactics.xlsx")
techniques_df = pd.read_excel("/content/enterprise-attack-v16.1-techniques.xlsx")

# Display Sample Data
print("Relationships Data:")
display(relationships_df.head())

print("\nTactics Data:")
display(tactics_df.head())

print("\nTechniques Data:")
display(techniques_df.head())
# Check column names and sample rows
print("Relationships Data Columns:", relationships_df.columns)
print("Tactics Data Columns:", tactics_df.columns)
print("Techniques Data Columns:", techniques_df.columns)

# Check for missing values
print("\nMissing Values in Relationships Data:\n", relationships_df.isnull().sum())
print("\nMissing Values in Tactics Data:\n", tactics_df.isnull().sum())
print("\nMissing Values in Techniques Data:\n", techniques_df.isnull().sum())


# Ensure columns are cleaned (lowercase, no spaces)
relationships_df.columns = relationships_df.columns.str.strip().str.lower()
tactics_df.columns = tactics_df.columns.str.strip().str.lower()
techniques_df.columns = techniques_df.columns.str.strip().str.lower()

# Merge techniques with relationships (source ID -> techniques ID)
merged_df = relationships_df.merge(
    techniques_df,
    left_on='source id',
    right_on='id',
    how='left'
)

# Merge tactics with previous result (target ID -> tactics ID)
merged_df = merged_df.merge(
    tactics_df,
    left_on='target id',
    right_on='id',
    how='left'
)

# Keep only useful columns for extraction
merged_df = merged_df[['source id', 'target id', 'source name', 'name_x', 'name_y']]
# Rename columns for clarity
merged_df.columns = ['Technique_ID', 'Tactic_ID', 'Source_Name', 'Technique', 'Tactic']

# Display merged data sample
print("\n Data Sample Merged:")
display(merged_df.head())
print("Missing Techniques:", merged_df['Technique'].isnull().sum())
print("Missing Tactics:", merged_df['Tactic'].isnull().sum())

merged_df.to_csv('/content/cleaned_attack_mapping.csv', index=False)

from google.colab import files
files.download('/content/cleaned_attack_mapping.csv')
import re

# Clean text function to normalize input
def clean_text(text):
    text = re.sub(r'http\S+|www\S+|[^A-Za-z0-9\s]', '', str(text))  # Ensure text is string and clean it
    return text.lower()

# Extract TTPs function
def extract_ttps(report, mapping_df):
    detected_ttps = []

    # Clean the report
    report = clean_text(report)

    # Iterate over mapping DataFrame
    for _, row in mapping_df.iterrows():
        # Ensure the row has a valid technique and tactic (skip NaN values)
        if pd.notna(row['technique']) and pd.notna(row['tactic']):
            if row['technique'] in report:
                detected_ttps.append((row['technique'], row['tactic']))

    return detected_ttps

# Sample Threat Report
sample_report = """
The attacker used spear-phishing emails to gain initial access. 
Later, they used PowerShell scripts to maintain persistence and evade defenses.
"""

# Detect TTPs
detected_ttps = extract_ttps(sample_report, merged_df)

# Output detected TTPs
print("\n TTPs Detected:")
if not detected_ttps:
    print("No TTPs detected.")
else:
    for technique, tactic in detected_ttps:
        print(f"Technique: {technique} | Tactic: {tactic}")

