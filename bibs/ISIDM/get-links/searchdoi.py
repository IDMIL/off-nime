#!/usr/bin/env python3

# % Source - https://tex.stackexchange.com/a/300474
# % Posted by SachaB, modified by community. See post 'Timeline' for change history
# % Retrieved 2026-08-31, License - CC BY-SA 4.0

import sys, re
from unidecode import unidecode
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import http.client as httplib
import urllib

# Search for the DOI given a title; e.g.  "computation in Noisy Radio Networks"
# Credit to user13348, slight modifications
# http://tex.stackexchange.com/questions/6810/automatically-adding-doi-fields-to-a-hand-made-bibliography
def searchdoi(title, author):
  params = urllib.parse.urlencode({"titlesearch":"titlesearch", "auth2" : author, "atitle2" : title, "multi_hit" : "on", "article_title_search" : "Search", "queryType" : "author-title"})
  headers = {"User-Agent": "Mozilla/5.0" , "Accept": "text/html", "Content-Type" : "application/x-www-form-urlencoded", "Host" : "www.crossref.org"}
  # conn = httplib.HTTPConnection("www.crossref.org:80") # Not working any more, HTTPS required
  conn = httplib.HTTPSConnection("www.crossref.org")       
  conn.request("POST", "/guestquery/", params, headers)
  response = conn.getresponse()
  #print(response.status, response.reason)
  data = response.read()
  conn.close()
  return re.search(r'doi\.org/([^"^<^>]+)', str(data))

def normalize(string):
    """Normalize strings to ascii, without latex."""
    string = re.sub(r'[{}\\\'"^]',"", string)
    string = re.sub(r"\$.*?\$","",string) # better remove all math expressions
    return unidecode(string)

def get_authors(entry):
    """Get a list of authors' or editors' last names."""
    def get_last_name(authors):
        for author in authors :
            author = author.strip(" ")
            if "," in author:
                yield author.split(",")[0]
            elif " " in author:
                yield author.split(" ")[-1]
            else:
                yield author

    try:
        authors = entry["author"]
    except KeyError:
        authors = entry["editor"]

    authors = normalize(authors).split("and")
    return list(get_last_name(authors))


print("Reading Bibliography...")
with open(sys.argv[1]) as bibtex_file:
    bibliography = bibtexparser.load(bibtex_file)


print("Looking for Dois...")
before = 0
new = 0
total = len(bibliography.entries)
for i,entry in enumerate(bibliography.entries):
    print("\r{i}/{total} entries processed, please wait...".format(i=i,total=total),flush=True,end="")
    try:
        if "doi" not in entry or entry["doi"].isspace():
            title = entry["title"]
            authors = get_authors(entry)
            for author in authors:
                doi_match = searchdoi(title,author)
                if doi_match:
                    doi = doi_match.groups()[0]
                    entry["doi"] = doi
                    new += 1
        else:
            before += 1
    except:
        pass
print("")

template="We added {new} DOIs !\nBefore: {before}/{total} entries had DOI\nNow: {after}/{total} entries have DOI"

print(template.format(new=new,before=before,after=before+new,total=total))
outfile = sys.argv[1]+"_doi.bib"
print("Writing result to ",outfile)
writer = BibTexWriter()
writer.indent = '    '     # indent entries with 4 spaces instead of one
with open(outfile, 'w') as bibfile:
    bibfile.write(writer.write(bibliography))
