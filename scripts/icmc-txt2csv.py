import csv

def parse_details(line):
    """Extracts details from lines following the conference title."""
    parts = line.split(' - ')
    if len(parts) >= 3:
        return {
            "page-range": parts[0].strip(),
            "authors": parts[1].strip(),
            "title": parts[2].strip()
        }
    else:
        return None

def process_file(input_file):
    data = []
    current_year = None
    current_country = None
    current_institution = None
    current_city = None

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            # Identify and parse the conference title line
            if 'PROCEEDINGS OF THE INTERNATIONAL COMPUTER MUSIC CONFERENCE' in line:
                # Extract year, institution, city, and country
                # Assuming format: "... CONFERENCE YEAR, Institution, City, Country"
                parts = line.split(',')
                if len(parts) >= 4:
                    current_year = parts[0].split()[-1]  # Last word of the first part
                    current_institution = parts[-3].strip()
                    current_city = parts[-2].strip()
                    current_country = parts[-1].strip()

            # Parse contribution details
            elif line:  # non-empty line
                parsed_line = parse_details(line)
                if parsed_line:
                    parsed_line.update({
                        "year": current_year,
                        "country": current_country,
                        "institution": current_institution,
                        "city": current_city
                    })
                    data.append(parsed_line)

    return data

def write_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        fieldnames = ["year", "country", "institution", "city", "page-range", "authors", "title"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def main():
    input_file = 'input.txt'  # Update with the path to your input .txt file
    output_file = 'output.csv'  # Update with the desired path for your output .csv file
    data = process_file(input_file)
    write_csv(data, output_file)
    print("Conversion complete! Data has been written to", output_file)

if __name__ == "__main__":
    main()
