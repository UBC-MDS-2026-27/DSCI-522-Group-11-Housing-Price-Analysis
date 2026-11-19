# Housing Price Analysis in Ames, Iowa

**DSCI 522 – Data Science Workflows | Group 11 | University of British Columbia**

## Project Overview

Housing prices are influenced by various property characteristics, including size, age, and overall quality. This project investigates how these factors are associated with residential sale prices in Ames, Iowa.

Using the Ames Housing dataset, we perform exploratory data analysis and develop a multiple linear regression model to understand the relationships between housing characteristics and sale prices.

## Research Question

**How are living area, house age, and overall quality associated with residential sale prices in Ames, Iowa?**

The analysis focuses on three explanatory variables:

- **Living area:** Above-ground living space measured in square feet.
- **House age:** Age of the property, calculated from its year of construction.
- **Overall quality:** Rating of the property's materials and finishes on a scale of 1–10.

Our target variable is the property's sale price in US dollars.

## Dataset

We use the **Ames Housing dataset**, which contains information on 2,930 residential properties sold in Ames, Iowa, between 2006 and 2010.

**Source:** De Cock, D. (2011). *Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project.*

[Original dataset](https://jse.amstat.org/v19n3/decock/AmesHousing.txt)

The dataset contains property characteristics such as living area, year built, overall quality, and sale price.

## Methodology

Our analysis follows these steps:

1. **Data collection:** Obtain the Ames Housing dataset.
2. **Data cleaning:** Select and prepare the relevant housing characteristics.
3. **Exploratory data analysis:** Visualize relationships between housing features and sale prices.
4. **Model development:** Fit a multiple linear regression model and compare it against a baseline model.
5. **Model evaluation:** Evaluate model performance using RMSE, R², and MAE.

We use an 80/20 training-test split and five-fold cross-validation to assess model performance.

## Project Structure

```text
.
├── analysis/
│   ├── ames_analysis.qmd
│   └── ames_analysis.html
├── data/
│   ├── raw/
│   └── processed/
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── pyproject.toml
└── uv.lock
```

## How to Run the Analysis

### 1. Clone the repository

```bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-Group-11-Housing-Price-Analysis.git

cd DSCI-522-Group-11-Housing-Price-Analysis
```

### 2. Set up the Python environment

The project uses Python 3.14 and `uv` for dependency management.

```bash
uv sync
```

### 3. Run the analysis

To execute the Quarto analysis and regenerate the HTML report:

```bash
cd analysis
uv run quarto render ames_analysis.qmd
```

This command requires Quarto to be installed and available on your system.

Alternatively, view the existing report at [`analysis/ames_analysis.html`](analysis/ames_analysis.html).

## Tools and Technologies

- Python
- pandas
- scikit-learn
- Altair
- Quarto
- Git and GitHub
- uv

## Contributors

This project was developed by **Group 11**, UBC Master of Data Science (2026–2027).

- Atinuke Wole-Ilori
- Nikita Wadnikop
- Paromita Sengupta
- Xiangtian Ji

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for expected community standards.

## License

The analysis report is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license.

See [LICENSE.md](LICENSE.md) for details.