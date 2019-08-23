import os
import struct
import numpy as np

import tqdm
import csv

from DataIO import StateInterface
from image_classifier.DTO.AlgorithmDefinitionOption import AlgorithmDefinitionOption
from image_classifier.DTO.Algorithm import Algorithm


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
    for img in images:
        # labeling the images
        try:
            if img is not None:
                paths.append(img.path)
                labels.append(label_img(img))
        except IOError:
            print('failed to read image!')
            continue
    return paths, labels


def CreateCSV(path):
    header = []
    header.append('Status')
    header.append('ReelCenterX')
    header.append('ReelCenterY')
    header.append('ReelCenterRefinedX')
    header.append('ReelCenterRefinedY')
    #header.append('PartSize?!?!')
    header.append('HasMultiCounts')
    header.append('ComponentCount')
    header.append('MinReelRadius')
    header.append('MinReelRadiusConfidence')
    header.append('MaxReelRadius')
    header.append('MaxReelRadiusConfidence')
    header.append('ResultImageIsOverlay')
    header.append('AutoComponentWidth')
    header.append('AutoComponentHeight')
    header.append('AutoComponentDepth')
    header.append('AutoOuterRadius')
    header.append('AutoInnerRadius')
    header.append('Insecurity')
    header.append('AppliedThreshold')
    header.append('ReelDiameter')
    header.append('ReelHubDiameter')
    header.append('IPModuleID')
    header.append('SmallPartsCorrection')

    with open(path, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(header)

def strOptionsToAlgorithmDefinitionOptions(str):
    # split string for each option:
    options = str.split()
    algOption = AlgorithmDefinitionOption()
    for option in options:
        if (option == 'None'):
            return AlgorithmDefinitionOption()

        elif (option == 'UseContrastEnhancement'):
            algOption.UseContrastEnhancement = True

        elif (option == 'UseThresholdAdjust'):
            algOption.UseThresholdAdjust = True

        elif (option == 'UseSizeHints'):
            algOption.UseSizeHints = True

        elif (option == 'UseClosing'):
            algOption.UseClosing = True

        elif (option == 'UseMultiThreshold'):
            algOption.UseMultiThreshold = True

        elif (option == 'AllowMultiCounts'):
            algOption.AllowMultiCounts = True

        elif (option == 'Option9'):
            algOption.Option9 = True

        elif (option == 'Option10'):
            algOption.Option10 = True

        elif (option == 'Option11'):
            algOption.Option11 = True

        elif (option == 'Option13'):
            algOption.Option13 = True

        elif (option == 'Option14'):
            algOption.Option14 = True

        elif (option == 'Option15'):
            algOption.Option15 = True
        else:
            print(option + ' not caught up yet.')

        return algOption

def setExpertParameters(optimizer, expPar):
    pass


def setAlgorithmDefinition(optimizer, aod):
    optimizer.SetAlgorithmDefinitionAlgorithm(aod.Algorithm)
    optimizer.SetAlgorithmDefinitionIsNew(aod.IsNew)
    optimizer.SetAlgorithmDefinitionConvertedFromOldVersion(aod.ConvertedFromOldVersion)
    optimizer.SetAlgorithmDefinitionWidthHint(aod.WidthHint)
    optimizer.SetAlgorithmDefinitionHeightHint(aod.HeightHint)
    optimizer.SetAlgorithmDefinitionSizeHint(aod.SizeHint)
    optimizer.SetAlgorithmDefinitionLayerThickness(aod.LayerThickness)
    optimizer.SetAlgorithmDefinitionPitchHint(aod.PitchHint)
    optimizer.SetAlgorithmDefinitionMeasurementProbability(aod.MeasurementProbability)


def setNewImageInfo(optimizer, info):
    # set default values:
    optimizer.SetDefaultValues()

    # set all values from the read image info from the xml file
    optimizer.SetComponentWidth(info.MeasuredWidth)
    optimizer.SetComponentHeight(info.MeasuredHeight)
    optimizer.SetReelLayerThickness(info.LayerThickness)
    #optimizer.SetLayerPitch(info.Pitch)
    optimizer.SetCenterX(info.CenterX)
    optimizer.SetCenterY(info.CenterY)

    optimizer.SetMinReelRadius(15)
    optimizer.SetImagePath(info.path)
    setAlgorithmDefinition(optimizer, info.AlgorithmDefinition)

    pass


def StringToAlgorithm(str):
    ret = Algorithm.NotDefined
    if (str is None):
        ret = Algorithm.OCGenericCounter
        return ret

    if (str == 'IISResistorCounter'):
        ret = Algorithm.IISResistorCounter

    elif (str == 'IISCapacityCounter'):
        ret = Algorithm.IISCapacityCounter

    elif (str == 'IISMelfCounter'):
        ret = Algorithm.IISMelfCounter

    elif (str == 'IISElkoCounter'):
        ret = Algorithm.IISElkoCounter

    elif (str == 'IISIcCounter'):
        ret = Algorithm.IISIcCounter

    elif (str == 'IISSotCounter'):
        ret = Algorithm.IISSotCounter

    elif (str == 'IISOptoCounter'):
        ret = Algorithm.IISOptoCounter

    elif (str == 'IISElkoLargeCounter'):
        ret = Algorithm.IISElkoLargeCounter

    elif (str == 'IISIcModCounter'):
        ret = Algorithm.IISIcModCounter

    elif (str == 'IISResistorNewCounter'):
        ret == Algorithm.IISResistorNewCounter

    elif (str == 'IISSmallChipCounter'):
        ret == Algorithm.IISSmallChipCounter

    #not legacy algorithms
    elif (str == 'OCGenericCounter'):
        ret = Algorithm.OCGenericCounter

    elif (str == 'OCSmallChipCounter'):
        ret = Algorithm.OCSmallChipCounter

    elif (str == 'OCTrayStickCounter'):
        ret = Algorithm.OCTrayStickCounter

    elif (str == 'OCSnippetCounter'):
        ret = Algorithm.OCSnippetCounter

    elif (str == 'OCNetworkCounter'):
        ret = Algorithm.OCNetworkCounter

    elif (str == 'OCFargmentedPartsCounter'):
        ret = Algorithm.OCfragmentedPartsCounter

    else:
        ret = Algorithm.NotDefined
        print("no algorithm set: " + str)

    return ret
