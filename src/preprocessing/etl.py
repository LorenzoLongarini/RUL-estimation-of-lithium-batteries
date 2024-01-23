import pandas as pd
import os
from src.utils import constants as cs
from datetime import datetime

# merge all files in specific folder
def merge_files (data_dir: str = 'src/dataset/CS2_38', file_name:str = 'CS2_38', is_charge = True):
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
            if is_charge: 
                # consider only step index 2-4
                cleaned = cleaned[~cleaned[cs.step_index].isin(cs.charge_indexes)]
                # check current
                cond_sindex = (cleaned[cs.step_index] == 4)
                cond_curr = (cleaned[cs.current] > 0.55)
                # reduce dataframe
                cleaned = cleaned[~(cond_sindex & cond_curr)]
                # for key, group in cleaned.groupby(cs.c_index):
                #     diffs =  group[cs.current].diff().abs() 
                #     mask = ~(diffs > 0.0502)
                #     cleaned.loc[cleaned[cs.c_index] == key, :] = cleaned.loc[cleaned[cs.c_index] == key, :][mask]
                cleaned = cleaned[cs.charge_list]
                cleaned.to_csv(os.path.join(cs.ds_cleaned, f'charge-{file_name}'), index=False)    
            else:
                # consider only step index 7
                # cleaned = cleaned[~cleaned[cs.step_index].isin(cs.discharge_indexes)]
                cleaned = cleaned[cs.discharge_list]
                cleaned.to_csv(os.path.join(cs.ds_cleaned, f'discharge-{file_name}'), index=False)    
