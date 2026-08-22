function setNumEntries() {
    const table = document.getElementById("bibliography-table");
    const trs = table.getElementsByTagName("tr");
    
    let numVisibleEntries = -1; // ignore header

    for (const tr of trs) {
        if (tr.style.display !== "none") {
            numVisibleEntries++;
        }
    }

    document.getElementById("num-entries").innerHTML = `<p>Number of visible entries: ${numVisibleEntries}</p>`
}

window.onload = setNumEntries();