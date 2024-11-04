# COVID-19 Vaccination Data Analysis

This project provides a detailed analysis of global COVID-19 vaccination data using Python, with visualizations illustrating vaccination distributions, progress over time for the top vaccinated countries, and correlations between key vaccination metrics.

## Table of Contents
- [Project Overview](#project-overview)
- [Data](#data)
- [Project Structure](#project-structure)
- [Visualizations](#visualizations)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project loads the latest COVID-19 vaccination data from [Our World in Data](https://github.com/owid/covid-19-data) and processes it to:
1. Visualize the distribution of full vaccination rates across countries.
2. Track vaccination progress over time for the top 5 fully vaccinated countries.
3. Generate a correlation heatmap of different vaccination metrics.

## Data
The dataset is sourced from [Our World in Data's COVID-19 data repository](https://github.com/owid/covid-19-data). The analysis excludes aggregated regions (e.g., "World", "High income") to focus solely on individual countries.

## Project Structure
- `vaccination_histogram.png`: Histogram of full vaccination rates across countries.
- `vaccination_timeline.png`: Timeline of vaccination progress for the top 5 fully vaccinated countries.
- `correlation_heatmap.png`: Correlation heatmap between key vaccination metrics.
- `covid_vaccination_analysis.py`: Python script containing data processing, analysis, and visualization.

## Visualizations
1. **Vaccination Rate Histogram**: Shows the distribution of fully vaccinated individuals per 100 people across countries.
2. **Vaccination Timeline for Top 5 Countries**: Tracks vaccination progress over time for the top 5 fully vaccinated countries.
3. **Correlation Heatmap**: Visualizes correlations between various vaccination metrics, such as total vaccinations and booster doses.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kallubhavijyothi/COVID-19-Vaccination-Progress-Analysis
   cd COVID-19-Vaccination-Progress-Analysis
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy seaborn matplotlib
   ```

## Usage
Run the script to load, process, and visualize the data:
```bash
python covid_vaccination_analysis.py
```
The output images will be saved in the current directory, and basic statistics for full vaccination rates will be printed in the console.

## Contributing
Contributions are welcome! Please feel free to submit issues or pull requests to improve this project.

## License
This project is licensed under the MIT License.

---
