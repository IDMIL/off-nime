function generateAndDownloadBibtex(bibtex) {
    // const blob = new Blob([bibtex], { type: "text/plain" });
    // const fileUrl = URL.createObjectURL(blob);

    // const hiddenAnchor = document.createElement("a");
    // hiddenAnchor.href = fileUrl;
    // hiddenAnchor.download = "reference.bib";

    // document.body.appendChild(hiddenAnchor);
    // hiddenAnchor.click();

    // document.body.removeChild(hiddenAnchor);
    // URL.revokeObjectURL(fileUrl);
    navigator.clipboard.writeText(bibtex);
}