---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

# Off-NIME: NIME papers, chapters and books published outside of the NIME Conference Proceedings

## What is this resource?

This website contains a table of <span id="blurb-count"></span> vetted Off-NIME references deemed to be relevant to the NIME community. This includes materials from conferences that predated NIME (CMJ, ICMC; so-called ["prehistoric NIME"](https://nime.org/proceedings/2023/nime2023_8.pdf)) as well as concurrent conferences, publications, and books, currently from around <span id="min-year"></span> to <span id="max-year"></span>. 

There are three primary datasets, represented by the radio buttons just above the table: CMJ, ICMC, and ISIDM ([the Interactive Systems and Instrument Design in Music Working Group](https://www.sensorwiki.org/isidm)). There is also the From-NIME dataset, which was created by performing a recursive NIME and Off-NIME paper citation search. This was headed by [Alexander Jensenius](https://www.arj.no/) in his [Off-NIME Atlas](https://alexarje.github.io/off-nime/atlas/). 

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

<input type="text" id="table-search" onkeyup="searchTable(); setNumEntries();" placeholder="Search...">

<div id="table-tabs">
    <p>Datasets:</p>
    <input type="radio" id="html" name="table-tab" checked="checked" onclick="filterTable(''); updateNumEntries();"><label for="html">All</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('CMJ'); updateNumEntries();"><label for="html">CMJ</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('ICMC'); updateNumEntries();"><label for="html">ICMC</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('ISIDM'); updateNumEntries();"><label for="html">ISIDM</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('From-NIME'); updateNumEntries();"><label for="html">From-NIME</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('Extras'); updateNumEntries();"><label for="html">Extras</label>    
</div>

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
