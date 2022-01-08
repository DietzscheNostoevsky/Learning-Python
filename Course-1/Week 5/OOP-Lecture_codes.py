class Apple:
    def __init__(self, color='red', flavor='sweet'):
        self.color = color
        self.flavour = flavor

        # str method so that when this code :
        # print(himachal) gets executed, it dooesnt returns the memory loc
        # when print fn is called with an instance of our class ie himachal

    def __str__(self):
        return f'This apple is {self.color} and its flavor is {self.flavour}.'


#kashmiri = Apple()
# print(kashmiri.color)
# print(kashmiri.flavour)
himachal = Apple("yellow", 'bitter')

print(himachal.color)
print(himachal)

# docstring
