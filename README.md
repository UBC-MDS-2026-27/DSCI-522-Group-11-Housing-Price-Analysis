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

## Report
 
The analysis report is available in HTML format and is hosted on GitHub Pages:
 
[View the rendered analysis report](https://ubc-mds-2026-27.github.io/DSCI-522-Group-11-Housing-Price-Analysis/)

## Usage
 
The analysis runs in a Docker container so that everyone uses the same software and package versions.
 
### Setup
 
Install [Git](https://git-scm.com/downloads) and [Docker Desktop](https://www.docker.com/products/docker-desktop/), then start Docker Desktop. On Windows, run the commands below in Git Bash. Clone this repository and enter its folder. Run all later commands from the root of the repository.
 
```bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-Group-11-Housing-Price-Analysis.git
cd DSCI-522-Group-11-Housing-Price-Analysis
```

The container also reads your Git settings. If `git config --global user.email` prints nothing, set your name and email before continuing.
 
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
### 1. Make an SSH key
 
If `~/.ssh/id_ed25519.pub` does not exist, create a key and press Enter at each question. Do not overwrite an existing key.
 
```bash
ssh-keygen -t ed25519
```
 
The container uses this key for SSH login. Without it, Docker creates a folder named `~/.ssh/id_ed25519.pub`, and SSH login fails until you delete that folder and create the key.

### 2. Download the image
 
```bash
docker compose pull
```
 
 ### 3. Render the report
 
```bash
docker compose run --rm analysis-env uv run quarto render analysis/ames_analysis.qmd
```
 
With the `--rm` option, the container is removed automatically when rendering finishes. Open `analysis/ames_analysis.html` in your browser to read the new report.



## Dependencies

The project uses Python 3.14 and the following tools and libraries:
- **Git** - Run analysis
- **Dockerfile** - How project image is built 
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

Generative AI tools, including ChatGPT and Claude, were used to support brainstorming, understanding regression analysis concepts, reviewing project work, and proofreading documentation.

Examples of prompts used include:

- "What are some interesting questions we could explore using housing price data?"
- "What assumptions should we consider when using linear regression?"
- "Review the regression analysis approach and suggest possible improvements."

AI-generated suggestions were reviewed and evaluated by team members. Final decisions regarding the analysis, interpretation, and documentation were made by the team.


## Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations.

## References

- De Cock, D. (2011). Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. *Journal of Statistics Education, 19*(3), 1–15. <https://doi.org/10.1080/10691898.2011.11889627>
- Harrison, D., & Rubinfeld, D. L. (1978). Hedonic housing prices and the demand for clean air. *Journal of Environmental Economics and Management, 5*(1), 81–102. <https://doi.org/10.1016/0095-0696(78)90006-2>
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer.
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- Rosen, S. (1974). Hedonic prices and implicit markets: Product differentiation in pure competition. *Journal of Political Economy, 82*(1), 34–55. <https://doi.org/10.1086/260169>
- Sirmans, G. S., Macpherson, D. A., & Zietz, E. N. (2005). The composition of hedonic pricing models. *Journal of Real Estate Literature, 13*(1), 3–43.
- VanderPlas, J., Granger, B., Heer, J., Moritz, D., Wongsuphasawat, K., Satyanarayan, A., … Sievert, S. (2018). Altair: Interactive statistical visualizations for Python. *Journal of Open Source Software, 3*(32), 1057. <https://doi.org/10.21105/joss.01057>

## Attribution

The structure of this README was adapted from the course's [Breast Cancer Predictor example README](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/blob/1.0.0/README.md).


