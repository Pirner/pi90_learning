class Point(object):
    """description of class"""
    x = 0
    y = 0

    def __init__(self, x, y):
        if (x >= 0 and y >= 0):
            self.x = x
            self.y = y
        else:
            self.x = 0
            self.y = 0
