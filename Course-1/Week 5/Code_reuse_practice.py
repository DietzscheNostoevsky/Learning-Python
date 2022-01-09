# %%


class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

# %%


class Turtle(Animal):

    Animal.category = "Reptile"


print(Turtle.category)

# %%


class Snake(Animal):

    Snake.category = "heehaa"

# %%


print(Snake.category)
print(Animal.category)
print(Turtle.category)


# %%
