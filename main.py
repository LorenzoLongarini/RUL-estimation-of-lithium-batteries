from src.preprocessing.etl import merge_files
import os
from src.utils import constants as cs
from src.preprocessing.hi import make_hi
import pandas as pd


def main():
    ds_root = os.listdir(cs.dataset_root)
    # merge files foreach datasets
    for folder in ds_root:
        if folder.startswith('CS2'):
            merge_files(data_dir = f'{cs.dataset_root}/{folder}/ordered', file_name = f'{folder}.csv')   
            merge_files(data_dir = f'{cs.dataset_root}/{folder}/ordered', file_name = f'{folder}.csv', is_charge=False)   
    # make_hi(path=f'{cs.ds_cleaned}/charge-CS2_33.csv')
    # df = pd.read_csv(f'{cs.ds_cleaned}/hi.csv')
    
    # mean = df['hi_v'].mean()
    # # print(mean)
    # std = df['hi_v'].std()
    # hi = pd.DataFrame()
    # for key, value in df.groupby('cycle'):
    #     new_hi = (value['hi_v']- mean) / std
    #     row = pd.DataFrame([{'new_hi': new_hi}])
    #     hi = pd.concat([hi, row])
    # hi.to_csv(f'{cs.ds_cleaned}/hi_v.csv')
    

if __name__ == '__main__':
    main()