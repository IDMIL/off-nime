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
        const journal = tr.getElementsByTagName("td")[1].innerText.toUpperCase(); // index 1 => journal name

        if (journal.indexOf(filter.toUpperCase()) == -1) {
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
        const journal = tr.getElementsByTagName("td")[1].innerText.toUpperCase(); // index 1 => journal name
        let found = false;

        for (const notFilter of notFilters) {
            if (journal.indexOf(notFilter.toUpperCase()) > -1) {
                found = true;
                break;
            }
        }

        // Show all rows that don't have any matches
        if (!found) {
            tr.style.display = "";
            filterVisibleRows.push(tr);
        }
        // Hide rows that do
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
 */
function searchTable() {
    const searchTerm = document.getElementById("table-search").value.toUpperCase();

    // We are only searching the subset of trs given to us from the active filter
    for (const tr of filterVisibleRows) {
        const tds = tr.getElementsByTagName("td");
        let found = false;

        for (const td of tds) {
            if (td.innerText.toUpperCase().indexOf(searchTerm) > -1) {
                found = true;
                break;
            }
        }

        if (!found) {
            tr.style.display = "none";
        }
        else {
            tr.style.display = "";
        }
    }
}

filterTable('');