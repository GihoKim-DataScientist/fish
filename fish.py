import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
#from torch.utils.data import Dataset
import json

info = open('/Users/jiyul/Documents/fish/dataset/labels/train.json')
# 'images'  'annotations'  'categories'
train_info = json.load(info)

images = train_info['images']
annotations = train_info['annotations']
categories = train_info['categories']

print(images[0])
print(annotations[0])

print(categories)



annotation_lst = []
for annotation in annotations:
    annotation_lst.append(annotation['image_id'])

#contain file names that have annotation
fish_images = []
nonfish_images = []

data = {'id': [], 'file': [], 'label':[], 'bbox': []}

for image in images:
    image_id = image['id']

    data['id'].append(image['id'])
    data['file'].append(image['file_name'])

    if image_id in annotation_lst:
        check = 0
        fish_images.append(image['file_name'])
        for annotation in annotations:
            if annotation['image_id'] == image_id:
                if check > 0:
                    data['id'].append(image['id'])
                    data['file'].append(image['file_name'])
                data['label'].append(annotation['category_id'])
                data['bbox'].append(annotation['bbox'])
                check += 1
    else:
        nonfish_images.append(image['file_name'])
        data['label'].append(8)
        data['bbox'].append(None)

df = pd.DataFrame.from_dict(data)
print(df)

train_path = '/Users/jiyul/Downloads/dataset/train/'

# for img in nonfish:
#     image = mpimg.imread(train_path + img)
#     plt.imshow(image)
#     plt.show()


