from src.preprocessing.etl import merge_files
import os
from src.utils import constants as cs
from src.preprocessing.hi import make_hi
from src.preprocessing.soh import make_soh
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

def make_sohs():
    ds_root = os.listdir(cs.ds_cleaned)
    for folder in ds_root:
        if folder.startswith('charge'):
            make_soh(file_path=f'{cs.ds_cleaned}/{folder}')

def main():
    # make_files()
    # make_his()
    make_sohs()
    

if __name__ == '__main__':
    main()
