# Contributing to the Housing Price Analysis

This document explains how anyone, including people outside the core team, can
report a bug, suggest a change, and submit their own work to the Housing Price
project. In short: open an issue, make a branch, and open a pull request.

### Reporting a bug

1. Search the existing [issues](https://github.com/UBC-MDS-2026-27/DSCI-522-Group-11-Housing-Price-Analysis/issues)
   to check that the bug has not already been reported.
2. If it has not, open a new issue and describe what you expected to happen and
   what happened instead.
3. Include a minimal [reprex](https://www.tidyverse.org/help/#reprex): the
   smallest piece of code and data that reproduces the problem, along with your
   operating system and the output of `uv pip list` (or the relevant package
   versions).

### Suggesting a change

Open an issue describing the change you would like to see, why it would improve
the project, and (if you can) how you would approach it. Wait for a team member
to agree before starting any substantial work, so that your effort is not wasted.

### Fixing typos

Small typos or grammatical errors in documentation may be edited directly using
the GitHub web interface, so long as the changes are made in the _source_ file.

*  YES: you edit the Quarto source file `analysis/ames_analysis.qmd`.
*  NO: you edit the rendered `analysis/ames_analysis.html`, `.pdf`, or `docs/index.html`.

### Prerequisites

Before you make a substantial pull request, you should always file an issue and
make sure someone from the team agrees that it's a problem. If you've found a
bug, create an associated issue and illustrate the bug with a minimal
[reprex](https://www.tidyverse.org/help/#reprex).

## Setting Up the Project
All work happens in the project's Docker container. You connect to it from Positron over SSH.
 
### Before your first connection
First follow the [Usage section of the README](README.md#usage) to install Docker, clone the repository, create an SSH key, set your Git details, and render the report. Use the email of your GitHub account for Git. Then:
 
1. Install [Positron](https://positron.posit.co/). Remote SSH is built in.
2. From the project folder, run `docker compose pull`.
 
### Each time you work
1. With Docker Desktop running, start the container from the project folder. `analysis-env` should be listed as running.
```bash
docker compose up -d
docker compose ps
```
2. In Positron, open the Command Palette (`Cmd+Shift+P` on Mac, `Ctrl+Shift+P` on Windows).
3. Run **Remote SSH: Show Remote Menu**, choose **Connect to Host**, and enter `root@localhost:2222`. If asked, choose **Linux**.
4. Choose **Open Folder** and enter `/workspace`.
5. Open the interpreter button at the top right, choose **New Console Session**, and select the Python at `/opt/venv/bin/python`. Do not use `/workspace/.venv`. To check, run this in the Console. It should print `/opt/venv/bin/python`.
```python
import sys; print(sys.executable)
```
6. Render the report in Positron's terminal:
```bash
cd /workspace
uv run quarto render analysis/ames_analysis.qmd
```
7. When finished, close the Positron remote window. Then run `docker compose down` on your computer.

### Connection problems
- **The container exits, or `~/.ssh/id_ed25519.pub` or `~/.gitconfig` is a folder:** run `docker compose down`, remove the empty folder with `rmdir`, then create the key or set your Git details as above.
- **Remote host identification has changed** after the image changes: run `ssh-keygen -R "[localhost]:2222"` and reconnect.
- **It asks for a password:** check that your key is named `id_ed25519.pub`, or change the key path in `docker-compose.yml`.
- **GitHub asks you to sign in when you push from the container:** sign in once in the browser window Positron opens.
- **A Linux computer refuses the key:** remove the `#` from the `StrictModes no` line in the `Dockerfile`, if present, through a pull request so the workflow publishes a new image.
- **Port 2222 is in use:** change the first `2222` in `docker-compose.yml` to another number and connect to that port. Do not commit this local change.

To render the report without opening the container in Positron, run this on your computer from the project folder:
```bash
docker compose run --rm analysis-env uv run quarto render analysis/ames_analysis.qmd
```
 
## Adding or Updating a Package
1. Create a branch from an up-to-date `main`, then start and connect to the container.
2. In the container, from `/workspace`, run `uv add <package>==<version>`. Check that `pyproject.toml` pins it with `==`.
3. Commit `pyproject.toml` and `uv.lock` together, then push the branch.
4. Wait for GitHub Actions to publish a new image and commit its tag to `docker-compose.yml` on your branch.
5. Close Positron. On your computer, run `git pull`, `docker compose pull`, and `docker compose up -d`. Reconnect and render the report.
6. Merge through a reviewed pull request. The merge builds the image again.
7. When that run finishes, everyone runs `git switch main`, `git pull`, and `docker compose pull`.
## Publishing the Report
After any change to the report, render it in the container, then run these from `/workspace`:
```bash
mkdir -p docs
cp analysis/ames_analysis.html docs/index.html
touch docs/.nojekyll
```
Commit the updated `docs/` files in your pull request. GitHub Pages serves them from the `/docs` folder on `main`.
 

## Pull request process

*  Create a new Git branch for each pull request (PR), starting from an
   up-to-date `main`. Do not commit directly to `main`.
*  Give the branch a short name that describes the work,
   for example `fix-readme-typo` or `add-eda-figure`.
*  Keep each branch small: one independent piece of work per branch.
*  Before opening the PR, render the report in the container to check that the analysis still runs from start to finish. On your computer, run `docker compose run --rm analysis-env uv run quarto render analysis/ames_analysis.qmd`.
   to check that the analysis still runs from start to finish.
*  Open a PR into `main` and describe what changed and why.
   Link the related issue (e.g., "Closes #12").
*  At least one other team member must review and approve the PR before it is merged.
   The reviewer, not the author, merges it.
*  New code should follow the PEP8 [style guide](https://peps.python.org/pep-0008/).

## AI policy

Generative AI tools (e.g., ChatGPT, GitHub Copilot, Claude) may be used when
contributing to this project, under the following rules.

**What is allowed**

*  Using AI tools to help you brainstorm, explain code or errors, draft or
   refactor code, and improve the wording of documentation.
*  Using AI-generated text or code in your contribution, provided you have read,
   understood, and tested it, and can explain and defend every line.

**What is not allowed**

*  Opening, commenting on, reviewing, approving, or merging issues and pull
   requests using an AI agent or any automated tool acting on your behalf.
   Issues and pull requests are opened, reviewed, and merged by people.
*  Submitting AI output you have not verified, including code that has not been
   run, results you have not checked, or references you have not confirmed exist.
*  Pasting private or sensitive data (credentials, tokens, personal information)
   into an AI tool.

**What you must disclose**

*  State in your pull request description which AI tool(s) you used and what you
   used them for (for example, "Claude was used to draft the docstrings in
   `src/clean.py`").
*  Mark substantial AI-generated passages of code or text in the pull request so
   reviewers know where to look more carefully.

**Who is responsible**

The contributor is fully responsible for everything they submit, whether or not
an AI tool helped produce it. This includes correctness, licensing, style, and
the accuracy of the analysis and its interpretation. Reviewers may ask you to
explain your changes and may close contributions that appear to be unreviewed
AI output.

## Code of Conduct

Please note that this project is released with a [Contributor Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.

## Attribution

These contributing guidelines were adapted from the [dplyr contributing guidelines](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md).

Parts of this guide were also adapted from the course's Breast Cancer Predictor example contributing guide, available in the [example repository](https://github.com/UBC-MDS/DSCI_522_project-template-breast-cancer-predictor/tree/1.0.0).

The AI policy was written with reference to the AI policies of
[earthaccess](https://earthaccess.readthedocs.io/en/latest/contributor/ai-policy/),
[SciPy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html), and
[SymPy](https://docs.sympy.org/dev/contributing/ai-generated-code-policy.html).

