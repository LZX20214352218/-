import pandas as pd
import os
from sklearn.model_selection import train_test_split


def split_dataset(data_file):
    # 展示不同的调用方式
    data = pd.read_csv(data_file, header=None, sep=' ')
    train_dataset, eval_dataset = train_test_split(data, test_size=0.2, random_state=42)
    print(f'train dataset len: {train_dataset.size}')
    print(f'eval dataset len: {eval_dataset.size}')
    train_filename = 'train_' + data_file.split('.')[0] + '.txt'
    eval_filename = 'eval_' + data_file.split('.')[0] + '.txt'
    train_dataset.to_csv(train_filename, index=None, header=None, sep=' ')
    eval_dataset.to_csv(eval_filename, index=None, header=None, sep=' ')


data_file = 'train_period.txt'
split_dataset(data_file)