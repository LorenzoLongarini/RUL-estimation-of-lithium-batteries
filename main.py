from src.preprocessing.etl import merge_files
import os
from src.utils import constants as cs
from src.preprocessing.hi import make_hi
import pandas as pd


def make_files():
    ds_root = os.listdir(cs.dataset_root)
    # merge files foreach datasets
    for folder in ds_root:
        if folder.startswith('CS2'):
            merge_files(data_dir = f'{cs.dataset_root}/{folder}/ordered', file_name = f'{folder}.csv')   
            merge_files(data_dir = f'{cs.dataset_root}/{folder}/ordered', file_name = f'{folder}.csv', is_charge=False)  

def make_his():
    ds_root = os.listdir(cs.ds_cleaned)
    for folder in ds_root:
        if folder.startswith('charge'):
            make_hi(path=f'{cs.ds_cleaned}/{folder}', file_name=folder)

def main():
    make_files()
    make_his()
    

if __name__ == '__main__':
    main()
