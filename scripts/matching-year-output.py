from fuzzywuzzy import fuzz
import pandas as pd

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

for index1, index2, score in matches:
    # Combine the original row data from both files along with the score
    matched_row = list(original_file1.iloc[index1].values) + list(original_file2.iloc[index2].values) + [score]
    matched_data.append(matched_row)

# Convert the combined matched data into a DataFrame
matched_df = pd.DataFrame(matched_data, columns=match_columns)

# Save the new DataFrame to a CSV file
matched_df.to_csv('matched_file.csv', index=False)
print("Matched data saved to 'matched_file.csv'.")
