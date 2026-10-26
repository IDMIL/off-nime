# Off-NIME NIME Papers
Website for NIME papers, chapters and books published outside of the NIME Conference Proceedings

See the website here: [https://idmil.github.io/off-nime](https://idmil.github.io/off-nime)

## What is this?

This repo contains BibTeX bibliography entries for New Interfaces for Musical Expression (NIME) papers that were published outside of NIME. This includes materials that were published before NIME existed as well as concurrent submissions. 

All of the raw .bib files can be found in `./bibs`.  There are three main datasets: (1) [Computer Music Journal (CMJ)](https://www.computermusicjournal.org/), (2) [International Computer Music Conference (ICMC)](https://quod.lib.umich.edu/i/icmc/), and (3) [Interactive Systems and Instrument Design in Music Working Group (ISIDM)](https://www.sensorwiki.org/isidm). All of the entries were deemed relevant to researchers in music interface design across a plurality of areas.

If you would like to get involved with cleaning any references, or with adding new datasets/features, see below.

## How to Contribute

### Adding Publications

Adding publications to this website is simple:

* Clone this repo and make a new local branch (`git checkout -B [branch-name]`)
  * `[branch-name]` can be anything, but we suggest something descriptive of the change in kebab case (e.g., `new-icmc-post-2020`)
* Save your citations as a `.bib` file
* Navigate to `bibs/` and add your `.bib` file here
  * For changes to existing datasets, put the file in the corresponding folder (e.g., ICMC citations go in `bibs/ICMC/`).
  * For new datasets, make a new folder or put it in `bibs/Extras/`. You may want to add a radio button for the new dataset on the website with some filtering operations; see examples in `index.md` and "Changing the Website" below.
  * If you need to do some data cleaning on your `.bib` first, the convention in this repo is to make a `scripts/` subfolder in the dataset folder and run scripts from there. We mark any intermediate `.bib`s as `.bib.skip` to prevent the BibTeX parser from trying to parse them.
* Navigate back to the repo root, `git add ./`, `git commit -m "[message]"` (make the message useful and human-readable), and `git push`
* [Make a PR on the GitHub](https://github.com/IDMIL/off-nime/pulls) to merge your new feature branch with `main`

Any changes that unnecessarily bloat the size of the repo will be rejected. This includes uploading PDFs to `pdfs/` which we use exclusively for certain references that have no stable link. We do not intend to deal with copyright issues. **THIS IS A WEBSITE, NOT A HARD DRIVE!**

### Changing the Website

The website is a static [Jekyll](https://jekyllrb.com/) website hosted using [GitHub Pages](https://docs.github.com/en/pages). The website is auto-redeployed by any commit to the `main` branch. 

You can run the website locally by cloning this repo, navigating to it, and running `bundle exec jekyll serve`. You will need to install [Ruby](https://www.ruby-lang.org/en/documentation/installation/) for your system.

Important files:

* `_config.yml`: Some basic config settings for Jekyll
* `index.md`: The website itself (mix of Markdown, HTML, Liquid, and JavaScript)
* `scripts/`: All JavaScript scripts running on the website
* `_layouts/bibliography_table_row.html`: HTML file that controls how each row of the bib table renders
* `styles.css`: Some CSS overrides for specific HTML elements on the site

For information on how to make a PR, the instructions are generally the same as in "Adding Publications" above.

*We generally like this page staying static; however, we are open to other frameworks such as [React](https://react.dev/). At a minimum, any massive changes to the website should (a) have a corresponding branch and PR, (b) run locally with no visible bugs or issues, and (c) include detailed instructions on how to host the site both locally and online. Members of the IDMIL will perform a detailed review of the PR and accept it **if and only if** there is consensus on the changes and all breaking changes are addressed.*

### Bugs

If you find any bugs, please feel free to raise a [GitHub Issue](https://github.com/IDMIL/off-nime/issues). We will also accept PRs for bugs.

## Acknowledgements

This project was created at [McGill University's Input Devices and Music Interaction Laboratory (IDMIL)](https://idmil.org) under the supervision of Marcelo Wanderley. 

The initial contributors to this repo include João Tragtenberg, Kasey Pocius, and Maxwell Gentili-Morin (see their work [here](https://github.com/IDMIL/off-nime/commit/9f644ab6e21e8bcea87916c635c7d87ff06a5939)). The latest changes, including the website and repo revamp, were headed by Wanderley, Gentili-Morin and [Ian Doherty](mailto:ian.doherty@mail.mcgill.ca).