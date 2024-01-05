from fuzzywuzzy import fuzz
import pandas as pd
from collections import defaultdict, Counter
import re

# Read the CSV files
print("Reading CSV files...")
original_file1 = pd.read_csv('input1-corrigido.csv')
original_file2 = pd.read_csv('icmc_papers_web.csv')

# Create copies for preprocessing and matching
file1 = original_file1.copy()
file2 = original_file2.copy()

# Preprocess function
def preprocess(text):
    if pd.isna(text):
        return ""
    return str(text).strip().lower()

# Preprocess titles and authors in both files for matching
print("Preprocessing data for matching...")
file1['title'] = file1['title'].apply(preprocess)
file1['authors'] = file1['authors'].apply(preprocess)
file2['Title'] = file2['Title'].apply(preprocess)
file2['Authors'] = file2['Authors'].apply(preprocess)

# Initialize an empty list to hold matched rows
matches = []

# Set a threshold for fuzzy matching (e.g., 80 out of 100)
threshold = 80
print(f"Threshold for matching is set to {threshold}.")

# Iterate over each row in file1 to find the best match in file2
print("Starting the matching process...")
for index1, row1 in file1.iterrows():
    best_match_score = threshold  # Initialize with threshold
    best_match_index = None
    year1 = row1['year']  # Get the year from file1 row
    print(f"Processing File1 Row {index1} (Year {year1})...")

    for index2, row2 in file2.iterrows():
        if row2['Year'] == year1:  # Match only rows from the same year
            title_score = fuzz.token_sort_ratio(row1['title'], row2['Title'])
            if title_score > best_match_score:
                best_match_score = title_score
                best_match_index = index2

    if best_match_index is not None:
        matches.append((index1, best_match_index, best_match_score))
        print(f"--> Best match for File1 Row {index1} is File2 Row {best_match_index} with score {best_match_score}.")
    else:
        print(f"###ERROR: File1 Titles {index1} didn't have any match with File2")

print("Matches Found and Data Collected.")

# Create a new DataFrame to store all the match data
print("Creating a new DataFrame for matched data...")
match_columns = list(original_file1.columns) + list(original_file2.columns) + ["Score"]
matched_data = []

# Define a function to convert a list of author names into the BibTeX format with conditional dots
def convert_to_bibtex_format_conditional_dots(authors_list):
    bibtex_authors = []
    for author in authors_list:
        parts = author.split(',')
        if len(parts) == 2:
            last_name, first_names = parts
            first_names_formatted = []
            for name in first_names.strip().replace('.', '').split():
                name = name.strip()
                first_names_formatted.append(f"{name}." if len(name) == 1 else name)
            formatted_name = f"{last_name.strip()}, {' '.join(first_names_formatted)}"
            bibtex_authors.append(formatted_name)
        else:
            bibtex_authors.append(author.strip())
    return ' and '.join(bibtex_authors)

# Function to extract the last name of the first author and concatenate it with the year
def construct_reference_name(authors, year):
    first_author = authors.split(';')[0]  # Assumes authors are separated by ';'
    last_name = first_author.split(',')[0]  # Assumes format "Last, First"
    # Remove any special characters from the last name
    sanitized_last_name = re.sub(r'[^A-Za-z0-9]', '', last_name.strip())
    reference_name = f"{sanitized_last_name}{year}"
    return reference_name


# Initialize a counter to track occurrences of last name and year combinations
name_year_counter = Counter()

def construct_reference_name(authors, year):
    first_author = authors.split(';')[0]  # Assumes authors are separated by ';'
    last_name = first_author.split(',')[0]  # Assumes format "Last, First"
    # Remove any special characters from the last name
    sanitized_last_name = re.sub(r'[^A-Za-z0-9]', '', last_name.strip())
    
    # Check for existing occurrences and determine suffix
    ref_base = f"{sanitized_last_name}{year}"
    count = name_year_counter[ref_base]
    name_year_counter[ref_base] += 1  # Increment the count for this base
    suffix = '' if count == 0 else chr(ord('a') + count)  # 'a', 'b', 'c', etc.
    
    reference_name = f"{ref_base}{suffix}"
    return reference_name

# Grouping matches by year
matches_by_year = defaultdict(list)
for index1, index2, score in matches:
    year = original_file1.iloc[index1]['year']
    matches_by_year[year].append((index1, index2, score))

print("Formatting matched data for BibTeX and writing to separate files...")

for year, year_matches in matches_by_year.items():
    # Start writing to a .bib file for each year
    with open(f'{year}.bib', 'w') as bibfile:
        for index1, index2, score in year_matches:
            # Retrieve the original data for matched entries
            entry_file1 = original_file1.iloc[index1]
            entry_file2 = original_file2.iloc[index2]

            # Format the authors
            authors = convert_to_bibtex_format_conditional_dots(entry_file1['authors'].split(';'))

            # Construct the reference name
            ref_name = construct_reference_name(entry_file2['Authors'], year)

            # Construct the address
            address = f"{entry_file1['institution']}, {entry_file1['city']}, {entry_file1['country']}"

            # Constructing the BibTeX entry
            bibtex_entry = f"@inproceedings{{{ref_name},\n" \
                           f"  author = {{{authors}}},\n" \
                           f"  title = {{{entry_file2['Title']}}},\n" \
                           f"  pages = {{{entry_file1['page-range']}}},\n" \
                           f"  booktitle = {{Proceedings of the International Computer Music Conference}},\n" \
                           f"  year = {{{year}}},\n" \
                           f"  publisher = {{MI: Michigan Publishing, University of Michigan Library}},\n" \
                           f"  address = {{{address}}},\n" \
                           f"  issn = {{2223-3881}},\n" \
                           f"  url = {{{entry_file2['Link'] if 'Link' in entry_file2 else 'Not Available'}}},\n}}\n"
            # Constructing the BibTeX entry
            # bibtex_entry = f"""
            # @inproceedings{{{ref_name}},
            #   author = {{{authors}}},
            #   title = {{{entry_file2['Title']}}},
            #   pages = {{{entry_file1['page-range']}}},
            #   booktitle = {{Proceedings of the International Computer Music Conference}},
            #   year = {{{year}}},
            #   publisher = {{MI: Michigan Publishing, University of Michigan Library}},
            #   address = {{{address}}},
            #   issn = {{2223-3881}},
            #   url = {{{entry_file2['Link'] if 'Link' in entry_file2 else 'Not Available'}}},
            # }}
            # """  

            # Write each BibTeX entry to the file
            bibfile.write(bibtex_entry)

    print(f"Matched data for year {year} saved to '{year}.bib'.")
