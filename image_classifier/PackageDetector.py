# python system
import random


# learning related
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.models import load_model


# own packages
from utils import get_image_paths_labels, get_image_path_labels_packed, label_img
from DataIO.CustomDataGenerator import DataGenerator
from image_classifier.Settings import network_params


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
        self.model.add(Dense(7, activation='softmax'))

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        if new:
            pass

        else:
            self.model = load_model(model_name)

    def list_train_model(self, train_list, validation_list, labels, n_elements=50):
        train_data = get_image_path_labels_packed(train_list)
        validation_data = get_image_path_labels_packed(validation_list)

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

                if counter >= train_data_size - 1:
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
                n_classes=7,
                shuffle=False
            )

        data_gen_validate = DataGenerator(
            x_validate,
            y_validate,
            batch_size=self.batch_size,
            dim=(network_params['img_width'], network_params['img_height']),
            n_classes=7,
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
            n_classes=7,
            shuffle=False
        )

        data_gen_validate = DataGenerator(
            x_validate,
            y_validate,
            batch_size=self.batch_size,
            dim=(network_params['img_width'], network_params['img_height']),
            n_classes=7,
            shuffle=False
        )

        self.model.fit_generator(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=False, epochs=5)

    def save_model(self, model_name):
        self.model.save(model_name)


package_detector_cnn = PackageDetectorCNN()
package_detector_cnn.initialize_model()

xml_file = 'O://10_Entwicklung/image_database/learning_set_cnn_prototype.xml'

print('Started Training')
package_detector_cnn.list_train_model_all_images(xml_file, xml_file)
print('Finished Training')

print('save model')
package_detector_cnn.save_model(network_params['model_name'])
