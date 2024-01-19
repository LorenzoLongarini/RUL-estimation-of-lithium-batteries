import pandas as pd
import os
from src.utils import constants as cs

def normalize(path):
    df = pd.read_csv(path)
    df[cs.index] = df.index
    max_voltage = df[cs.voltage].max()
    min_voltage = df[cs.voltage].min()
    t0_voltage = 3.8
    t1_voltage = 4.1999
    for key, group in df.groupby(cs.c_index):
        t0_index = (group[cs.voltage] >= t0_voltage).idxmax()
        t1_index = (group[cs.voltage] >= t1_voltage).idxmax()
        group[cs.voltage] = (group[cs.voltage] - min_voltage) / (max_voltage - min_voltage)
        
        mean_voltage = group[cs.voltage].mean()
        std_voltage = group[cs.voltage].std()
        group[cs.voltage] = (group[cs.voltage]- mean_voltage) / std_voltage
        selected_rows = group[(group[cs.index] >= t0_index) & (group[cs.index] <= t1_index)]
        hi_v = selected_rows[cs.voltage].sum()
        # hi_v = np.trapz(selected_rows[voltage])
    cycle = group[cs.c_index].iloc[0]
    
    row = pd.DataFrame([{'hi_v': hi_v, 'cycle': cycle}])
    hi = pd.concat([hi, row])