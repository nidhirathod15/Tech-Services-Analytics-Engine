import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:SQLiskilla2026@127.0.0.1:5432/tech_companies")


df = pd.read_csv("clean_companies.csv")

# Companies table
companies = df[['company', 'award', 'link', 'company_logo']].drop_duplicates()
companies.columns = ['company_name', 'award', 'website', 'logo_url']
companies.to_sql('companies', engine, if_exists='replace', index=False)

# Locations table
locations = df[['city', 'country']].drop_duplicates()
locations.to_sql('locations', engine, if_exists='replace', index=False)

# Services table
services = df[['service']].drop_duplicates()
services.columns = ['service_name']
services.to_sql('services', engine, if_exists='replace', index=False)

# Meta table
meta = df[['company', 'team_size_min', 'team_size_max', 'hourly_rate_min', 'hourly_rate_max', 'data_source']]
meta.columns = ['company_name', 'team_size_min', 'team_size_max', 'hourly_rate_min', 'hourly_rate_max', 'data_source']
meta.to_sql('company_meta', engine, if_exists='replace', index=False)

print("Data loaded successfully.")