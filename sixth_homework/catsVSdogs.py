import argparse
import os
import threading
from datetime import datetime
from io import BytesIO
from multiprocessing.pool import ThreadPool

import numpy as np
import requests
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array


def load_tf_model(path: str) -> keras.Model:
    """
    Load serialized keras model from the directory `path`

    :param path: directory with serialized keras model
    :return: serialized keras model
    """
    print(f"Loading keras model from {path}")
    return keras.models.load_model(path)


def is_cat(model: keras.Model, img: Image) -> bool:
    """
    Returns True if Cat on the picture, Dog otherwise

    :param model: Loaded model for CatVSDog classification
    :param img: PIL PNG image with size 224x224
        example:
        >>> print(img)
        <PIL.PngImagePlugin.PngImageFile image mode=RGB size=224x224 at ...>
    :return:
    """
    img_array = tf.cast(img_to_array(img), tf.float32) / 255.0
    img_expended = np.expand_dims(img_array, axis=0)
    return model.predict(img_expended)[0][0] < 0.5


loaded_files = 0
total_bites = 0
lock = threading.Lock()
cats = 0
dogs = 0


def load_images(url, counter, model):
    try:
        content = requests.get(url)
        global total_bites
        global loaded_files
        global cats
        global dogs
        lock.acquire()
        loaded_files += 1
        total_bites += int(content.headers['Content-length'])
        image = Image.open(BytesIO(content.content))
        image = image.resize((224, 224))
        image.convert()
        print(str(loaded_files) + ' file is loaded')
        if is_cat(model, image):
            directory = os.path.join('images', 'cats', str(counter).rjust(5, '0') + '.png')
            cats += 1
            image.save(directory)
        else:
            directory = os.path.join('images', 'dogs', str(counter).rjust(5, '0') + '.jpeg')
            dogs += 1
            image.save(directory)
        return image
    except:
        return None
    finally:
        lock.release()


def run():
    parser = argparse.ArgumentParser(description='Provide file with URLs.')
    parser.add_argument('file', type=str)
    parser.add_argument('--threads', default=1, type=int)
    args = parser.parse_args()
    file_path, threads = args.file, args.threads

    file = open(file_path)
    urls = file.read().split('\n')

    counter = 0
    if not os.path.exists('./images'):
        os.mkdir('./images')
    if not os.path.exists('./images/cats'):
        os.mkdir('./images/cats')
    if not os.path.exists('./images/dogs'):
        os.mkdir('./images/dogs')
    executor = ThreadPool(threads)
    images = []
    model = load_tf_model(os.path.join('model'))
    for url in urls:
        images.append(executor.apply_async(load_images, (url, counter, model)))
        counter += 1

    for image in images:
        image.get()

    global loaded_files
    global total_bites
    global dogs
    global cats
    print(str(loaded_files) + ' out of ' + str(counter) + ' files were uploaded')
    print(str(total_bites) + ' bites ware uploaded during the script running')
    print(str(counter - loaded_files) + ' errors occurred')
    print(str(dogs / (dogs + cats) * 100) + ' % of dogs')
    print(str(cats / (dogs + cats) * 100) + ' % of cats')


if __name__ == '__main__':
    start_time = datetime.now()
    run()
    print('Total time of execution ' + str(datetime.now() - start_time))
