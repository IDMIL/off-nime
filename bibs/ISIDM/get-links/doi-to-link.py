#!/usr/bin/env python3

import bibtexparser

library = bibtexparser.parse_file("with-dois.bib")

for entry in library.entries:
    if entry.fields_dict.get("url") == None and entry.fields_dict.get("doi") != None:
        entry.set_field(bibtexparser.model.Field("url", f"https://doi.org/{entry.fields_dict["doi"].value}"))

bibtexparser.write_file("with-links.bib", library)