import os
import uuid
from django.conf import settings
import tensorflow as tf
from django.http import JsonResponse
# from keras.preprocessing import image
import numpy as np
from django.core.files.storage import FileSystemStorage
# from tensorflow.keras.preprocessing import image
import random
import string



# model_path = os.path.join(os.path.dirname(__file__), 'C:/Users/Asante/Documents/final year project/model/', 'lung_cancer.h5')
model = tf.keras.models.load_model('/home/ltabari/Desktop/FInal year/project trials/Final Project/fruit_model.h5')

# model = tf.keras.models.load_model(model_path)
# model = load_model(model_path)



def predict_fruit(uploaded_image):
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
    filename = fs.save(uploaded_image.name, uploaded_image)

    img_path = os.path.join(settings.MEDIA_ROOT, filename)
    img = tf.keras.utils.load_img(img_path, target_size=(180, 180))
    img_arr = tf.keras.utils.img_to_array(img)
    img_arr = tf.expand_dims(img_arr, 0)
    img_arr = img_arr / 255

    predictions = model.predict(img_arr)
    predicted_class = np.argmax(predictions)
    score = tf.nn.softmax(predictions[0])
   
    classes = ['Ripe_banana', 'Ripe_oranges', 'Ripe_tomatoes','Rotten_banana','Unripe_banana','Unripe_tomatoes']
    prediction_label = classes[predicted_class]
    pred= classes[np.argmax(score)]


    # Construct the full image path including the base URL
    # image_url = settings.MEDIA_URL + filename
    # Construct the full image path on the local file system
    image_path = os.path.abspath(img_path)

    result = {
        "prediction": prediction_label,
        'accuracy': '{:.2f}'.format(100 * np.max(score)),
        "image_path": image_path  # Include the full image path
    }

    return result

