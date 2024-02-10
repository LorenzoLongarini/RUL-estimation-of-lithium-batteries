import pandas as pd
import os
from src.utils import constants as cs
import numpy as np
from scipy.integrate import simps

def make_hi(path, file_name):
    #initialize dataframes
    hiv = pd.DataFrame()
    hii = pd.DataFrame()

    #define different df for hiv and hii
    df_hiv = pd.read_csv(path)
    df_hiv[cs.index] = df_hiv.index
    df_hii = df_hiv
    df_hiv = df_hiv[(df_hiv[cs.step_index] == 2)]
    df_hii = df_hii[(df_hii[cs.step_index] == 4)]
    df_hiv = df_hiv[(df_hiv[cs.voltage] >= 3.8) & (df_hiv[cs.voltage] <= 4.2001)]

    #integrate voltage through time and convert into Voltage/hour
    for key, group in df_hiv.groupby(cs.c_index):
        group[cs.test_time]=group[cs.test_time]/1000.0
        # t0 = group[cs.test_time].iloc[0]
        # t1 = group[cs.test_time].iloc[-1]
        # high = t1 - t0
        # minor_base = group[cs.voltage].iloc[0]
        # major_base = group[cs.voltage].iloc[-1]
        # hi_v = ((major_base + minor_base) * high) / 2

        hi_v = simps(group[cs.voltage], x=group[cs.test_time])
        # hi_v = np.trapz(group[cs.voltage], x=group[cs.test_time])
        cycle = group[cs.c_index].iloc[0]

        row = pd.DataFrame([{'hi_v': hi_v, 'cycle': cycle}])
        hiv = pd.concat([hiv, row])

    #integrate current through time and convert into Current/hour
    for key, group in df_hii.groupby(cs.c_index):
        hi_i = simps(group[cs.current], x=group[cs.test_time]/1000.0)
        cycle = group[cs.c_index].iloc[0]
        row = pd.DataFrame([{'hi_i': hi_i, 'cycle': cycle}])
        hii = pd.concat([hii, row])

    # Salva il DataFrame come CSV senza l'indice
    hiv.to_csv(f'{cs.ds_hi}/hiv-{file_name}', index=False)
    hii.to_csv(f'{cs.ds_hi}/hii-{file_name}', index=False)
