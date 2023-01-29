import bibtexparser
import os

# create a list of subdirectories containing bib files
directories = ["./CMJ", "./ICMC"]

with open("README.md", "w") as md_file:
    md_file.write(f"# Off-NIME NIME Papers\n")
    md_file.write(f"Nime papers, chapters and books published outside of the NIME Conference proceedings\n")

    for directory in directories:
        if directory == "./CMJ":
            md_file.write(f"\n## Computer Music Journal (CMJ)\n\n")
        elif directory == "./ICMC":
            md_file.write(f"\n## International Computer Music Conference (ICMC)\n\n")
        # create a list to store entries from all bib files
        all_entries = []    
    
        # create a list of bib files in the directory
        bib_files = [f for f in os.listdir(directory) if f.endswith('.bib')]
    
        # iterate over all bib files and extract the data
        for bib_file in bib_files:
            with open(os.path.join(directory, bib_file), 'r') as bibfile:
                bib_database = bibtexparser.load(bibfile)
            all_entries += bib_database.entries
    
        # sort the entries by year and then by number
        all_entries = sorted(all_entries, key=lambda x: (x.get('year', ''), x.get('number', '')))
    
        # write the data to markdown file
        
        current_year = ""
        for entry in all_entries:
            title = entry.get('title', '')
            author = entry.get('author', '')
            year = entry.get('year', '')
            url = entry.get('url', '')
            entry_type = entry.get('ENTRYTYPE', '')
    
    
            if entry_type == 'article':
                number = entry.get('number', '')
                journal = entry.get('journal', '')
                volume = entry.get('volume', '')
                if year != current_year:
                    current_year = year
                    md_file.write(f"### {year} (Vol {volume})\n\n")
    
                md_file.write(f"N.{number}\\\n")
                md_file.write(f"**{author}**. {title}. ***{journal} {year}***.\\\n")
                md_file.write(f"[<kbd><br>Download PDF<br></kbd>]({url}) <nbsp> [<kbd><br>BibTex<br></kbd>](CMJ/{year}.bib)\n\n")
    
    
            if entry_type == 'inproceedings':
                booktitle = entry.get('booktitle', '')
                if year != current_year:
                    current_year = year
                    md_file.write(f"### {year}\n\n")
    
                md_file.write(f"**{author}**. {year}. {title}. ***{booktitle}***.\\\n")
                md_file.write(f"[<kbd><br>Download PDF<br></kbd>]({url}) <nbsp> [<kbd><br>BibTex<br></kbd>](CMJ/{year}.bib)\n\n")
    
    
            
    