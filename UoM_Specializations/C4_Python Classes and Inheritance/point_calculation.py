# Learning about classes

# %%
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

    def distance(self, point2):
        xdiff = point2.x - self.x
        ydiff = point2.y - self.y

        dis = (xdiff ** 2 + ydiff ** 2) ** 0.5
        return dis

    def __str__(self) -> str:
        retstr = f"x = {self.x} , y = {self.y}"
        return retstr

    # Suppose you have a point object and wish to find
    # the midpoint halfway between it and some other target point.
    # We would like to write a method, let’s call it halfway,
    # which takes another Point as a parameter and
    # returns the Point that is halfway between the
    # point and the target point it accepts as input.

    def halfway(self, targetpoint):
        xd = (self.x + targetpoint.x)/2
        yd = (self.y + targetpoint.y)/2
        retpt = Point(xd, yd)
        return retpt


# %%
