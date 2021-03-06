import numpy as np
import keras
# from tensorflow.python.keras.utils.data_utils import Sequence
from keras.utils import Sequence
from PIL import Image
from image_classifier.Settings import  network_params
import tqdm


def normalize_data(arr):
    mean = arr.mean()
    std = arr.std()
    x = lambda a: (a - mean) / std
    return x(arr)

def preprocess_image(file):
    pil_img = Image.open(file)
    pil_img = pil_img.resize((network_params['img_width'], network_params['img_height']), Image.BILINEAR)
    np_img = np.array(pil_img, dtype=np.uint16).reshape((network_params['img_width'] * network_params['img_height']))
    return np_img


def preprocess_image_cnn(file):
    np_img = np.zeros(shape=(network_params['img_width'], network_params['img_height'], 1))
    try:
        pil_img = Image.open(file)
        pil_img = pil_img.resize((network_params['img_width'], network_params['img_height']), Image.BILINEAR)
        np_img = np.array(pil_img, dtype=np.uint16).reshape((network_params['img_width'], network_params['img_height'], 1))
        np_img = normalize_data(np_img)
    except IOError as e:
        print('failed pre processing file: ', file)
        img = Image.fromarray(np_img)
        img.save('failed_image.png')

    return np_img

def preprocess_image_cnn_predict(file):
    np_img = np.zeros(shape=(network_params['img_width'], network_params['img_height'], 1))
    try:
        pil_img = Image.open(file)
        pil_img = pil_img.resize((network_params['img_width'], network_params['img_height']), Image.BILINEAR)
        np_img = np.array(pil_img, dtype=np.uint16).reshape((1, network_params['img_width'], network_params['img_height'], 1))
        np_img = normalize_data(np_img)
    except IOError as e:
        print('failed pre processing file: ', file)
        img = Image.fromarray(np_img)
        img.save('failed_image.png')

    return np_img


def preprocess_batch(x, y):
    #n_files = len(x)
    x_copy = []
    for entry in x:
        x_copy.append(preprocess_image(entry))
    x_copy = np.array(x_copy)
    y_copy = np.array(y)
    print(x_copy.shape)
    return x_copy, y_copy


class DataGenerator(Sequence):
    'Generates data for Keras'
    def __init__(self, list_IDs, labels, batch_size=32, dim=(32, 32, 32), n_channels=1,
                 n_classes=10, shuffle=True, normalize=False, normalize_all=False):
        'Initialization'
        self.dim = dim
        self.batch_size = batch_size
        self.labels = labels
        self.list_IDs = list_IDs
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.on_epoch_end()
        self.normalize = normalize
        self.mean = 0
        self.std = 0

        # normalize data if requested
        if normalize_all:
            self.normalize_data_all()

        sample_list = [1, 2, 3]
        sample_list = np.array(sample_list)
        self.normalize_data(sample_list)

    def normalize_data_all(self):
        self.mean = 0
        self.std = 0
        # first compute the mean of every single image:
        means = []
        for image_path in tqdm.tqdm(self.list_IDs):
            data = preprocess_image_cnn(image_path)
            means.append(data.mean())

        n_entries = len(means)
        means = np.array(means)

        aux_sum = 0
        for i in tqdm.tqdm(range(n_entries)):
            aux_sum += means[i] / n_entries

        final_mean = means.mean()

        counter = 0
        aux_mean = 0

        for i in tqdm.tqdm(range(n_entries)):
            aux_mean += means[i]
            counter += 1

        aux_mean = aux_mean / counter

        print('mean successful computed')

    def get_label_of_image(self, img_path):
        i = 0
        fail = -1
        for path in self.list_IDs:
            if path == img_path:
                return i
            i += 1
        return fail

    def __len__(self):
        'Denotes the number of batches per epoch'
        return int(np.floor(len(self.list_IDs) / self.batch_size))

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]

        # Find list of IDs
        list_IDs_temp = [self.list_IDs[k] for k in indexes]

        # Generate data
        X, y = self.__data_generation(list_IDs_temp)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        'Generates data containing batch_size samples' # X : (n_samples, *dim, n_channels)
        # Initialization
        X = np.empty(shape=(self.batch_size, network_params['img_width'], network_params['img_height'], 1))
        y = np.empty(self.batch_size, dtype=int)

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            # Store sample
            X[i, ] = preprocess_image_cnn(ID)

            # Store class
            index = self.get_label_of_image(ID)
            if index >= 0:
                #y[i] = np.array(self.labels[ID])
                y[i] = self.labels[index]
            else:
                y[i] = 0

        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)
        #return X, y

    def normalize_data(self, arr):
        mean = arr.mean()
        std = arr.std()
        x = lambda a: (a - mean) / std
        return x(arr)
