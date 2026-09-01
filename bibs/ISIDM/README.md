## ISIDM Citations

This folder contains a dataset of citations for the [Interactive Systems and Instrument Design in Music Working Group (ISIDM)](https://www.sensorwiki.org/isidm). These citations were acquired from the Bibliography section of each Main Topic page.

Due to issues with the citations, a multi-step citation cleaning process has been started. A walkthrough of how this data was obtained and cleaned is included below for future maintainers.

Contact Ian Doherty ([ian.doherty@mail.mcgill.ca](mailto:ian.doherty@mail.mcgill.ca)) if you have any questions. (A lot of this is definitely overengineered...)

### Some Notes

All of the scripts used for the cleaning process are Python (.py files). All intermediate .bib files are marked .bib.skip to prevent jekyll-scholar from trying to read them (though all of the scripts will output as .bib by default; make sure to manually rename them to .bib.skip if you run them). The final .bib that *is* read by jekyll-scholar is in `./final`.

### 1. Obtaining citations (`text/`)

The citations were manually copied from the [ISIDM website](https://www.sensorwiki.org/isidm) into two separate .txt files.

### 2. Converting citations to .bib (`text2bib/`)

The text files from the previous step were then piped into an online service called [text2bib](https://text2bib.org/). This website converts citations into BibTeX. 

Due to the citations being somewhat malformed, many of the citations from text2bib need to be further cleaned by hand.

### 3. Removing duplicates (`deduplicated/`)

Many of the ISIDM citations contain duplicates, both between bibliographies and with the CMJ/ICMC datasets in this repo. A script was written to remove these duplicates.

Duplicates are detected by [string similarity](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher), and those with a ratio above 0.7 are deemed to be duplicates.

### 4. Acquiring URLs (`get-links/`)

None of the ISIDM citations included links to stable hosts for the material. I found [a useful Stack Overflow post](https://tex.stackexchange.com/a/300474) that contains a script which scrapes the DOIs for BibTeX entries using an online third-party API. This got us the URLs for just under 300 citations, which is almost half of the dataset at this point. 

I wrote one more simple script to add a URL field to all of these entries that simply points to `doi.org/{doi}`, which gives us a stable link.

### 5. Next steps

We've reached what seems to be the limit of what can be cleaned automatically for these citations. The remaining >50% of citations need to be cleaned by hand. This means:

* Missing fields (at least: year, author, title, pages, and URL) need to be found and populated
* We need to agree on a format for titles and types (and probably write a script that handles *all* citations in the repo)
  * The current type suggestion has been Pascal case in the following format: first author last name, first word (not including conjunctions), year. For example, "The Example" by John Smith in 1980 would be "SmithExample1980". Mandating this is harder than it seems and has many edge cases, and it's probably not worth doing until the ISIDM dataset is actually complete.