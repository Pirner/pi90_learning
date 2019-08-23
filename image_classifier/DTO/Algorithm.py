from enum import IntEnum

class Algorithm(IntEnum):
    """description of class"""
    NotDefined = 0

    IISResistorCounter = 1
    IISCapacityCounter = 2
    IISMelfCounter = 3
    IISElkoCounter = 4
    IISIcCounter = 5
    IISSotCounter = 6
    IISOptoCounter = 7
    IISElkoLargeCounter = 8
    IISIcModCounter = 9
    IISResistorNewCounter = 10
    IISSmallChipCounter = 11
    OCGenericCounter = 100
    OCSmallChipCounter = 101
    OCTrayStickCounter = 102
    OCSnippetCounter = 103
    OCNetworkCounter = 104
    OCfragmentedPartsCounter = 105
