function getMinMaxYears() {
    const table = document.getElementById("bibliography-table");

    // the table is already sorted by year, so we can take advantage of that
    const trs = table.getElementsByTagName("tr");
    const minYear = trs[1].getElementsByTagName("td")[0].innerHTML;
    const maxYear = trs[trs.length - 1].getElementsByTagName("td")[0].innerHTML;

    return [minYear, maxYear];
}

function initMinMaxYears() {
    const minMaxYears = getMinMaxYears();
    document.getElementById("min-year").innerHTML = minMaxYears[0];
    document.getElementById("max-year").innerHTML = minMaxYears[1];
}

window.onload = initMinMaxYears();