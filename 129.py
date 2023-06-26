import csv
import pandas as pd 

df_merged = pd.read_csv("merged_data.csv")

columns = df_merged.columns
print("Columns:")
for column in columns:
    print(column)

columns_to_delete = ["Luminosity", "duplicate_column1", "duplicate_column2"]  
df_merged = df_merged.drop(columns=columns_to_delete)

df_merged = df_merged.dropna()
df_merged.to_csv("cleaned_merged_data.csv", index=False)
