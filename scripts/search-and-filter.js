let filterVisibleRows = [];

/**
 * Filters the bibliography table by a specific dataset
 * @param {string} query The dataset we are filtering by
 */
function filterTable(query) {
    const trs = document
        .getElementById("bibliography-table")
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");
    
    // Resets the list of the visible rows from the filter
    filterVisibleRows = [];
    let i = 0;

    // Filters have priority over searches, so we check all rows of the table
    for (const tr of trs) {
        const tds = tr.getElementsByTagName("td");

        // Checking the hidden dataset td (see _layouts/bibliography_table_row.html)
        if (query == "" || tds[tds.length - 1].textContent == query) {
            tr.style.display = "";

            filterVisibleRows.push({
                id: i,
                year: tds[0].textContent,
                authors: tds[2].textContent,
                title: tds[1].textContent,
                type: tds[3].textContent,
                publication: tds[4].textContent,
                htmlObject: tr
            });

            i++;
        }
        else {
            tr.style.display = "none";
        }
    }

    // If there's also an active search, re-initiate that
    if (document.getElementById("table-search").value != "") {
        searchTable();
    }
}

/**
 * Searches all cells of the bibliography table for a string
 * @note Uses https://github.com/lucaong/minisearch for fuzzy searching
 */
function searchTable() {
    // const searchTerm = document.getElementById("table-search").value.toUpperCase();

    // // We are only searching the subset of trs given to us from the active filter
    // for (const tr of filterVisibleRows) {
    //     let found = false;

    //     for (const td of tr.getElementsByTagName("td")) {
    //         if (td.textContent.toUpperCase().indexOf(searchTerm) > -1) {
    //             found = true;
    //             break;
    //         }
    //     }

    //     tr.style.display = (found ? "" : "none");
    // }

    const searchTerm = document.getElementById("table-search").value;

    if (searchTerm == "") {
        for (const filterVisibleRow of filterVisibleRows) {
            filterVisibleRow.htmlObject.style.display = "";
        }
        return;
    }

    for (const filterVisibleRow of filterVisibleRows) {
        filterVisibleRow.htmlObject.style.display = "none";
    }

    const miniSearch = new MiniSearch({
        fields: ['year', 'authors', 'title', 'type', 'publication'], 
        storeFields: ['htmlObject']
    });

    miniSearch.addAll(filterVisibleRows);
    let results = miniSearch.search(searchTerm);

    for (const result of results) {
        result.htmlObject.style.display = "";
    }

    updateNumEntries();
}

filterTable('');