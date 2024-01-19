from src.preprocessing.etl import merge_files
import os
from src.utils import constants as cs


def main():
    ds_root = os.listdir(cs.dataset_root)
    # merge files foreach datasets
    for folder in ds_root:
        if folder.startswith('CS2'):
            merge_files(data_dir = f'{cs.dataset_root}/{folder}', file_name = f'{folder}.csv')   

if __name__ == '__main__':
    main()