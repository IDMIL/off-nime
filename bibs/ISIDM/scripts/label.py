#!/usr/bin/env python3

import bibtexparser

def label(path):
    lib = bibtexparser.parse_file(path)

    for entry in lib.entries:
        entry.set_field(bibtexparser.model.Field("note", "ISIDM"))

    bibtexparser.write_file(path, lib)

label("final.bib")
label("theses-tech-reports.bib")
