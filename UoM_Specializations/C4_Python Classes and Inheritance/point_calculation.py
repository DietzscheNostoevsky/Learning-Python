# Learning about classes


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distancefromorigin(self):
        return (self.x ** 2 + self.y ** 2) ** (0.5)

    def distance(point1, point2):
        xdiff = point2.x - point1.x
        ydiff = point2.y - point1.y

        dis = (xdiff ** 2 + ydiff ** 2) ** 0.5
        return dis
