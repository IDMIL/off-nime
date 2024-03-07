import requests
from bs4 import BeautifulSoup
import pickle
import time
import os
import pandas as pd
from typing import TypedDict

class RefType(TypedDict):
    Gen_Case: str
    names: list
class RefTypes(TypedDict):
    Conference_Proceedings: RefType
    Journal_Paper: RefType
    Book: RefType
    Other: RefType


def path_checker(path):
    print(os.path.exists(path))
    return os.path.exists(path)
    
def page_scraper(url_list: dict):
    list_items = []
    old_list_size =0
    for url,type_ in url_list.items():
        
        try:
            response = requests.get(url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            list_items = extract_references(list_items,soup,type_)
            list_size = len(list_items)
            print(list_size," ",list_size-old_list_size)
            old_list_size = list_size
            time.sleep(0)
        except Exception as e:
            print(f"Failed to scrape ")
            exit()

    return(list_items)
# Let's define a function to parse the HTML and extract list items
def extract_list_items_UL(soup, list_items):

    # Find all unordered list elements
    ul_elements = soup.find_all('ul')
    
    # Loop through each unordered list
    for ul in ul_elements:
        if ul.find(class_='toc'):
            continue
        # Find all list item elements within each unordered list
        li_elements = ul.find_all('li', class_='level1')
        
        # Extract text from each list item
        for li in li_elements:
            text = li.get_text(strip=True)
            
            #Throws for special cases that could not be caught by the find_all
            if "(updated in November 2011)" in text:
                break
            if "Introductory References" in text:
                break
            else:
                list_items.append(text)
            
            
    return list_items
def extract_list_items_P(soup, list_items):
    # Find all unordered list elements
    div_elements = soup.find_all('div', class_='level2')
    # Loop through each unordered list
    for div in div_elements:
        p_elements = div.find_all('p')
        for p in p_elements:
            text = p.get_text(strip=True)
            list_items.append(text)
    
    return list_items

def extract_references(list_items, soup, type_):
    # Extend the if case with a new type that must be defined for scraping a web sites_ reference.
    # Must also create a new function to go with the if case.
    if type_ == "p":
        list_items = extract_list_items_P(soup,list_items)
    if type_ == "ul":
        list_items = extract_list_items_UL(soup,list_items)
    return list_items

type_list: RefTypes = {
    "Conference Proceedings" : RefType(
        Names= ["International Computer Music Conference"],
        Gen_Case= "Proceedings"
    ),
        
    "Journal Paper" : RefType(
        Names= ["Contemporary Music Review", "Science", "ACM", "Scientific American", "Computer Music Journal"],
        Gen_Case= "TBD"
    ),
    "Book" : RefType(
        Names= ["Prentice Hall", "MIT"],
        Gen_Case= "Press"
    ),
    "Other" : RefType(
        Names= ["NIME", "VHS"],
        Gen_Case= "TBD"
    )
}


def ref_sorter(ref, type_list: RefTypes):
    t = "N/A"
    n = "N/A"
    for type_, specs in type_list.items():
        if specs["Gen_Case"] in ref:
            t = type_
        for name in specs["Names"]:
            if name in ref:
                n = name
                t = type_
    
    return formater(t,n)


            
        
def formater(type_,org_):
    return {'type':type_, 'org': org_}


def main():
    # SECTION: GATHERING REFERENCES 
    if not path_checker("../ISIDM/references.pkl"):
        if not path_checker("../ISIDM"):
            os.makedirs("../ISIDM")
            print(f"The directory ISIDM has been created.")
        references = []
        url_list = {"https://sensorwiki.org/isidm/evolution_of_interactive_electronic_systems/bibliography": "ul",
                    "https://sensorwiki.org/isidm/interaction_and_performance/bibliography": "p",
                    "https://sensorwiki.org/isidm/sensors_and_actuators/bibliography": "ul",
                    "https://sensorwiki.org/isidm/interface_design/bibliography": "ul",
                    "https://sensorwiki.org/isidm/mapping/bibliography": "ul",
                    "https://sensorwiki.org/isidm/software_tools/bibliography": "ul",
                    "https://sensorwiki.org/isidm/dance_technology/bibliography": "ul"}
        references = page_scraper(url_list)
        references = {"references": references}
        df_references = pd.DataFrame(references)
        
        df_references.to_pickle("../ISIDM/references.pkl")

        # Used to visualize the data and see if anything was not extracted well
        # df_references.to_excel("../ISIDM/references.xlsx")

    data : pd.DataFrame = pd.read_pickle("../ISIDM/references.pkl")
    sorted_reference = []
    for index, row in data.iterrows():
        sorted_reference.append(ref_sorter(row['references'] ,type_list))
        print(sorted_reference)
    ref_types_orgs = pd.DataFrame(sorted_reference)
    
    data = data.join(ref_types_orgs)
    print(data)
    # for ref in references:
    #         sorted_reference.append(ref_sorter(ref ,type_list))
    # df = pd.DataFrame(sorted_reference)
    # print(df)

    # with open("../ISIDM/ISIDM_references.json", "w", encoding='utf8') as file:
        
            
    #         # json.dump(sorted_reference, file,ensure_ascii=False,  indent = 4)
            
    # file.close()
    

        
    # SECTION: SORTING REFERENCES 
    # Code must be updated to take into concideration an absolute path, or have it depend on where the user wants the folder.
        

#    
        
    
        
if __name__ =='__main__':
    main()





# Load the first HTML content to pass to the function for extraction
# Please note that this approach assumes that the file content can fit into memory
# If the file is too large, more sophisticated streaming and parsing techniques may be needed
# with open('/mnt/data/file-ra1g0xX4P2KeskRUi4tnlHmv', 'r', encoding='utf-8') as file:
#     html_content = file.read()

# # Call the function to extract list items
# bibliographic_entries = extract_list_items(html_content)
# bibliographic_entries[:5]  # Return the first 5 entries for brevity
# # Initialize a list to hold all papers info
# all_papers_info = []



# Exporting the data to a CSV file
# with open('icmc_papers_1980_2000.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Year', 'Title', 'Authors', 'Link'])  # writing header
#     writer.writerows(all_papers_info)  # writing all paper information