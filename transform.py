import pandas as pd
import re

df = pd.read_csv("Tech Companies.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Drop index column
df = df.drop(columns=['index'], errors='ignore')

# Clean team size
def parse_team_size(value):
    if pd.isna(value):
        return None, None
    value = str(value)
    numbers = re.findall(r'\d+', value)
    if len(numbers) == 2:
        return int(numbers[0]), int(numbers[1])
    elif len(numbers) == 1:
        return int(numbers[0]), int(numbers[0])
    return None, None

df[['team_size_min', 'team_size_max']] = df['team_size'].apply(lambda x: pd.Series(parse_team_size(x)))

# Clean hourly charges
def parse_hourly(value):
    if pd.isna(value):
        return None, None
    value = str(value)
    numbers = re.findall(r'\d+', value)
    if len(numbers) == 2:
        return int(numbers[0]), int(numbers[1])
    elif len(numbers) == 1:
        return int(numbers[0]), int(numbers[0])
    return None, None

df[['hourly_rate_min', 'hourly_rate_max']] = df['hourly_charges'].apply(lambda x: pd.Series(parse_hourly(x)))

# Standardize text
df['company'] = df['company'].str.strip()
df['service'] = df['service'].str.strip()
df['city'] = df['city'].str.strip()
df['country'] = df['country'].str.strip()

print(df[['company', 'team_size_min', 'team_size_max', 'hourly_rate_min', 'hourly_rate_max']].head())

df.to_csv("clean_companies.csv", index=False)