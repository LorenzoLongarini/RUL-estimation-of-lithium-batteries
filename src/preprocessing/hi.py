import pandas as pd
import os
from src.utils import constants as cs
import numpy as np
from datetime import datetime

def make_hi(path):
    hi = pd.DataFrame()

    df = pd.read_csv(path)
    df[cs.index] = df.index
    df = df[(df[cs.step_index] == 2)]
    df = df[(df[cs.voltage] >= 3.8) & (df[cs.voltage] <= 4.2001)]
    max_voltage = df[cs.voltage].max()
    min_voltage = df[cs.voltage].min()

    date_format = "%Y-%m-%d %H:%M:%S"
    for key, group in df.groupby(cs.c_index):

        # group[cs.date_time] = datetime.strptime(group[cs.date_time], date_format)   
        group[cs.date_time] = group[cs.date_time].apply(lambda x: datetime.strptime(x, date_format))  
        
        # mean_voltage = group[cs.voltage].mean()
        # std_voltage = group[cs.voltage].std()
        # group[cs.voltage] = (group[cs.voltage]- mean_voltage) / std_voltage
        # selected_rows = group[(group[cs.index] >= t0_index) & (group[cs.index] <= t1_index)]
        group[cs.voltage] = (group[cs.voltage] - min_voltage) / (max_voltage - min_voltage)
        timestamps = (group[cs.date_time] - datetime(1970, 1, 1)).dt.total_seconds().values
        # Converti la stringa in un oggetto datetime
        print(timestamps)
        # hi_v = selected_rows[cs.voltage].sum()
        hi_v = np.trapz(group[cs.voltage], x=timestamps)#group[cs.date_time])
        hi_v_hour = hi_v / 3600.0
        cycle = group[cs.c_index].iloc[0]
    
        row = pd.DataFrame([{'hi_v': hi_v_hour, 'cycle': cycle}])
        hi = pd.concat([hi, row])
    hi.to_csv(f'{cs.ds_cleaned}/hi.csv')
