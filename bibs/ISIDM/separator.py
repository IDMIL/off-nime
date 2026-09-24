#!/usr/bin/env python3

import bibtexparser

lib = bibtexparser.parse_file("from-claude.bib")

good = []
noPublication = []

for entry in lib.entries:
    if not ("journal" in entry.fields_dict) and not ("booktitle" in entry.fields_dict) and not ("publisher" in entry.fields_dict):
        noPublication.append(entry)
    else:
        good.append(entry)

bibtexparser.write_file("unfinished/no-publication.bib", bibtexparser.Library(noPublication))
bibtexparser.write_file("final.bib", bibtexparser.Library(good))