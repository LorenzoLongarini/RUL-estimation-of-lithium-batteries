import pandas as pd
import os
from src.utils import constants as cs

# merge all files in specific folder
def merge_files (data_dir: str = 'src/dataset/CS2_38', file_name:str = 'CS2_38'):
    # define new data frame
    cleaned = pd.DataFrame()
    # consider only channel sheets
    for filename in os.listdir(data_dir):
        xls_file = pd.ExcelFile(os.path.join(data_dir, filename))
        sheet_fnames = [sheet for sheet in xls_file.sheet_names if sheet.startswith(cs.channel)]
        # cycle all files 
        for sheet_fname in sheet_fnames:
            df = pd.read_excel(os.path.join(data_dir, filename), sheet_name=sheet_fname)
            df = df[cs.white_list]
            # find max cycle value for each sheet
            max_cindex = cleaned[cs.c_index].max() if not cleaned.empty else 0
            # update total cycle index
            df[cs.c_index] += max_cindex
            # concat all files 
            cleaned = pd.concat([cleaned, df], ignore_index=True)
            cleaned.to_csv(os.path.join(cs.ds_cleaned, f'{file_name}.csv'), index=False)