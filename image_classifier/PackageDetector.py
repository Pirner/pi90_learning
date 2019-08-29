# python system
import random


# learning related
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.models import load_model


# own packages
from utils import get_image_paths_labels, get_image_path_labels_packed, label_img
from utils import DataAnalyzer
from DataIO.CustomDataGenerator import DataGenerator
from image_classifier.Settings import network_params


# analyzing stuff
import matplotlib.pyplot as plt
from tqdm import tqdm
import time


class PackageDetectorCNN(object):
    model = None
    batch_size = 8

    def __init__(self, bs=8):
        self.model = None
        self.batch_size = bs

    def initialize_model(self, model_name='', new=True):
        # create model architecture
        self.model = Sequential()
        self.model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(network_params['img_width'], network_params['img_height'], 1)))
        self.model.add(Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(network_params['n_classes'], activation='softmax'))

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        if new:
            pass

        else:
            self.model = load_model(model_name)

    def load_model_state(self, model_name):
        self.model = load_model(model_name)

    def list_train_model(self, train_list, validation_list, labels, n_elements=50):
        train_data = get_image_path_labels_packed(train_list)
        validation_data = get_image_path_labels_packed(validation_list)

        sample_path, sample_lable = train_data[0]
        print('sample_path: ', sample_path, 'sample_lable: ',sample_lable)

        # data_analyzer = DataAnalyzer()
        # sample_img_preprocessed = data_analyzer.preprocess_image2D_small(sample_path)
        # plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
        # plt.imshow(sample_img_preprocessed, cmap='gray')
        # plt.show()
        # print('sample finished, no training today')


        # shuffle data
        random.shuffle(train_data)
        random.shuffle(validation_data)

        x_train = []
        y_train = []

        x_validate = []
        y_validate = []

        train_data_size = len(train_data)

        valDataSize = len(validation_data)

        labels_processed = []
        # now pick of of each label 50 sample data
        for label in labels:
            counter = 0
            n_samples = 0
            while n_samples < n_elements:
                if n_samples > n_elements:
                    break

                if counter >= train_data_size - 1:
                    break

                path, img_label = train_data[counter]
                if img_label == label:
                    x_train.append(path)
                    y_train.append(img_label)
                    n_samples += 1

                counter += 1

        for label in labels:
            counter = 0
            n_samples = 0
            while n_samples < n_elements:
                if n_samples > n_elements:
                    break

                if counter >= train_data_size:
                    break

                path, img_label = validation_data[counter]
                if img_label == label:
                    x_validate.append(path)
                    y_validate.append(img_label)
                    n_samples += 1

                counter += 1

        data_gen_train = DataGenerator(
                x_train,
                y_train,
                batch_size=self.batch_size,
                dim=(network_params['img_width'], network_params['img_height']),
                n_classes=network_params['n_classes'],
                shuffle=False,
                normalize=True
        )

        data_gen_validate = DataGenerator(
            x_validate,
            y_validate,
            batch_size=self.batch_size,
            dim=(network_params['img_width'], network_params['img_height']),
            n_classes=network_params['n_classes'],
            shuffle=False
        )

        self.model.fit_generator(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=False, epochs=5)

    def list_train_model_all_images(self, train_list, validation_list):
        x_train, y_train = get_image_paths_labels(train_list)
        x_validate, y_validate = get_image_paths_labels(validation_list)

        # filter to make even data sets (at least for training and validation)

        data_gen_train = DataGenerator(
            x_train,
            y_train,
            batch_size=self.batch_size,
            dim=(network_params['img_width'], network_params['img_height']),
            n_classes=network_params['n_classes'],
            shuffle=False
        )

        data_gen_validate = DataGenerator(
            x_validate,
            y_validate,
            batch_size=self.batch_size,
            dim=(network_params['img_width'], network_params['img_height']),
            n_classes=network_params['n_classes'],
            shuffle=False
        )

        self.model.fit_generator(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=False, epochs=5)

    def predict_single(self, x):
        ret = self.model.predict(x)
        return ret

    def save_model(self, model_name):
        self.model.save(model_name)

def initialize_and_train_net_network(network, list_path_train, list_path_validation, labels)
    print('Initializing CNN-Model...')
    network.initialize_model()
    print('Finished init')

    print('starting to train on: ', list_path_train)
    package_detector_cnn.list_train_model(list_path_train, list_path_validation, classifier_labels)
    print('finished training model.')
    print('saving model...')
    package_detector_cnn.save_model(network_params['model_name'])
    print('finished saving model')


package_detector_cnn = PackageDetectorCNN()
package_detector_cnn.initialize_model()
classifier_labels = [1, 2, 3]
xml_file = 'O://10_Entwicklung/image_database/learning_set_cnn_prototype.xml'


#print('Started Training')
# package_detector_cnn.list_train_model_all_images(xml_file, xml_file)
# classifier_labels = ['Reel', 'Tray', 'Stick']


#package_detector_cnn.list_train_model(xml_file, xml_file, classifier_labels)
#print('Finished Training')

#print('save model')
#package_detector_cnn.save_model(network_params['model_name'])

#print('load model')
#package_detector_cnn.load_model_state(network_params['model_name'])

#x_train_samples, y_train_samples = get_image_paths_labels(xml_file)
#x1 = x_train_samples[len(x_train_samples) - 2]
#print('path here: ', x1)
#data_analyzer = DataAnalyzer()
#x1 = data_analyzer.preprocess_image_cnn(x1)
#print('selected path: ', x_train_samples[0])
#print('training a sample')
#ret = package_detector_cnn.predict_single(x1)
#print('previous: ', ret)
#n_files = len(x_train_samples)

#n_false = 0
#n_right = 0

#for i in tqdm(range(n_files)):
    #print('\nselecting new file for prediction')
    #x = x_train_samples[i]
    #y = y_train_samples[i]

    #x = data_analyzer.preprocess_image_cnn(x)
    #pred = package_detector_cnn.predict_single(x1)
    #print('pred: ', pred, '\nassigned_label: ', y)
    #time.sleep(5)
    # break

# print('Finish predicting list.')

