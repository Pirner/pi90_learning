class AlgorithmDefinitionOption(object):
    """store different options for the algorithm"""
    _None = False
    _UseContrastEnhancement = False
    _UseThresholdAdjust = False
    _UseSizeHints = False
    _UseClosing = False
    _UseMerging = False
    _UseMultiThreshold = False
    _AllowMultiCounts = False
    _Option9 = False
    _Option10 = False
    _Option11 = False
    _Option12 = False
    _Option13 = False
    _Option14 = False
    _Option15 = False

    def __init__(self):
        _None = False
        _UseContrastEnhancement = False
        _UseThresholdAdjust = False
        _UseSizeHints = False
        _UseSizeHints = False
        _UseClosing = False
        _UseMerging = False
        _UseMultiThreshold = False
        _AllowMultiCounts = False
        _Option9 = False
        _Option10 = False
        _Option11 = False
        _Option12 = False
        _Option13 = False
        _Option14 = False
        _Option15 = False

    def getOptions(self):
        ret = []

        
        if (self._None):
            return []

        elif (self._UseContrastEnhancement):
            ret.append('UseContrastEnhancement')

        elif (self._UseThresholdAdjust):
            ret.append('UseThresholdAdjust')

        elif (self._UseSizeHints):
            ret.append('UseSizeHints')

        elif (self._UseClosing):
            ret.append('UseClosing')

        elif (self._UseMerging):
            ret.append('UseMerging')

        elif (self._UseMultiThreshold):
            ret.append('UseMultiThreshold')

        elif (self._AllowMultiCounts):
            ret.append('AllowMultiCounts')
        
        elif (self._Option9):
            ret.append('Option9')

        elif (self._Option10):
            ret.append('Option10')

        elif (self._Option11):
            ret.append('Option11')

        elif (self._Option12):
            ret.append('Option12')

        elif (self._Option13):
            ret.append('Option13')

        elif (self._Option14):
            ret.append('Option14')

        elif (self._Option15):
            ret.append('Option15')

        else:
            return []

    def getOptionsAsString(self):
        ret = ''

        if (self._None):
            return ''

        elif (self._UseContrastEnhancement):
            ret = ret + ' UseContrastEnhancement'

        elif (self._UseThresholdAdjust):
            ret = ret + ' UseThresholdAdjust'

        elif (self._UseSizeHints):
            ret = ret + ' UseSizeHints'

        elif (self._UseClosing):
            ret = ret + ' UseClosing'

        elif (self._UseMerging):
            ret = ret + ' UseMerging'

        elif (self._UseMultiThreshold):
            ret = ret + ' UseMultiThreshold'

        elif (self._AllowMultiCounts):
            ret = ret + ' AllowMultiCounts'
        
        elif (self._Option9):
            ret = ret + ' Option9'

        elif (self._Option10):
            ret = ret + ' Option10'

        elif (self._Option11):
            ret = ret + ' Option11'

        elif (self._Option12):
            ret = ret + ' Option12'

        elif (self._Option13):
            ret = ret + ' Option13'

        elif (self._Option14):
            ret = ret + ' Option14'

        elif (self._Option15):
            ret = ret + ' Option15'

        else:
            return ''
