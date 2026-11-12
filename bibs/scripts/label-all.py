#!/usr/bin/env python3

import bibtexparser
import os

def label(path, l):
    lib = bibtexparser.parse_file(path)

    for entry in lib.entries:
        entry.set_field(bibtexparser.model.Field("note", l))

    bibtexparser.write_file(path, lib)

def recurseRun(path):
    for child in os.listdir(path):
        childPath = path + "/" + child

        if os.path.isdir(childPath):
            recurseRun(childPath)

        else:
            _, ext = os.path.splitext(childPath)
            if ext == ".bib":
                labelStr = childPath[:childPath.find('/')]
                print(f"{childPath}:\t{labelStr}")
                label(childPath, labelStr)

for item in os.listdir():
    if os.path.isdir(item):
        recurseRun(item)