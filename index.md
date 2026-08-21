---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

# Off-NIME: NIME papers, chapters and books published outside of the NIME Conference Proceedings

## How to use this resource

A table of Off-NIME materials has been provided below. The URL column links to a stable host of the material, and the BibTeX column allows you to download the citation as a BibTeX .bib file. 

You can search for specific items using the search box, and you can also sort the table by clicking on any of the headers.

<head>
    <link rel="stylesheet" href="styles.css">
    <script src="search.js" async></script>
    <script src="sorttable.js" async></script>
    <script src="download-bibtex.js" async></script>
</head>

<input type="text" id="table-search" onkeyup="tableSearch()" placeholder="Search...">


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