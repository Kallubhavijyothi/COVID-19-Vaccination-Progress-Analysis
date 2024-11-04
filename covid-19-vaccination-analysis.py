import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'
df = pd.read_csv(url)

# Data cleaning and preprocessing
df['date'] = pd.to_datetime(df['date'])

# Get the latest data for each country
latest_data = df.sort_values('date').groupby('location').last().reset_index()

# Remove aggregated regions and focus on countries
excluded_locations = ['World', 'Upper middle income', 'Lower middle income', 'High income', 'Low income', 'European Union']
latest_data = latest_data[~latest_data['location'].isin(excluded_locations)]

# Create vaccination histogram
plt.figure(figsize=(12, 6))
plt.hist(latest_data['people_fully_vaccinated_per_hundred'].dropna(), 
         bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Full Vaccination Rates Across Countries')
plt.xlabel('People Fully Vaccinated per 100')
plt.ylabel('Number of Countries')
plt.grid(True, alpha=0.3)
plt.savefig('vaccination_histogram.png')
plt.show()
plt.close()
