import requests
from bs4 import BeautifulSoup
import csv

# Base URL
base_url = "https://quod.lib.umich.edu/i/icmc/bbp2372."

# Initialize a list to hold all papers info
all_papers_info = []

for year in range(1980, 2001):  # Looping from 1980 to 2000
    # Constructing the URL for each year
    url = f"{base_url}{year}"
    print(f"Scraping Year: {year}")  # Verbose mode: print the year being scraped
    
    try:
        # Send a GET request to the website and get the HTML content
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Locating the table by its id
        table = soup.find('table', id='picklistitems')

        # Iterate over each table row (ignoring the header row)
        for row in table.find_all('tr')[1:]:  # [1:] to skip the header row
            columns = row.find_all('td')
            if columns:  # Check if there are columns in the row
                title_element = columns[0].find('a')  # Getting the anchor element with the title
                title = title_element.get_text(strip=True)  # First column for titles
                title_link = title_element.get('href')  # Extracting the link related to the title

                # Disregard the last route of the link that starts with "--" and add "1"
                if "--" in title_link:
                    title_link = title_link.split("--")[0] + "1"
                
                authors = columns[1].get_text(strip=True)  # Second column for authors
                all_papers_info.append([year, title, authors, title_link])
        
        print(f"Successfully scraped {year}.")  # Verbose mode: print success message

    except Exception as e:
        print(f"Failed to scrape {year}. Error: {e}")  # Verbose mode: print failure message

# Exporting the data to a CSV file
with open('icmc_papers_1980_2000.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Year', 'Title', 'Authors', 'Link'])  # writing header
    writer.writerows(all_papers_info)  # writing all paper information
