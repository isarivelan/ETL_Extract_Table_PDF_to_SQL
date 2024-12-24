import pdfplumber
import json
import csv
import pandas as pd

# Specify the input PDF path and output paths for JSON, CSV, and Excel formats
input_pdf_path = r"C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\pdfsample.pdf"
json_output_path = r"C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\output_file\output.json"
csv_output_path = r"C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\output_file\output.csv"
excel_output_path = r"C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\output_file\output.xlsx"

# Function to extract tables from all pages and save the output in JSON, CSV, and Excel formats
def extract_tables_to_formats(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        all_tables = []
        
        # Extract tables from each page
        for page in pdf.pages:
            tables = page.extract_tables()
            all_tables.extend(tables)
        print(all_tables)
    
    # Flatten the list of tables into a single list of rows
    flattened_table = [row for table in all_tables for row in table]
    
    return flattened_table

def cleaned_data(flattened_table, json_path, csv_path, excel_path):
    df = pd.DataFrame(flattened_table)
    cleaned_df = df.dropna(how='all')
    final_cleaned_df = cleaned_df.drop_duplicates()
  
    # Save to JSON format
    with open(json_path, 'w') as json_file:
        json.dump(final_cleaned_df.to_dict(orient = 'records'), json_file)

    # Save to Excel format
    final_cleaned_df.to_csv(csv_output_path, index = False)
    
    final_cleaned_df.to_excel(excel_path, index=False)




if __name__ == '__main__':
# Extract tables from the input PDF and save to JSON, CSV, and Excel formats
   flattened_table =  extract_tables_to_formats(input_pdf_path)
   cleaned_data(flattened_table, json_output_path, csv_output_path, excel_output_path)
    

    