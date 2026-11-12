#!/usr/bin/env python3

import bibtexparser
import sys

def removeNIME(lib):
    newEntries = []
    removed = 0

    for entry in lib.entries:
        booktitle = entry.get("booktitle")

        if booktitle != None and ("NIME" in booktitle.value or "New Interfaces for Musical Expression" in booktitle.value):
            removed += 1
        else:
            newEntries.append(entry)

    return bibtexparser.Library(newEntries)

# Usage: ./remove-nime.py [input-bib]

def main():
    assert(len(sys.argv) == 2)

    lib = bibtexparser.parse_file(sys.argv[1])
    newLib = removeNIME(lib)
    bibtexparser.write_file("no-nime.bib", newLib)

main()