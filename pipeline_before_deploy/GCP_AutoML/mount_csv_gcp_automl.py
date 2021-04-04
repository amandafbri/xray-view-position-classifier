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

train['ML_USE'] = 'train'
validation['ML_USE'] = 'validation'
test['ML_USE'] = 'test'

metadata_for_automl = pd.concat([train, validation, test], ignore_index=True)
metadata_for_automl = metadata_for_automl[metadata_for_automl.columns[::-1]]
metadata_for_automl = metadata_for_automl.rename(columns={'filename': 'GCS_FILE_PATH', 'view': 'LABEL'})

metadata_for_automl['GCS_FILE_PATH'] = metadata_for_automl['GCS_FILE_PATH'].apply(lambda x: 'gs://my-bucket/data/' + x)

metadata_for_automl.to_csv('metadata_for_automl.csv', header=None, index=False)
