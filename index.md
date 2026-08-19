---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

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