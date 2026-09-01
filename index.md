---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

# Off-NIME: NIME papers, chapters and books published outside of the NIME Conference Proceedings

## How to use this resource

A table of Off-NIME materials has been provided below. The URL column links to a stable host of the material, and the BibTeX column allows you to copy the citation as a BibTeX .bib file. 

You can search for specific items using the search box, and you can also sort the table by clicking on any of the headers.

<head>
    <link rel="stylesheet" href="styles.css">
    <script src="scripts/num-entries.js" async></script>
    <script src="scripts/search-and-filter.js" async></script>
    <script src="scripts/sorttable.js" async></script>
    <script src="scripts/copy-bibtex.js" async></script>
</head>

<input type="text" id="table-search" onkeyup="tableSearch(); setNumEntries();" placeholder="Search...">

<div id="table-tabs">
    <p>Datasets:</p>
    <input type="radio" id="html" name="table-tab" checked="checked" onclick="tableFilter(''); setNumEntries();"><label for="html">All</label>
    <input type="radio" id="html" name="table-tab" onclick="tableFilter('Computer Music Journal'); setNumEntries();"><label for="html">CMJ</label>
    <input type="radio" id="html" name="table-tab" onclick="tableFilter('Proceedings of the International Computer Music Conference'); setNumEntries();"><label for="html">ICMC</label>
    <input type="radio" id="html" name="table-tab" onclick="tableNotFilter(['Computer Music Journal', 'Proceedings of the International Computer Music Conference']); setNumEntries();"><label for="html">ISIDM</label>
</div>

<div class="scrollableTable">
<table id="bibliography-table" class="sortable">
    <thead>
        <th>Year</th>
        <th>Journal</th>
        <th>Author(s)</th>
        <th>Title</th>
        <th>Pages</th>
        <th>URL</th>
        <th>BibTeX</th>
    </thead>
    {% bibliography %}
</table>
</div>

<div id="num-entries"></div>