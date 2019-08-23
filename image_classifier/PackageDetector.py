from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.models import load_model


# own packages
from utils import get_image_paths_labels
from DataIO.CustomDataGenerator import DataGenerator


net_parameters = {
    'img_width': 3023,
    'img_height': 3023
}


class PackageDetectorCNN(object):
    model = None
    batch_size = 8

    def __init__(self, bs=8):
        self.model = None
        self.batch_size = bs

    def initialize_model(self, model_name='', new=True):
        # create model architecture
        self.model = Sequential()
        self.model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(net_parameters['img_width'], net_parameters['img_height'], 1)))
        self.model.add(Conv2D(32, kernel_size=3, activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(10, activation='softmax'))

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        if new:
            pass

        else:
            self.model = load_model(model_name)

    def list_train_model(self, train_list, validation_list):
        x_train, y_train = get_image_paths_labels(train_list)
        x_validate, y_validate = get_image_paths_labels(validation_list)

        data_gen_train = DataGenerator(
            x_train,
            y_train,
            batch_size=self.batch_size,
            dim=(net_parameters['img_width'], net_parameters['img_height']),
            n_classes=7,
            shuffle=False
        )

        data_gen_validate = DataGenerator(
            x_validate,
            y_validate,
            batch_size=self.batch_size,
            dim=(net_parameters['img_width'], net_parameters['img_height']),
            n_classes=7,
            shuffle=False
        )

        self.model.fit(generator=data_gen_train, validation_data=data_gen_validate, use_multiprocessing=False, epochs=5)


package_detector_cnn = PackageDetectorCNN()
package_detector_cnn.initialize_model()

xml_file = 'O:/10_Entwicklung/image_database/TESTSET.xml'

print('Started Training')
package_detector_cnn.list_train_model(xml_file, xml_file)
print('Finished Training')

