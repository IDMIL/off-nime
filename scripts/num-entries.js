function getNumEntries() {
    const table = document.getElementById("bibliography-table");
    const trs = table.getElementsByTagName("tr");
    
    let numVisibleEntries = -1; // ignore header

    for (const tr of trs) {
        if (tr.style.display !== "none") {
            numVisibleEntries++;
        }
    }

    return numVisibleEntries;
}

function initNumEntries() {
    const numEntries = getNumEntries();
    document.getElementById("num-entries").innerHTML = `<p>Number of visible entries: ${numEntries}</p>`;
    document.getElementById("blurb-count").innerHTML = `${numEntries}`;
}

window.onload = initNumEntries();