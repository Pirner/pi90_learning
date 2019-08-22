from __future__ import absolute_import, division, print_function, unicode_literals
from DataIO import StateInterface
import numpy as np
from PIL import Image


import math
import tensorflow as tf
import tensorflow.contrib.keras as keras
from tqdm import tqdm
from DataIO.CustomDataGenerator import DataGenerator


# constants
xmlfile = 'O:/10_Entwicklung/image_database/TESTSET.xml'
img_width = 3023
img_height = 3023
n_epochs = 5
batch_size = 32


def get_image_paths_labels(file):
    paths = []
    labels = []
    # xmlfile = 'G:/dev/images_dev/DataSets/tray_plausibility_set/tray_plausy_set.xml'
    data_manager = StateInterface.StateInterface()
    images = data_manager.readXMLImageList(file)

    print('loading image paths:')
    for img in tqdm(images):
        # labeling the images
        try:
            if img is not None:
                paths.append(img.path)
                labels.append(label_img(img))
        except IOError:
            print('failed to read image!')
            continue
    return paths, labels

# Undefined 0
# Reel 1
# Tray 2
# Stick 3
# Snippet 4
# Wafflepack 5
# Other 6


def label_img_onehot(img):
    if img.PackageType == 'Undefined':
        return [1, 0, 0, 0, 0, 0, 0]
    elif img.PackageType == 'Reel':
        return [0, 1, 0, 0, 0, 0, 0]
    elif img.PackageType == 'Tray':
        return [0, 0, 1, 0, 0, 0, 0]
    elif img.PackageType == 'Stick':
        return [0, 0, 0, 1, 0, 0, 0]
    elif img.PackageType == 'Snippet':
        return [0, 0, 0, 0, 1, 0, 0]
    elif img.PackageType == 'Wafflepack':
        return [0, 0, 0, 0, 0, 1, 0]
    else:
        return [0, 0, 0, 0, 0, 0, 1]

def label_img(img):
    if img.PackageType == 'Undefined':
        return 0
    elif img.PackageType == 'Reel':
        return 1
    elif img.PackageType == 'Tray':
        return 2
    elif img.PackageType == 'Stick':
        return 3
    elif img.PackageType == 'Snippet':
        return 4
    elif img.PackageType == 'Wafflepack':
        return 5
    else:
        return 6


def preprocess_image(file):
    pil_img = Image.open(file)
    pil_img = pil_img.resize((img_width, img_height), Image.BILINEAR)
    np_img = np.array(pil_img, dtype=np.uint16).reshape((img_width * img_height))
    return np_img


def _tf_parse_function(filename, label):
    tmp_img = tf.io.read_file(filename)
    tmp_img = tf.image.decode_png(tmp_img, channels=0, dtype=tf.dtypes.uint16, name=None)
    tmp_img = tf.image.resize(tmp_img, [img_width, img_height])
    return tmp_img, label


def create_batch_generator(X, y, shuffle=False):
    # x is a list of strings which have to be preprocessed
    preprocessed_images = []
    for entry in X:
        preprocessed_images.append(preprocess_image(entry))
    X_copy = np.array(preprocessed_images)
    print('shape of X: ', X_copy.shape)
    y_copy = np.array(y)

    if shuffle:
        data = np.column_stack((X_copy, y_copy))
        np.random.shuffle(data)
        X_copy = data[:, :-1]
        y_copy = data[:, -1].astype(int)

    for i in range(0, X.shape[0], batch_size):
        yield(X_copy[i:i+batch_size, :], y_copy[i:i+batch_size])


def preprocess_batch(x, y):
    n_files = len(x)
    x_copy = []
    for entry in x:
        x_copy.append(preprocess_image(entry))
    x_copy = np.array(x_copy)
    y_copy = np.array(y)
    print(x_copy.shape)
    return x_copy, y_copy


# use image generator functionality
def image_generator(input_path, bs, lb, mode="train", aug=None):
    pil_img = Image.open(file)
    pil_img = pil_img.resize((img_width, img_height), Image.BILINEAR)
    np_img = np.array(pil_img, dtype=np.uint16).reshape((img_width * img_height))


############################################################################################
# script starts
# prepare the datasets
x_train, y_train = get_image_paths_labels(xmlfile)

data_gen_train = DataGenerator(x_train, y_train, batch_size=8, dim=img_width*img_height, n_classes=7, shuffle=False)
data_gen_validate = DataGenerator(x_train, y_train, batch_size=8, dim=img_width*img_height, n_classes=7, shuffle=False)


model = keras.models.Sequential()

model.add(keras.layers.Dense(
    units=50,
    input_dim=img_height*img_width,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    activation='tanh'))

model.add(keras.layers.Dense(
    units=50,
    input_dim=50,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    activation='tanh'))

model.add(keras.layers.Dense(
    units=7,
    input_dim=50,
    kernel_initializer='glorot_uniform',
    bias_initializer='zeros',
    activation='softmax'))

sgd_optimizer = keras.optimizers.SGD(lr=0.001, decay=1e-7, momentum=.9)

model.compile(optimizer=sgd_optimizer, loss='categorical_crossentropy')

n_data_samples = len(x_train)
n_batches = math.ceil(n_data_samples / batch_size)

#for epoch in tqdm(range(n_epochs)):
    # batch_generator = create_batch_generator(x_train, y_train)
    #batch_counter = 0
    #for i in tqdm(range(n_batches - 1)):
        # preprocess stack, so first slice the path and label list
        #slice_from = batch_counter * batch_size
        #slice_to = slice_from + batch_size
        #x_batch = x_train[slice_from:slice_to]
        #y_batch = y_train[slice_from:slice_to]
        #x_batch, y_batch = preprocess_batch(x_batch, y_batch)
        #print('finished preprocessing a batch')
        #history = model.fit(x_batch, y_batch, batch_size=batch_size, epochs=2, verbose=1, validation_split=0.1)
        #history = model.train_on_batch(x_batch, y_batch)
    #for batch_X, batch_y in batch_generator:
        #continue

# model.fit_generator(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=True, workers=1)

model.fit_generator(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=False)
