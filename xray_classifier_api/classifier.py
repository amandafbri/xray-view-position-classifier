import requests
import numpy as np
import tensorflow as tf

from PIL import Image
from io import BytesIO


def classify(request_dict: dict) -> str:

    get_image_from_url = requests.get(request_dict['url_image'])
    img = Image.open(BytesIO(get_image_from_url.content))
    img_resized = img.resize((512, 512))
    img_as_array = np.asarray(img_resized)
    img_normalized = img_as_array/255

    model = tf.keras.models.load_model('autokeras_model/')
    prediction = model.predict(img_normalized)

    prediction_index = np.where(prediction.round() == 1)[0][0]
    classes = {0: 'AP', 1: 'AP_Supine', 2: 'L', 3: 'PA'}
    view_predicted = classes.get(prediction_index)

    return view_predicted
