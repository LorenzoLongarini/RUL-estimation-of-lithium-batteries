import pandas as pd
import os
from src.utils import constants as cs
import numpy as np

def make_hi(path):
    hi = pd.DataFrame()

    df = pd.read_csv(path)
    df[cs.index] = df.index
    df = df[(df[cs.step_index] == 2)]
    df = df[(df[cs.voltage] >= 3.8) & (df[cs.voltage] <= 4.2001)]
    max_voltage = df[cs.voltage].max()
    min_voltage = df[cs.voltage].min()

    for key, group in df.groupby(cs.c_index):

        
        # mean_voltage = group[cs.voltage].mean()
        # std_voltage = group[cs.voltage].std()
        # group[cs.voltage] = (group[cs.voltage]- mean_voltage) / std_voltage
        # selected_rows = group[(group[cs.index] >= t0_index) & (group[cs.index] <= t1_index)]
        group[cs.voltage] = (group[cs.voltage] - min_voltage) / (max_voltage - min_voltage)
        print(group)
        # hi_v = selected_rows[cs.voltage].sum()
        hi_v = np.trapz(group[cs.voltage])
        cycle = group[cs.c_index].iloc[0]
    
        row = pd.DataFrame([{'hi_v': hi_v, 'cycle': cycle}])
        hi = pd.concat([hi, row])
    hi.to_csv(f'{cs.ds_cleaned}/hi.csv')
