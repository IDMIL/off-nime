## ISIDM Citations

This folder contains the cleaned ISIDM citation materials for the ISIDM dataset on the website. The final versions of the bibliography are in `final.bib` and `theses-tech-reports.bib`; all intermediate bibliographies used in-between the cleaning steps are ended with `.bib.skip`.

The citations were cleaned by (1) gathering the citations from [the ISIDM website](https://www.sensorwiki.org/isidm), (2) running them through Claude to generate BibTeX entries, and (3) removing any duplicates with the CMJ/ICMC datasets.

Before this latest cleaning process, a more involved cleaning process was attempted in `old/`. Some of the scripts could be useful in the future, so the directory was left where it is, but all of the `.bib.skip` files in there are most likely not useful.

If you would like to update any of the citations in ISIDM for any reason, please feel free! Just make a PR on the GitHub repo and we'll take a look at it.