import pandas as pd
from src.utils import constants as cs

def make_soh(path:str=''):
    # charge csv from path and initialize capacities
    df = pd.read_csv(path)

    values = [value[cs.charge_cap].max() for key, value in df.groupby(cs.white_list[1])]
    perc = [i / 1.35 * 100 for i in values]
    return perc