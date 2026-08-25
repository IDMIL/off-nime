# Off-NIME NIME Papers
Website for NIME papers, chapters and books published outside of the NIME Conference Proceedings

See a pretty table of entries here: [https://idmil.github.io/off-nime](https://idmil.github.io/off-nime)

## What is this?

This repo contains BibTeX entries for New Interfaces for Musical Expression (NIME) papers that were published outside of NIME. This includes papers that were published before NIME existed as well as concurrent submissions. 

All of the raw .bib files can be found in `./bibs`, grouped by year.  There are three main datasets: (1) [Computer Music Journal (CMJ)](https://www.computermusicjournal.org/), (2) [International Computer Music Conference (ICMC)](https://quod.lib.umich.edu/i/icmc/), and (3) [Interactive Systems and Instrument Design in Music Working Group (ISIDM)](https://www.sensorwiki.org/isidm). All of the entries were hand-picked and were deemed relevant to researchers in music interface design across a plurality of areas.

## Progress

*Disclaimer:* This project is still a work-in-progress. Please excuse any bugs on the website, incomplete entries, or missing data.

✅ **Website:** Created using Jekyll and GitHub Actions

✅ **Table:** Created using [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar) and [sorttable](www.kryogenix.org/code/browser/sorttable/)

✅ **CMJ .bib files:** Carried over from previous repo (see commit [here](https://github.com/IDMIL/off-nime/commit/9f644ab6e21e8bcea87916c635c7d87ff06a5939))

✅ **ICMC .bib files:** Carried over and supplemented from previous repo (see `bibs/ICMC/parser.py`)

❌ **ISIDM .bib files:** In progress. Currently dealing with data correction, duplicate removal, and normalization. (See `bibs/ISIDM/citations-[x].txt`.)

❌ **Dataset tabs** In progress.

## Acknowledgements

This project was created at McGill University's Input Devices and Music Interaction Laboratory (IDMIL) under the supervision of Marcelo Wanderley. 

The initial contributors to this repo include João Tragtenberg and Kasey Pocius (see their work [here](https://github.com/IDMIL/off-nime/commit/9f644ab6e21e8bcea87916c635c7d87ff06a5939)). The latest changes, including the website and repo revamp, were headed by Wanderley and [Ian Doherty](mailto:ian.doherty@mail.mcgill.ca).