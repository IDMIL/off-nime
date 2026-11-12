#!/usr/bin/env python3

import bibtexparser
from difflib import SequenceMatcher
import os
import sys

entryTitles = set()

def recurseGetEntries(path, ignore):
    global entryTitles

    for child in os.listdir(path):
        childPath = path + "/" + child
        print(childPath)

        if os.path.isdir(childPath):
            recurseGetEntries(childPath, ignore)

        else:
            _, ext = os.path.splitext(childPath)
            if ext == ".bib" and child != ignore:
                lib = bibtexparser.parse_file(childPath)
                entryTitles.update([entry.get("title").value.lower() for entry in lib.entries])


# Measures the similarity between two strings and returns a ratio
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Removes duplicates from a file by performing a recursive search of all .bib entries in root-path
# Usage: ./removeDuplicates.py [root-path] [file]
def main():
    assert(len(sys.argv) == 3)

    print("Getting all entries from the database...")
    recurseGetEntries(sys.argv[1], sys.argv[2].split("/")[-1])
    print("Done!")

    lib = bibtexparser.parse_file(sys.argv[2])
    deduplicated = []

    for entry in lib.entries:
        found = False

        for title in entryTitles:
            if similarity(title, entry.get("title").value.lower()) >= 0.9:
                print(f"Removed duplicate: entry = {entry.get("title").value.lower()}, database = {title}")
                found = True
                break

        if not found:
            deduplicated.append(entry)

    bibtexparser.write_file("out.bib", bibtexparser.Library(deduplicated))

main()