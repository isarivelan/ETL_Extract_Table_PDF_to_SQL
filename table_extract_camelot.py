import camelot
import cv2
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
from util import conn_str


INPUT_PATH = r"C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\pdfsample.pdf"
OUTPUT_DIR = r'C:\Users\isarivelan.mani\OneDrive - Wood PLC\Documents\Git\mani\output_file'


engine = create_engine(f'mssql+pyodbc:///?odbc_connect={conn_str}')


def table_extract_camelot(INPUT_PATH):
    tables = camelot.read_pdf(INPUT_PATH, pages='2,3,4', flavor='lattice' )
    for i, table in enumerate(tables):
        table.df.to_sql(name=f'table_{i+1}', con = engine, if_exists='replace', index=False)
   
    return tables


def clean_data(tables):
    
    combined_df = pd.concat([table.df for table in tables], ignore_index = True)
    cleaned_df = combined_df.dropna().drop_duplicates()
    cleaned_df.to_sql(name="pdf_data", con = engine, if_exists='replace' )
    return cleaned_df

if __name__ == "__main__":
    tables = table_extract_camelot(INPUT_PATH)
    clean_data(tables)