#!/usr/bin/env python3

import bibtexparser
import os

def label(path, l):
    lib = bibtexparser.parse_file(path)

    for entry in lib.entries:
        entry.set_field(bibtexparser.model.Field("note", l))

    bibtexparser.write_file(path, lib)

for path in os.listdir("./"):
    _, ext = os.path.splitext(path)
    if ext == ".bib":
        label(path, "Extras")
