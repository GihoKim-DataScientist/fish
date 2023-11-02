import data 
import os
from PIL import Image
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import pandas as pd

train_data = data.FishDataset('/Users/jiyul/Documents/fish/fish.csv', '/Users/jiyul/Documents/fish/dataset/train')

train_loader = DataLoader(train_data, batch_size = 4, shuffle = True, num_workers=0)
train_features, train_labels = next(iter(train_loader))
print(train_features)
print(train_labels)

if __name__ == '__main__':
    main()
