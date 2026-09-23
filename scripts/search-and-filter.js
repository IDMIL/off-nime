let filterVisibleRows = [];

/**
 * Filters the bibliography table by a specific journal name
 * @param {string} filter A journal name to filter by
 */
function filterTable(filter) {
    const trs = document
        .getElementById("bibliography-table")
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");
    
    // Resets the list of the visible rows from the filter
    filterVisibleRows = [];

    // Filters have priority over searches, so we check all rows of the table
    for (const tr of trs) {
        let found = false;

        for (const td of tr.getElementsByTagName("td")) {
            if (td.innerText.toUpperCase().indexOf(filter.toUpperCase()) != -1) {
                found = true;
                break;
            }
        }

        if (found) {
            tr.style.display = "";
            filterVisibleRows.push(tr);
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
 * Filters the bibliography table by a list of journals that should *not* match
 * @param {string[]} notFilters A list of journals to filter by
 */
function notFilterTable(notFilters) {
    const trs = document
        .getElementById("bibliography-table")
        .getElementsByTagName("tbody")[0]
        .getElementsByTagName("tr");
    
    // Resets the list of the visible rows from the filter
    filterVisibleRows = [];

    // Filters have priority over searches, so we check all rows of the table
    for (const tr of trs) {
        let found = false;

        for (const td of tr.getElementsByTagName("td")) {
            for (const notFilter of notFilters) {
                if (td.innerText.toUpperCase().indexOf(notFilter.toUpperCase()) != -1) {
                    found = true;
                    break;
                }
            }

            if (found) {
                break;
            }
        }

        if (found) {
            tr.style.display = "none";
        }
        else {
            tr.style.display = "";
            filterVisibleRows.push(tr);
        }
    }

    // If there's also an active search, re-initiate that
    if (document.getElementById("table-search").value != "") {
        searchTable();
    }
}

/**
 * Searches all cells of the bibliography table for a string
 */
function searchTable() {
    const searchTerm = document.getElementById("table-search").value.toUpperCase();

    // We are only searching the subset of trs given to us from the active filter
    for (const tr of filterVisibleRows) {
        let found = false;

        for (const td of tr.getElementsByTagName("td")) {
            if (td.innerText.toUpperCase().indexOf(searchTerm) > -1) {
                found = true;
                break;
            }
        }

        tr.style.display = (found ? "" : "none");
    }
}

filterTable('');