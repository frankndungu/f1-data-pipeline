import pandas as pd
import json

# Load raw data
df = pd.read_csv("raw_data/f1_race_results_2025.csv")

# Clean column names
df.columns = df.columns.str.strip().str.title()

# Fill missing values
df["Points"] = df["Points"].fillna(0)
df["Position"] = pd.to_numeric(df["Position"], errors="coerce")

# Feature engineering
df["IsWin"] = df["Position"] == 1
df["IsPodium"] = df["Position"] <= 3

# Select final fields
cleaned_df = df[["Driver", "Team", "Race", "Points", "Position", "IsWin", "IsPodium"]]

# Convert DataFrame to a list of dicts
records = cleaned_df.to_dict(orient="records")

# Save cleaned data to JSON
with open("cleaned_data/f1_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=4)

print("✅ Data pipeline complete. Cleaned data saved to cleaned_data/f1_cleaned.json")
