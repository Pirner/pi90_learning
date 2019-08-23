import csv

from DTO.Point import Point
from DTO.IPStatus import IPStatus

class IPResults(object):
    """description of class"""
    Status = IPStatus.NotDefined
    ReelCenter = Point(0, 0)
    ReelCenterRefined = Point(0, 0)
    PartSizes = []
    HasMultiCounts = False
    ComponentCount = 0

    MinReelRadius = 0.0
    MinReelRadiusConfidence = 0.0
    MaxReelRadius = 0.0
    MaxReelRadiusConfidence = 0.0

    ResultImageIsOverlay = False

    AutoComponentWidth = 0.0
    AutoComponentHeight = 0.0
    AutoComponentDepth = 0.0

    AutoOuterRadius = 0.0
    AutoInnerRadius = 0.0

    Insecurity = 0.0
    AppliedThreshold = 0.0

    ReelDiameter = 0
    ReelHubDiameter = 0

    IPModuleID = ''

    SmallPartsCorrection = 0

    def __init__(self):
        self.Status = IPStatus.NotDefined
        self.ReelCenter = Point(0, 0)
        self.ReelCenterRefined = Point(0, 0)

        self.PartSizes = []

        self.HasMultiCounts = False
        self.ComponentCount = 0

        self.MinReelRadius = 0.0
        self.MinReelRadiusConfidence = 0.0
        self.MaxReelRadius = 0.0
        self.MaxReelRadiusConfidence = 0.0
        self.ResultImageIsOverlay = False

        self.AutoComponentWidth = 0.0
        self.AutoComponentHeight = 0.0
        self.AutoComponentDepth = 0.0

        self.AutoOuterRadius = 0.0
        self.AutoInnerRadius = 0.0

        self.Insecurity = 0.0
        self.AppliedThreshold = 0.0

        self.ReelDiameter = 0
        self.ReelHubDiameter = 0

        self.IPModuleID = ''

        self.SmallPartsCorrection = 0

    def CreateCSV(self, path):
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

    def AppendToCSV(self, path):
        line = []
        line.append(self.Status.toString())
        line.append(str(self.ReelCenter.x))
        line.append(str(self.ReelCenter.y))
        line.append(str(self.ReelCenterRefined.x))
        line.append(str(self.ReelCenterRefined.y))

        #think about a workaround
        #for ps in self.PartSizes:
        #    line.append(str(ps))

        line.append(str(self.HasMultiCounts))
        line.append(str(self.ComponentCount))
        line.append(str(self.MinReelRadius))
        line.append(str(self.MinReelRadiusConfidence))
        line.append(str(self.MaxReelRadius))
        line.append(str(self.MaxReelRadiusConfidence))
        line.append(str(self.ResultImageIsOverlay))
        line.append(str(self.AutoComponentWidth))
        line.append(str(self.AutoComponentHeight))
        line.append(str(self.AutoComponentDepth))
        line.append(str(self.AutoOuterRadius))
        line.append(str(self.AutoInnerRadius))
        line.append(str(self.Insecurity))
        line.append(str(self.AppliedThreshold))
        line.append(str(self.ReelDiameter))
        line.append(str(self.ReelHubDiameter))
        line.append(self.IPModuleID)
        line.append(str(self.SmallPartsCorrection))



        with open(path, mode='a') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result_writer.writerow(line)