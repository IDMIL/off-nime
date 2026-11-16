---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

# Off-NIME: NIME papers, chapters and books published outside of the NIME Conference Proceedings

## What is this resource?

This website contains a table of <span id="blurb-count"></span> vetted Off-NIME references deemed to be relevant to the NIME community. This includes materials from conferences that predated NIME (CMJ, ICMC; so-called ["prehistoric NIME"](https://nime.org/proceedings/2023/nime2023_8.pdf)) as well as concurrent conferences, publications, and books, currently from around <span id="min-year"></span> to <span id="max-year"></span>. 

There are several datasets, selectable in the dropdown above the table: 

1. [Computer Music Journal (CMJ)](https://www.computermusicjournal.org/)
2. [International Computer Music Conference (ICMC)](https://quod.lib.umich.edu/i/icmc/)
3. [Interactive Systems and Instrument Design in Music Working Group (ISIDM)](https://www.sensorwiki.org/isidm) 
4. From-NIME: NIME-cited works, including [Alexander Jensenius' recursive NIME search in his NIME Literature Atlas](https://alexarje.github.io/off-nime/atlas/)
5. Extras: Various other works, including Marcelo Wanderley's papers and specific requests

If you would like to get involved with cleaning any references, or with adding new datasets/features, check out [README.md in the GitHub repo](https://github.com/IDMIL/off-nime).

Other features of this table include the search bar, column sorting (click the header to sort), and the download all button below.

<head>
    <link rel="stylesheet" href="styles.css">
    <script src="scripts/min-max-year.js" async></script>
    <script src="scripts/num-entries.js" async></script>
    <script src="scripts/search-and-filter.js" async></script>
    <script src="scripts/sorttable.js" async></script>
    <script src="scripts/copy-bibtex.js" async></script>
    <script src="https://cdn.jsdelivr.net/npm/minisearch@7.2.0/dist/umd/index.min.js" async></script>
</head>

<button id="download-all-button" onclick="downloadAll()">Click here to download all entries as a single BibTeX file</button>

<input type="text" id="table-search" onkeyup="searchTable();" placeholder="Search...">

<label for="html">Dataset:</label>
<select>
    <option onclick="filterTable('')">All</option>
    <option onclick="filterTable('CMJ')">CMJ</option>
    <option onclick="filterTable('ICMC')">ICMC</option>
    <option onclick="filterTable('ISIDM')">ISIDM</option>
    <option onclick="filterTable('From-NIME')">From-NIME</option>
    <option onclick="filterTable('Extras')">Extras</option>
</select>

<div class="scrollableTable">
<table id="bibliography-table" class="sortable">
    <thead>
        <th>Year</th>
        <th>Author(s)</th>
        <th>Title</th>
        <th>Type</th>
        <th>Publication</th>
        <th>URL</th>
        <th>BibTeX</th>
    </thead>
    {% bibliography %}
</table>
</div>

<div id="num-entries"></div>
