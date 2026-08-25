#!/usr/bin/env python3

import bibtexparser
from difflib import SequenceMatcher
import os

# Measures the similarity between two strings and returns a ratio
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Checks if there is a string in list l that has a similarity ratio greater than 0.7 for query
def containsSimilar(query, l):
    for s in l:
        if (similarity(query, s) > 0.7):
            return True
        
    return False

################
# BEGIN SCRIPT #
################

cmj = set()
icmc = set()

print("Parsing CMJ and ICMC .bibs...")

# Collecting CMJ and ICMC entry titles
for cmjBib in os.listdir("../../CMJ"):
    cmj.update([entry.fields_dict["title"].value for entry in bibtexparser.parse_file("../../CMJ/" + cmjBib).entries])

for icmcBib in os.listdir("../../ICMC"):
    icmc.update([entry.fields_dict["title"].value for entry in bibtexparser.parse_file("../../ICMC/" + icmcBib).entries])

print("Done.\nParsing and deduplicating ISIDM .bib...")

isidm = bibtexparser.parse_file("from-zotero.bib").entries
deduplicated = []

i = 0
for isidmBibEntry in isidm:
    cmjContainsSimilar = containsSimilar(isidmBibEntry.fields_dict["title"].value, cmj)
    icmcContainsSimilar = containsSimilar(isidmBibEntry.fields_dict["title"].value, icmc)

    if not cmjContainsSimilar and not icmcContainsSimilar:
        deduplicated.append(isidmBibEntry)
    else:
        print(f"Found and removed duplicate: \"{isidmBibEntry.fields_dict["title"].value}\" (ISIDM <-> {"CMJ" if cmjContainsSimilar else "ICMC"})")
        i += 1

print(f"Removed {i} duplicates from the ISIDM bibliography.")

deduplicatedLibrary = bibtexparser.Library(deduplicated)
bibtexparser.write_file("deduplicated.bib", deduplicatedLibrary)

print("Done; see deduplicated.bib.")