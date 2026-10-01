#!/usr/bin/env python3

import bibtexparser
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
                if "url" in bibtexData.fields_dict:
                    continue

                print(f"\n[{i}/{len(bibtexDatas)}] Searching for \"{bibtexData.fields_dict["title"].value}\"")

                code = GetUrlCode.START
                titleUrlDict = volumesDict.get(bibtexData.fields_dict["year"].value)

                if (titleUrlDict):
                    for title, url in titleUrlDict.items():
                        similarityScore = similarity(bibtexData.fields_dict["title"].value, title)
                        
                        if similarityScore >= 0.7:
                            bibtexData.set_field(bibtexparser.model.Field("url", url))
                            
                            if (similarityScore < 0.9):
                                print(f"LOW_URL_SCORE: You may want to check the URL for this citation. (0.7 <= Ratio < 0.9)")

                            code = GetUrlCode.SUCCESS
                            break

                    if (code != GetUrlCode.SUCCESS):
                        code = GetUrlCode.TITLE_NOT_FOUND
                        print(f"URL_NOT_FOUND: Could not find a URL for this citation.")

                else:
                    code = GetUrlCode.INVALID_YEAR
                    print(f"URL_NOT_FOUND: Could not find a URL for this citation.")

                print(f"Result: {str(code)}");
                i += 1

lib = bibtexparser.parse_file("from-isidm.bib")
asyncio.run(getUrls(lib.entries))
bibtexparser.write_file("from-isidm-urls.bib", lib)