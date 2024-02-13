# Import data

import pandas as pd
import os
import numpy as np
from src.utils import constants as cs


def make_soh(file_path):

    soh_charge_folder = os.path.abspath(os.path.join(cs.ds_cleaned, '..', 'soh_charge'))
    soh_discharge_folder = os.path.abspath(os.path.join(cs.ds_cleaned, '..', 'soh_discharge'))
    df = pd.read_csv(file_path)

    #take head and tail indexes
    first_step_index_2 = df[df['Step_Index'] == 2].groupby('Cycle_Index').head(1)
    last_step_index_4 = df[df['Step_Index'] == 4].groupby('Cycle_Index').tail(1)
    
    #pick cycle index numbers
    cycle_indexes2 = first_step_index_2['Cycle_Index'].index
    cycle_indexes4 = last_step_index_4['Cycle_Index'].index

    #take first and last raw
    first = np.array([df.iloc[i, 6] for i in cycle_indexes2])
    last = np.array([df.iloc[i, 6] for i in cycle_indexes4])

    #discard invalid values
    valid_cycles = np.where(np.abs(last - first) > 0.01)[0]
    filtered_vector = (last - first)[valid_cycles]


    cs2x_part = file_path.split('-')[1].split('.csv')[0]
    output_csv_path = os.path.join(soh_charge_folder, f'soh-{cs2x_part}.csv')
    corresponding_cycle_indexes = first_step_index_2['Cycle_Index'].iloc[valid_cycles]

    #define new df
    df_output = pd.DataFrame({'SOH': filtered_vector,
                              'cycle': corresponding_cycle_indexes})
    #save df
    df_output.to_csv(output_csv_path, index=False)

def clear_soh():
    for file_name in os.listdir(cs.sohcharge_root):
        file_path = f'{cs.sohcharge_root}/{file_name}'
        if file_name.startswith('soh'):  
            df = pd.read_csv(file_path)

            i = len(df['SOH']) - 1
            while i > 0:
                difference = abs(df['SOH'].iloc[i] - df['SOH'].iloc[i - 1])
                if difference > 0.01:
                    df = df.drop(index=i)
                i -= 1
            df.to_csv(file_path, index=False)
