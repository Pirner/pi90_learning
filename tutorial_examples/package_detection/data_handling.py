import os
import struct
import numpy as np

from tutorial_examples.package_detection.ImageInfoV2 import  ImageInfoV2

# This module is responsible for the data in and output
# it acts as an interface to continue from a given state or write a state down
# import xml.etree.cElementTree as ET
from lxml import etree
from Learning import StackAdalineOptimizer
from DTO.ImageInfoV2 import ImageInfoV2
from DTO.AlgorithmDefinition import AlgorithmDefinition
from DTO.Algorithm import Algorithm
from array import array
from pathlib import Path
from Settings import basePath
import utils
import os


class StateInterface:

    def __init__(self):
        pass

    # this method write the current state down to continue the learning process
    #def writeState(self, filename, optimizer: StackAdalineOptimizer):
        #pass

    #def readState(self, filename, optimizer: StackAdalineOptimizer):
        #pass

    def readXMLImageList(self, filename):
        # root = ET.parse(filename.decode("utf-8").encode("utf-16")).getroot()
        # root = ET.parse(etree.tostring(filename).decode("utf-8").encode("utf-16")).getroot()
        parser = etree.XMLParser(encoding='UTF-8')
        root = etree.parse(filename, parser=parser).getroot()

        # print(root)

        imageInfos = []

        for child in root:
            # put every attribute to the construct together
            imageInfos.append(self.etreeToImageInfoV2(child))

        return imageInfos

    def replaceBaseInImagePath(self, imagePath):
        # split the path along side the \
        # tmp = Path(imagePath)
        # path, folder = os.path.split(tmp)

        # print("path: " + path)
        # print("folder: " + folder)
        split = imagePath.split('\\')

        # remove the base entry at the beginning
        split.pop(0)

        filename = basePath
        for path in split:
            filename = os.path.join(filename, path)

        ret = filename
        return ret

    def childToAlgorithmDefinition(self, tree):
        aod = AlgorithmDefinition()
        for child in tree:
            if (child.tag == 'Options'):
                if (child.text is not None):
                    aod.AlgoOptions = utils.strOptionsToAlgorithmDefinitionOptions(child.text)

            elif (child.tag == 'IsNew'):
                if (child.text is not None):
                    if (child.text == 'true'):
                        aod.isNew = True
                    else:
                        aod.IsNew = False
                else:
                    aod.IsNew = False

            elif (child.tag == 'ConvertedFromOldVersion'):
                if (child.text is not None):
                    if (child.text == 'true'):
                        aod.ConvertedFromOldVersion = True
                    else:
                        aod.IsNew = False
                else:
                    aod.ConvertedFromOldVersion = False

            elif (child.tag == 'WidthHint'):
                if (child.text is not None):
                    aod.WidthHint = (float)(child.text)
                else:
                    aod.WidthHint = 0.0

            elif (child.tag == 'HeightHint'):
                if (child.text is not None):
                    aod.HeightHint = (float)(child.text)
                else:
                    aod.HeightHint = 0.0

            elif (child.tag == 'SizeHint'):
                if (child.text is not None):
                    aod.SizeHint = (float)(child.text)
                else:
                    aod.SizeHint = 0.0

            elif (child.tag == 'LayerThicknessHint'):
                if (child.text is not None):
                    aod.LayerThicknessHint = (float)(child.text)
                else:
                    aod.LayerThickness = 0.0

            elif (child.tag == 'RecursionDepthHint'):
                if (child.text is not None):
                    aod.RecursionDepthHint = (int)(child.text)
                    aod.RecursionDepth = (int)(child.text)
                else:
                    aod.RecursionDepth = 0
                    aod.RecursionDepthHint = 0

            elif (child.tag == 'MeasurementProbability'):
                if (child.text is not None):
                    aod.MeasurementProbability = (float)(child.text)
                else:
                    aod.MeasurementProbability = 0.0

            elif (child.tag == 'Algorithm'):
                # decode child text:
                aod.Algorithm = utils.StringToAlgorithm(child.text)

            elif (child.tag == 'Override Algorithm'):
                print(child.tag + " not implemented")
            elif (child.tag == 'ExpertSettings'):
                print(child.tag + " not implemented")
            else:
                print(child.tag + " not caught up yet!")

        return aod

    def etreeToImageInfoV2(self, tree):
        forgotten_fields = []
        info = ImageInfoV2()
        for element in tree:
            if (element.tag == 'ImagePath'):
                if element.text is not None:
                    info.path = self.replaceBaseInImagePath(element.text)

            elif (element.tag == 'NFalsePositiveStructureComponents'):
                if element.text is not None:
                    info.NFalsePositiveStructureComponents = int(element.text)

            elif (element.tag == 'NFalsePositiveHeightWidthComponents'):
                if element.text is not None:
                    info.NFalsePositiveHeightWidthComponents = int(element.text)

            elif (element.tag == 'PredictedPackageType'):
                if element.text is not None:
                    info.PredictedPackageType = element.text

            # elif (element.tag == 'AlgorithmDefinition'):
            # info.AlgorithmDefinition = element.text

            elif (element.tag == 'MeasuredWidth'):
                if element.text is not None:
                    info.MeasuredWidth = float(element.text)

            elif (element.tag == 'MeasuredHeight'):
                if element.text is not None:
                    info.MeasuredHeight = float(element.text)

            elif (element.tag == 'MeasuredSize'):
                if element.text is not None:
                    info.MeasuredSize = float(element.text)

            elif (element.tag == 'Pitch'):
                if element.text is not None:
                    info.Pitch = float(element.text)

            elif (element.tag == 'LayerThickness'):
                if element.text is not None:
                    info.LayerThickness = float(element.text)

            elif (element.tag == 'CenterX'):
                if element.text is not None:
                    info.CenterX = int(element.text)
            elif (element.tag == 'CenterY'):
                if element.text is not None:
                    info.CenterY = int(element.text)

            # elif (element.tag == 'Status'):
            # info.Status = element.text

            elif (element.tag == 'PlausiDecision'):
                if element.text is not None:
                    info.PlausiDecision = element.text
            # elif (element.tag == 'ImageStatus'):
            # info.ImageStatus = element.text

            elif (element.tag == 'Count'):
                if element.text is not None:
                    info.Count = int(element.text)

            elif (element.tag == 'TargetCount'):
                if element.text is not None:
                    info.TargetCount = int(element.text)

            elif (element.tag == 'Accuracy'):
                if element.text is not None:
                    info.Accuracy = float(element.text)

            elif (element.tag == 'PlausiCountCorrection'):
                if element.text is not None:
                    info.PlausiCountCorrection = int(element.text)

            elif (element.tag == 'ProcessSwitch'):
                if element.text is not None:
                    info.ProcessSwitch = bool(element.text)

            elif (element.tag == 'ExecTime'):
                if element.text is not None:
                    info.ExecTime = element.text

            elif (element.tag == 'Seconds'):
                if element.text is not None:
                    info.Seconds = float(element.text)

            elif (element.tag == 'CenterHintX'):
                if element.text is not None:
                    info.CenterHintX = int(element.text)

            elif (element.tag == 'CenterHintY'):
                if element.text is not None:
                    info.CenterHintY = int(element.text)

            elif (element.tag == 'ReelName'):
                if element.text is not None:
                    info.ReelName = element.text

            elif (element.tag == 'ArticleName'):
                if element.text is not None:
                    info.ArticleName = element.text

            elif (element.tag == 'ReelInnerRadius'):
                if element.text is not None:
                    info.ReelInnerRadius = float(element.text)

            elif (element.tag == 'MeasurementProbability'):
                if element.text is not None:
                    info.MeasurementProbability = float(element.text)

            elif (element.tag == 'PackageType'):
                if element.text is not None:
                    info.PackageType = element.text
            elif (element.tag == 'AlgorithmDefinition'):
                aod = self.childToAlgorithmDefinition(element)
                info.AlgorithmDefinition = aod

            else:
                if element.text is not None:
                    forgotten_fields.append((element.tag, element.text))

        return info


def load_mnist(path, kind='train'):
    """MNIST-Daten von path laden"""
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte' % kind)

    images_path = os.path.join(path, '%s-images-idx3-ubyte' % kind)

    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II', lbpath.read(8))

        labels = np.fromfile(lbpath, dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))

        images = np.fromfile(imgpath, dtype=np.uint8).reshape(len(labels), 784)

    return images, labels

def get_image_infos_from_xml(path):
    image_infos = []

    return image_infos