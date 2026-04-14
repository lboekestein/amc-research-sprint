# AMC Research Sprint - Team 1

### Challenge 2: Does Verification Deter Participation?

*Team members:* William Kelly, Luuk Boekestein & Eva Branchereau


### Overview of contents in this repository
- [`docs/`](docs/): Folder containing documentation for the analysis, including the [presentation output](docs/Presentation_April_14th.pdf) and a knitted pdf version of the [code and documentation](docs/Researchsprint_code.pdf). This folder is the core output of our Sprint results.
- [`Researchsprint_code.Rmd`](Researchsprint_code.Rmd): R Markdown file with the R code and documentation of the analysis that can be used to replicate all feature engineering, figures and regressioni results.
- [`data_cleaned/`](data_cleaned/): Folder containing cleaned datasets used for analysis. This data contains the _extended_verification_index_ variable that we constructed as part of our analysis, in combination with the original dataset.
- [`figs/`](figs/): Folder containing all figures generated during the analysis.


### Replication instructions

To replicate the analysis, install the necessary requirements using the following command in R:
```r
renv::restore()
```
And then run the code blocks in the `Researchsprint_code.Rmd` notebook to generate the verification intensity measure, the new dataset, figures and regression results.