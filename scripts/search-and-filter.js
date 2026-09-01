// Code borrowed from: https://www.w3schools.com/howto/howto_js_filter_table.asp
function tableSearch() {
    var input, filter, table, tr, td, i, j, txtValue, found;
    input = document.getElementById("table-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("bibliography-table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");

        for (j = 0; j < td.length; j++) {
            if (td[1]) {
                txtValue = td[1].textContent || td[1].innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                    found = true;
                    break;
                } 
            }
        }
        if (!found) {
            tr[i].style.display = "none";
        }
        found = false;
    }
}

// Similar to tableSearch, but uses a passed value instead of reading from HTML
function tableFilter(dataset) {
    var filter, table, tr, td, i, txtValue, found;
    filter = dataset.toUpperCase()
    table = document.getElementById("bibliography-table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");

        if (td[1]) {
            txtValue = td[1].textContent || td[1].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                found = true;
            } 
        }

        if (!found) {
            tr[i].style.display = "none";
        }
        found = false;
    }
}

// Similar to tableFilter, but searches for entries that *do not* match the input list of filters. Used for inhomogenous datasets (i.e. ISIDM)
function tableNotFilter(datasets) {
    var filters, table, tr, td, i, txtValue, found;
    filters = datasets.map((dataset) => {return dataset.toUpperCase()})
    table = document.getElementById("bibliography-table");
    tr = table.getElementsByTagName("tr");

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");

        if (td[1]) {
            txtValue = td[1].textContent || td[1].innerText;
            
            for (var filter of filters) {
                if (txtValue.toUpperCase().indexOf(filter) != -1) { // hide items that match any of the filters
                    tr[i].style.display = "none";
                    found = true;
                    break;
                } 
            }
        }

        if (!found) {
            tr[i].style.display = "";
        }
        found = false;
    }
}