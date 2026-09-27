let downloadingAll = false;
let currentBibtex = ``;

function copyBibtex(bibtex) {
    if (!downloadingAll) {
        navigator.clipboard.writeText(bibtex);
    }
    else {
        currentBibtex = bibtex;
    }
}

function downloadAll() {
    downloadingAll = true;

    let all = "";

    const tbody = document
        .getElementById("bibliography-table")
        .getElementsByTagName("tbody")[0];

    for (const tr of tbody.getElementsByTagName("tr"))  {
        const tds = tr.getElementsByTagName("td");

        let button = tds[tds.length - 1].getElementsByTagName("button")[0];
        try {
            button.click();
        }
        catch (e) {
            console.log(tr);
        }

        all += currentBibtex;
    }

    const blob = new Blob([all], { type: "text/plain" });
    const fileUrl = URL.createObjectURL(blob);

    const hiddenAnchor = document.createElement("a");
    hiddenAnchor.href = fileUrl;
    hiddenAnchor.download = "off-nime.bib";

    document.body.appendChild(hiddenAnchor);
    hiddenAnchor.click();

    document.body.removeChild(hiddenAnchor);
    URL.revokeObjectURL(fileUrl);

    downloadingAll = false;
    currentBibtex = ``;
}