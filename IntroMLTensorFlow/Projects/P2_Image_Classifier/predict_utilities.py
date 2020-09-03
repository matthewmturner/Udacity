from PIL import Image
import numpy as np
import tensorflow as tf


def predict(image_path, model, top_k):
    image = Image.open(image_path)
    np_image = np.asarray(image)
    processed_image = np.expand_dims(process_image(np_image), axis=0)
    predictions = model.predict(processed_image)
    prob_classes = predictions[0].argsort()[-top_k:][::-1]
    probs = [predictions[0][i] for i in prob_classes]
    return probs, prob_classes


def process_image(image):
    tensor = tf.convert_to_tensor(image, tf.float32)
    tensor = tf.image.resize(tensor, (224, 224))
    tensor /= 255
    return tensor.numpy()
