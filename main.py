from src.preprocessing.etl import merge_files
import os
from src.utils import constants as cs
from src.preprocessing.hi import make_hi
from src.preprocessing.soh import make_soh, clear_soh
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
    
    if (len(os.listdir(cs.ds_cleaned))) < 1:
        print('cleaning files...')
        make_files()
        print('files cleaned')

    print('creating health indicators files...')
    make_his()
    print('health indicators files created!')

    print('creating soh files...')
    make_sohs()
    print('soh files created!')

    print('cleaning soh files...')
    clear_soh()
    print('soh files cleaned!')

    

if __name__ == '__main__':
    main()
