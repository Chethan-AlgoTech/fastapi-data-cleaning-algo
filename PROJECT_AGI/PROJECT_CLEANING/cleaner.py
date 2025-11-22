import pandas as pd

df = pd.read_csv('messy_data.csv')

print("--- ORIGINAL MESSY DATA ---")
print(df)

df_clean = df.dropna()

df_clean = df_clean.drop_duplicates(subset=['Name', 'Price', 'Category'])

print("\n--- CLEANED DATA ---")
print(df_clean)

df_clean.to_csv('clean_data.csv', index=False)
print("\nSuccess! Saved to 'clean_data.csv'")