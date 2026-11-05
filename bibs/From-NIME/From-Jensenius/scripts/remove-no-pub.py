#!/usr/bin/env python3

import bibtexparser

def removeNoPub(lib):
    newEntries = []

    for entry in lib.entries:
        if entry.get("journal") != None or entry.get("booktitle") != None:
            newEntries.append(entry)

    return bibtexparser.Library(newEntries)

lib = bibtexparser.parse_file("candidates_cited.bib")
lib = removeNoPub(lib)
bibtexparser.write_file("candidates_cited.bib", lib)
