import os
import struct
import numpy as np

from DataIO import StateInterface
import tqdm


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels.idx1-ubyte' % kind)
    images_path = os.path.join(path,
                               '%s-images.idx3-ubyte' % kind)

    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack(">IIII",
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)
        images = ((images / 255.) - .5) * 2

    return images, labels


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