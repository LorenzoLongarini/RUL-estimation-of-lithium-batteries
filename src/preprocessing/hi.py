import pandas as pd
import os
from src.utils import constants as cs
import numpy as np

def make_hi(path, file_name):
    hi = pd.DataFrame()

    df_hiv = pd.read_csv(path)
    df_hiv[cs.index] = df_hiv.index
    df_hii = df_hiv
    df_hiv = df_hiv[(df_hiv[cs.step_index] == 2)]
    df_hii = df_hii[(df_hii[cs.step_index] == 4)]
    df_hiv = df_hiv[(df_hiv[cs.voltage] >= 3.8) & (df_hiv[cs.voltage] <= 4.2001)]

    for key, group in df_hiv.groupby(cs.c_index):
        hi_v = np.trapz(group[cs.voltage], x=group[cs.test_time])
        hi_v_hour = hi_v / 3600.0
        cycle = group[cs.c_index].iloc[0]

        row = pd.DataFrame([{'hi_v': hi_v_hour, 'cycle': cycle}])
        hi = pd.concat([hi, row])

    for key, group in df_hii.groupby(cs.c_index):
        hi_i = np.trapz(group[cs.current], x=group[cs.test_time])
        hi_i_hour = hi_i / 3600.0
        cycle = group[cs.c_index].iloc[0]

        # Aggiungi la colonna hi_i solo se è presente nel DataFrame
        if 'hi_i' in hi.columns:
            hi.loc[hi['cycle'] == cycle, 'hi_i'] = hi_i_hour
        else:
            row = pd.DataFrame([{'hi_i': hi_i_hour, 'cycle': cycle}])
            hi = pd.concat([hi, row])

    # Riempi eventuali valori mancanti con 0
    hi = hi.fillna(0)

    # Salva il DataFrame come CSV senza l'indice
    hi.to_csv(f'{cs.ds_hi}/hi-{file_name}', index=False)
