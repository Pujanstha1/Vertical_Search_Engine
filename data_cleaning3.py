import csv
import re

def clean_text(text):
    # Remove leading and trailing whitespaces
    cleaned_text = text.strip()

    # Remove special characters and punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

    # Remove multiple spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    # Convert to lowercase
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def clean_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Cleaned Column 1', 'Cleaned Column 2', 'Cleaned Column 3'])  # Write header

            for row in reader:
                cleaned_row = [clean_text(cell) for cell in row]
                writer.writerow(cleaned_row)

    print('Cleaning completed.')

# Usage example
input_file = 'abc.csv'
output_file = 'cleaned_data1.csv'

clean_csv(input_file, output_file)
