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


# %%
