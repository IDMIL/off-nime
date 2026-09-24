---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

# Off-NIME: NIME papers, chapters and books published outside of the NIME Conference Proceedings

## What is this resource?

This website contains a table of over 750 vetted off-NIME references deemed to be relevant to the NIME community. This includes materials from conferences that predated NIME (CMJ, ICMC; so-called ["prehistoric NIME"](https://nime.org/proceedings/2023/nime2023_8.pdf)) as well as concurrent conferences, publications, and books from 1969 to 2011. 

There are three primary datasets, represented by the radio buttons just above the table: CMJ, ICMC, and ISIDM ([the Interactive Systems and Instrument Design in Music Working Group](https://www.sensorwiki.org/isidm)). Of the datasets, ISIDM is the most incomplete. Almost all of the references do not have links, and there are ~60 citations (omitted from the table) that have no identifiable publication. If you would like to get involved with cleaning these references, or with adding new datasets/features, feel free to [submit a PR on the GitHub repo](https://github.com/IDMIL/off-nime/pulls).

Other features of this table include the search bar and column sorting (click the header to sort).

<head>
    <link rel="stylesheet" href="styles.css">
    <script src="scripts/num-entries.js" async></script>
    <script src="scripts/search-and-filter.js" async></script>
    <script src="scripts/sorttable.js" async></script>
    <script src="scripts/copy-bibtex.js" async></script>
</head>

<input type="text" id="table-search" onkeyup="searchTable(); setNumEntries();" placeholder="Search...">

<div id="table-tabs">
    <p>Datasets:</p>
    <input type="radio" id="html" name="table-tab" checked="checked" onclick="filterTable(''); setNumEntries();"><label for="html">All</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('Computer Music Journal'); setNumEntries();"><label for="html">CMJ</label>
    <input type="radio" id="html" name="table-tab" onclick="filterTable('International Computer Music Conference'); setNumEntries();"><label for="html">ICMC</label>
    <input type="radio" id="html" name="table-tab" onclick="notFilterTable(['Computer Music Journal', 'International Computer Music Conference']); setNumEntries();"><label for="html">ISIDM</label>
</div>

<div class="scrollableTable">
<table id="bibliography-table" class="sortable">
    <thead>
        <th>Year</th>
        <th>Author(s)</th>
        <th>Title</th>
        <th>Publication</th>
        <th>Pages</th>
        <th>URL</th>
        <th>BibTeX</th>
    </thead>
    {% bibliography %}
</table>
</div>

<div id="num-entries"></div>