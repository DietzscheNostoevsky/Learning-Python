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

    Animal.category = 'reptile'

# %%


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo1 = Zoo()


# %%

turtle1 = Turtle("Kachua")
snake1 = Snake("Saamp")

zoo1.add_animal(turtle1)
zoo1.add_animal(snake1)


print(zoo1.total_of_category("reptile"))

# %%
