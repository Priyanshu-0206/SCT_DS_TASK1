import zipfile
import pandas as pd
import matplotlib.pyplot as plt


zip_path = r"C:\Users\Priyanshu\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_81108.zip"

with zipfile.ZipFile(zip_path) as z:
    # List all files in the zip
    print(z.namelist())  # Shows all 3 files
    
    # Extract the main CSV you want
    with z.open('API_SP.POP.TOTL_DS2_en_csv_v2_81108.csv') as f:
        df = pd.read_csv(f, skiprows=4)  # skip metadata rows

print(df.head())


# Clean data: remove rows without 2023 data
df_clean = df[df['2023'].notna()]

# Bar Chart: Top 10 most populated countries in 2023
top10 = df_clean.sort_values(by='2023', ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.bar(top10['Country Name'], top10['2023'], color='teal')
plt.title('Top 10 Most Populated Countries in 2023')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histogram: Distribution of populations across all countries in 2023
plt.figure(figsize=(10,6))
plt.hist(df_clean['2023'], bins=30, color='orange', edgecolor='black')
plt.title('Histogram of Country Populations in 2023')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()
