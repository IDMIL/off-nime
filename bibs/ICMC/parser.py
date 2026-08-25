#!/usr/bin/env python3

import asyncio
from difflib import SequenceMatcher
from enum import Enum
import numpy as np
from pydoll.browser.chromium import Chrome

class GetUrlCode(Enum):
    START=0             # initial state
    SUCCESS=1           # successfully found URL and updated the entry
    INVALID_YEAR=2      # the year is not a valid ICMC year (e.g., 1923 or something)
    TITLE_NOT_FOUND=3   # the title is not correlated with any papers from that year at ICMC

# Measures the similarity between two strings and returns a ratio
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Scrapes the ICMC website for paper URLs and assigns them to the parsed BibTeX entries
async def getUrls(bibtexDatas):
    start = "https://quod.lib.umich.edu/i/icmc/bbp2372.*"

    async with Chrome() as browser:
        tab = await browser.start()

        async with tab.expect_and_bypass_cloudflare_captcha():
            print("Scraping paper URLs for all ICMC years, this may take a while...")
            print("Note that your RAM usage may balloon quite a bit with this step.")

            await tab.go_to(start)

            volumeUl = await tab.find(id="byvolume", tag_name="ul", timeout=20)
            volumes = await volumeUl.get_children_elements(max_depth=1, tag_filter=["li"])

            volumeYears = [(await volume.text)[-4:] for volume in volumes]
            volumeLinks = [(await volume.get_children_elements(max_depth=1, tag_filter=["a"]))[0].get_attribute("href") for volume in volumes]

            # year -> { title -> URL }
            volumesDict = {(await volume.text)[-4]: None for volume in volumes}

            for i in range(len(volumes)):
                print(f"[{i+1}/{len(volumes)}] Scraping year: {volumeYears[i]}")
                await tab.go_to(volumeLinks[i])

                table = await tab.find(id="picklistitems", tag_name="table", timeout=5)
                entries = await table.get_children_elements(max_depth=4, tag_filter=["a"])
                
                # paper title -> url
                titleUrlDict = {}

                for entry in entries:
                    titleUrlDict.update({await entry.text: entry.get_attribute("href")})

                volumesDict.update({volumeYears[i]: titleUrlDict})

            print("Done scraping.")
            print("Assigning URLs to BibTeXs...")

            i = 1
            for bibtexData in bibtexDatas:
                print(f"\n[{i}/{len(bibtexDatas)}] Searching for \"{bibtexData["title"]}\"")

                code = GetUrlCode.START
                titleUrlDict = volumesDict.get(bibtexData["year"])

                if (titleUrlDict):
                    for title, url in titleUrlDict.items():
                        similarityScore = similarity(bibtexData["title"], title)
                        
                        if similarityScore >= 0.7:
                            bibtexData["url"] = url
                            
                            if (similarityScore < 0.9):
                                bibtexData["comment"] = f"LOW_URL_SCORE: You may want to check the URL for this citation. (0.7 <= Ratio < 0.9)"

                            code = GetUrlCode.SUCCESS
                            break

                    if (code != GetUrlCode.SUCCESS):
                        code = GetUrlCode.TITLE_NOT_FOUND
                        bibtexData["comment"] = f"URL_NOT_FOUND: Could not find a URL for this citation."

                else:
                    code = GetUrlCode.INVALID_YEAR
                    bibtexData["comment"] = f"URL_NOT_FOUND: Could not find a URL for this citation."

                print(f"Result: {str(code)}");
                i += 1

# Parses a string of authors separated by " and ", commas, and/or the Oxford comma
def parseAuthors(authorString):
    # Parsing the author string, which doesn't have any consistency (yippee!)
    authorsAndSplit = authorString.split(" and ")
    authors = []

    for author in authorsAndSplit:
        # Doing weird gymnastics to handle Oxford commas that were malformed due to the " and " split
        authorsCommaSplit = author.replace(", ", "|").replace(",", "").split("|")
        authors += authorsCommaSplit

    return authors

# Converts a Python dictionary of BibTeX data to a BibTeX string that can be put in a .bib file
def toBibtexString(data):
    citationName = data["authors"][0].split(" ")[-1].replace("\'", "-") + data["year"]

    return f'''{f"% {data["comment"]}" if data.get("comment") else ""}
@inproceedings{{{citationName},
    author = {{{" and ".join(data["authors"])}}},
    title = {{{data["title"]}}},
    pages = {{{data["pages"]}}},
    booktitle = {{{data["booktitle"]}}},
    year = {{{data["year"]}}},
    publisher = {{{data["publisher"]}}},
    address = {{{data["address"]}}}{f''',
    url = {{{data["url"]}}}''' if data.get("url") else ""}
}}
    '''

################
# BEGIN SCRIPT #
################

f = open("./citations.txt", "r")
content = f.read()
f.close()

bibtexDatas = []

year = ""
publisher = ""
address = ""
newConference = False

lines = content.split('\n')
i = 0

# main parsing loop
while i < len(lines):
    line = lines[i]

    # Handling new proceedings markers
    if len(line) > len("PROCEEDINGS") and line[0 : len("PROCEEDINGS")] == "PROCEEDINGS":
        year = line[line.index("CONFERENCE") + len("CONFERENCE") + 1 : -1]
        newConference = True
    else:
        # Handling location info underneath the PROCEEDINGS 
        if (newConference):
            locationSplit = line.split(", ", maxsplit=1)
            publisher = locationSplit[0]
            address = locationSplit[1]
            newConference = False
        else:
            # Handling weird line breaks where the citation is pushed onto a new line
            while i+1 < len(lines) and lines[i+1][0 : len("PROCEEDINGS")] != "PROCEEDINGS" and len(lines[i+1].split(" - ")) == 1:
                line += " " + lines[i+1]
                i += 1

            # Splitting entries by " - " and creating the BibTeX string using a dictionary
            fields = line.split(" - ")
            bibtexDatas.append({
                "authors": parseAuthors(fields[1]),
                "title": fields[2],
                "pages": fields[0],
                "booktitle": "Proceedings of the International Computer Music Conference",
                "year": year,
                "publisher": publisher,
                "address": address
            })

    i += 1

print(f"Parsed citations.txt file; found {len(bibtexDatas)} entries.")
print("Acquiring urls...")

asyncio.run(getUrls(bibtexDatas)) # gets and populates the URL fields in these BibTeX dictionaries
bibtexStrings = {} # year -> list of bibtex entries

print("Done acquiring URLS.")
print("Converting to .bib files...")

# converting all bibtex data dictionaries to strings and grouping them by year
for data in bibtexDatas:
    if bibtexStrings.get(data["year"]) == None:
        bibtexStrings.update({data["year"]: [toBibtexString(data)]})
    else:
        bibtexStrings[data["year"]].append(toBibtexString(data))

for year, bibs in bibtexStrings.items():
    # Skipping existing bib entries
    if year in ["1975", "1977", "1978"]:
        continue

    f = open(f"{year}.bib", "w")
    f.write("".join(bibs) if len(bibs) > 1 else bibs[0])
    f.close()

print("Done!")