import os
import shutil

import pandas as pd
import numpy as np

metadata = pd.read_csv(
        'C:/Users/amand/Desktop/Projects/covid-chestxray-dataset/metadata.csv',
        usecols=['view', 'modality', 'filename']
    )

metadata = metadata[metadata.modality == 'X-ray'].drop(['modality'], axis=1)

metadata.value_counts('view')
# PA: 344, AP Supine: 234, AP: 203, L: 84, AP Erect: 1

# There is just one example of this view
metadata = metadata[metadata.view != 'AP Erect']

# Labels must start with a letter and contain only letters, numbers and underscores
metadata['view'] = metadata['view'].apply(lambda x: x.replace(' ', '_'))

# Split into 80/10/10
train, validation, test = np.split(
        metadata.sample(frac=1, random_state=0), [int(.8*len(metadata)), int(.9*len(metadata))]
    )

# Remember to check if there are examples of all labels in all sets
train['view'].value_counts()
validation['view'].value_counts()
test['view'].value_counts()

# Organize files
os.mkdir('data')
os.mkdir('data/Train')
os.mkdir('data/Validation')
os.mkdir('data/Test')

for label in train['view'].unique():
    os.mkdir(f'data/Train/{label}')
    os.mkdir(f'data/Validation/{label}')
    os.mkdir(f'data/Test/{label}')

for example in train.iterrows():
    file = example[1]['filename']
    label = example[1]['view']
    shutil.copy(f'C:/Users/amand/Desktop/Projects/covid-chestxray-dataset/images/{file}', f'data/Train/{label}')

for example in validation.iterrows():
    file = example[1]['filename']
    label = example[1]['view']
    shutil.copy(f'C:/Users/amand/Desktop/Projects/covid-chestxray-dataset/images/{file}', f'data/Validation/{label}')

for example in test.iterrows():
    file = example[1]['filename']
    label = example[1]['view']
    shutil.copy(f'C:/Users/amand/Desktop/Projects/covid-chestxray-dataset/images/{file}', f'data/Test/{label}')
