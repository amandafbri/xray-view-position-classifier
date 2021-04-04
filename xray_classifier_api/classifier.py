import requests
import numpy as np
import tensorflow as tf

from PIL import Image
from io import BytesIO
from autokeras.keras_layers import CastToFloat32


def classify(request_dict: dict) -> str:
    view_predicted = ''
    url_image = request_dict.get('url_image')

    if url_image:
        get_image_from_url = requests.get(url_image)
        img = Image.open(BytesIO(get_image_from_url.content))
        img = img.convert('RGB')
        img_resized = img.resize((512, 512))
        img_as_array = np.asarray(img_resized)
        img_adjusted = np.expand_dims(img_as_array, axis=0)

        model = tf.keras.models.load_model(
            'xray_classifier_api/autokeras_model/bestmodel_v2.h5',
            custom_objects={'CastToFloat32': CastToFloat32}
            )
        prediction = model.predict(img_adjusted)

        prediction_index = np.where(prediction.round()[0] == 1)[0][0]
        classes = {0: 'AP', 1: 'AP_Supine', 2: 'L', 3: 'PA'}
        view_predicted = classes.get(prediction_index)

    return view_predicted
