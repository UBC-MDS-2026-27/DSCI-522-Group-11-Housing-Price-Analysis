# Housing Price Analysis in Ames, Iowa

**DSCI 522 – Data Science Workflows | Group 11 | UBC Master of Data Science (2026–2027)**

## Authors

- Atinuke Wole-Ilori
- Nikita Wadnikop
- Paromita Sengupta
- Xiangtian Ji

## Summary

This project investigates how living area, house age, and overall quality are associated with residential sale prices in Ames, Iowa. Using the Ames Housing dataset, we conducted exploratory data analysis and developed a multiple linear regression model to examine these relationships.

Our findings suggest that larger living areas and higher overall quality ratings are associated with higher sale prices, while older houses tend to have lower prices. Overall quality showed the strongest correlation with sale price. The regression model explained approximately 76% of the variation in sale prices on the test set, with an RMSE of approximately US$38,600.

These findings highlight the importance of property characteristics in understanding housing prices. However, the model does not account for other potentially important factors, such as neighborhood and location, and should not be used as a substitute for professional property valuation.

## How to Run the Analysis

Follow the steps below to reproduce the analysis and generate the report.

### 1. Clone the repository

```bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-Group-11-Housing-Price-Analysis.git
cd DSCI-522-Group-11-Housing-Price-Analysis
```

### 2. Install dependencies

Make sure Python 3.14, [uv](https://docs.astral.sh/uv/getting-started/installation/), and [Quarto](https://quarto.org/docs/get-started/) are installed.

Run the following command from the repository root to create the Python environment and install the required packages:

```bash
uv sync
```

### 3. Render the report

Navigate to the analysis directory:

```bash
cd analysis
```

Run the following command to render the Quarto report:

```bash
uv run quarto render ames_analysis.qmd
```

The rendered HTML report will be generated as `analysis/ames_analysis.html`.

## Dependencies

The project uses Python 3.14 and the following tools and libraries:

- **uv** – Python environment and dependency management
- **Quarto** – Report generation
- **pandas** – Data cleaning and manipulation
- **scikit-learn** – Regression modelling and evaluation
- **Altair** – Data visualization
- **Jupyter** – Python notebook execution

Python package dependencies are listed in [pyproject.toml](pyproject.toml), with versions resolved in [uv.lock](uv.lock).

## Licenses

This project uses two licenses:

- **MIT License:** For the software code.
- **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0):** For the analysis report.

See [LICENSE.md](LICENSE.md) for more information.

## Generative AI Use

Generative AI tools, including ChatGPT, were used to assist with drafting and improving project documentation, including the README.

Examples of prompts used include:

- "Help me write a README file for our housing price analysis project."
- "Organize the README according to the DSCI 522 assignment requirements."

AI-generated suggestions were reviewed before inclusion. Additional AI use by team members should be documented here, including any assistance with coding, debugging, or analysis.

No project-specific AI instruction files are identified here. Any such files used by the team should be committed and linked in this section.

## Rendered Report

The analysis report is available in HTML format:

[View the rendered analysis report](analysis/ames_analysis.html)

A public GitHub Pages URL can be added here once the report has been deployed.

## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.