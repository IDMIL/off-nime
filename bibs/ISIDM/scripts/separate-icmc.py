#!/usr/bin/env python3

import bibtexparser

lib = bibtexparser.parse_file("final.bib")

icmc = []
other = []

for entry in lib.entries:
    if "booktitle" in entry.fields_dict != None and "international computer music conference" in entry.fields_dict["booktitle"].value.lower():
        entry.fields_dict["booktitle"].value = "Proceedings of the International Computer Music Conference"
        icmc.append(entry)
    else:
        other.append(entry)

bibtexparser.write_file("icmc.bib", bibtexparser.Library(icmc))
bibtexparser.write_file("not-icmc.bib", bibtexparser.Library(other))
