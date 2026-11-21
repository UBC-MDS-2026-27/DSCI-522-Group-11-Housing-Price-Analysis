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
*  NO: you edit the rendered `analysis/ames_analysis.html` or `.pdf`.

### Prerequisites

Before you make a substantial pull request, you should always file an issue and
make sure someone from the team agrees that it's a problem. If you've found a
bug, create an associated issue and illustrate the bug with a minimal
[reprex](https://www.tidyverse.org/help/#reprex).

### Setting up the project

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and
[Quarto](https://quarto.org/docs/get-started/), then clone the repository and
create the virtual environment from the root of the repository:

``` bash
git clone https://github.com/UBC-MDS-2026-27/DSCI-522-Group-11-Housing-Price-Analysis.git
cd DSCI-522-Group-11-Housing-Price-Analysis
uv sync
```

To re-run the analysis and render the report:

``` bash
uv run quarto render
```

If your change needs a new Python package, add it with `uv add <package>`
(this pins an exact version in `pyproject.toml` and updates `uv.lock`),
and commit both files.

### Pull request process

*  Create a new Git branch for each pull request (PR), starting from an
   up-to-date `main`. Do not commit directly to `main`.
*  Give the branch a short name that describes the work,
   for example `fix-readme-typo` or `add-eda-figure`.
*  Keep each branch small: one independent piece of work per branch.
*  Before opening the PR, render the report (`uv run quarto render`)
   to check that the analysis still runs from start to finish.
*  Open a PR into `main` and describe what changed and why.
   Link the related issue (e.g., "Closes #12").
*  At least one other team member must review and approve the PR before it is merged.
   The reviewer, not the author, merges it.
*  New code should follow the PEP8 [style guide](https://peps.python.org/pep-0008/).

### AI policy

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

### Code of Conduct

Please note that this project is released with a [Contributor Code of
Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to
abide by its terms.

### Attribution

These contributing guidelines were adapted from the [dplyr contributing guidelines](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md).

The AI policy was written with reference to the AI policies of
[earthaccess](https://earthaccess.readthedocs.io/en/latest/contributor/ai-policy/),
[SciPy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html), and
[SymPy](https://docs.sympy.org/dev/contributing/ai-generated-code-policy.html).

