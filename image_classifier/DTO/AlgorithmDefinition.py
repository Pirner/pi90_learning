from DTO.Algorithm import Algorithm
from DTO.AlgorithmDefinitionOption import AlgorithmDefinitionOption

class AlgorithmDefinition(object):
    """description of class"""
    isNew = False
    ConvertedFromOldVersion = False
    WidthHint = 0.0
    HeightHint = 0.0
    SizeHint = 0.0
    LayerThickness = 0.0
    PitchHint = 0
    RecursionDepthHint = 0
    RecursionDepth = 0
    MeasurementProbability = 0.0
    Algorithm = Algorithm.NotDefined
    OverrideAlgorithm = None
    ExpertSettings = None
    AlgoOptions = AlgorithmDefinitionOption()

    def __init__(self):

        self.isNew = False
        self.ConvertedFromOldVersion = False
        self.WidthHint = 0.0
        self.HeightHint = 0.0
        self.SizeHint = 0.0
        self.LayerThickness = 0.0
        self.PitchHint = 0
        self.RecursionDepth = 0
        self.MeasurementProbability = 0.0
        self.Algorithm = Algorithm.NotDefined
        self.OverrideAlgorithm = None
        self.ExpertSettings = None
        self.AlgoOptions = AlgorithmDefinitionOption()