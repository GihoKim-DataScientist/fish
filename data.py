import os
from PIL import Image
import torch
from torch.utils.data import Dataset
import pandas as pd

class FishDataset(Dataset):
    def __init__(self, img_labels, img_dir, transform=None, target_transform=None):
        """
        Args:
            annotations_file (string): Path to the annotations file.
            img_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on a sample.
            target_transform (callable, optional): Optional transform to be applied to the label.
        """
        self.img_labels = pd.read_csv(img_labels, usecols = ['id', 'file', 'label', 'bbox'])
        print(self.img_labels)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 1])
        image = Image.open(img_path).convert('RGB')
        label = self.img_labels.iloc[idx, 2]
        bbox = self.img_labels.iloc[idx, 3]

        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label = self.target_transform(label)

        return image, label
