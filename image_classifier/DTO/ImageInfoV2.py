import PIL.Image
import numpy as np

class ImageInfoV2:

    # attributes
    path = None
    NFalsePositiveStructureComponents = 0
    NFalsePositiveHeightWidthComponents = 0
    # 3 is undefined package
    PredictedPackageType = 3

    AlgorithmDefinition = None
    MeasuredWidth = 0
    MeasuredHeight = 0
    MeasuredSize = 0
    Pitch = 0
    LayerThickness = 0
    CenterX = 0
    CenterY = 0
    # not implemented
    Status = None
    PlausiDecision = False
    # not implemented
    ImageStatus = None

    Count = 0
    TargetCount = 0
    Accuracy = 0
    PlausiCountCorrection = 0
    ProcessSwitch = False
    ExecTime = None
    Seconds = 0
    CenterHintX = 0
    CenterHintY = 0
    ReelName = None
    ArticleName = None
    ReelInnerRadius = None
    MeasurementProbability = 0
    PackageType = None
    ImageNPArray = []
    # attributes which are not from the ImageInfoV2
    MachinePrecision = 0.00001
    IsProcessed = False

    def __init__(self):
        pass

    def readImage(self, path):
        """This function reads the image from a path into a numpy array."""
        image = PIL.Image.open(path)   
        pixel = np.array(image)
        print(pixel.shape[0], pixel.shape[1])
        pixel = pixel.reshape(1, pixel.shape[0] * pixel.shape[1])
        # now reshape it for one line
        #image = np.fromfile(path, )
        self.ImageNPArray = pixel

    def toString(self):
        ret = ''
        if self.NFalsePositiveStructureComponents is None:
            ret = ret + 'NFalsePositiveStructureComponents: ' + 'None' + '\n'
        else:
            ret = ret + 'NFalsePositiveStructureComponents: ' + str(self.NFalsePositiveStructureComponents) + '\n'
        
        if self.NFalsePositiveHeightWidthComponents is None:
            ret = ret + 'NFalsePositiveHeightWidthComponents: ' + 'None' + '\n'
        else:
            ret = ret + 'NFalsePositiveHeightWidthComponents: ' + str(self.NFalsePositiveHeightWidthComponents) + '\n'

        if self.PredictedPackageType is None:
            ret = ret + 'PredictedPackageType: ' + 'None' + '\n'
        else:
            ret = ret + 'PredictedPackageType: ' + str(self.PredictedPackageType) + '\n'

        if self.AlgorithmDefinition is None:
            ret = ret + 'AlgorithmDefinition: ' + 'None' + '\n'
        else:
            ret = ret + 'AlgorithmDefinition: ' + self.AlgorithmDefinition + '\n'

        if self.MeasuredWidth is None:
            ret = ret + 'MeasuredWidth: ' + 'None' + '\n'
        else:
            ret = ret + 'MeasuredWidth: ' + str(self.MeasuredWidth) + '\n'
        
        if self.MeasuredHeight is None:
            ret = ret + 'MeasuredHeight: ' + 'None' + '\n'
        else:
            ret = ret + 'MeasuredHeight: ' + str(self.MeasuredHeight) + '\n'

        if self.MeasuredSize is None:
            ret = ret + 'MeasuredSize: ' + 'None' + '\n'
        else:
            ret = ret + 'MeasuredSize: ' + str(self.MeasuredSize) + '\n'

        if self.Pitch is None:
            ret = ret + 'Pitch: ' + 'None' + '\n'
        else:
            ret = ret + 'Pitch: ' + str(self.Pitch) + '\n'
        
        if self.LayerThickness is None:
            ret = ret + 'LayerThickness: ' + 'None' + '\n'
        else:
            ret = ret + 'LayerThickness: ' + str(self.LayerThickness) + '\n'
        
        if self.CenterX is None:
            ret = ret + 'CenterX: ' + 'None' + '\n'
        else:
            ret = ret + 'CenterX: ' + str(self.CenterX) + '\n'

        if self.CenterY is None:
            ret = ret + 'CenterY: ' + str(self.CenterY) + '\n'
        else:
            ret = ret + 'CenterY: ' + str(self.CenterY) + '\n'

        if self.Status is None:
            ret = ret + 'Status: ' + 'None' + '\n'
        else:
            ret = ret + 'Status: ' + self.Status + '\n'

        if self.PlausiDecision is None:
            ret = ret + 'PlausiDecision: ' + 'None' + '\n'
        else:
            ret = ret + 'PlausiDecision: ' + str(self.PlausiDecision) + '\n'


        return ret
