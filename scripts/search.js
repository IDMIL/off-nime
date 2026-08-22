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
            if (td[j]) {
                txtValue = td[j].textContent || td[j].innerText;
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