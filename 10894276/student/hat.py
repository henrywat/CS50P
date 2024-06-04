import random


class Hat:
    #def __init__(self):
    #    self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

    #def sort(self, name):
    #    print(name, "is in", random.choice(self.houses))


#hat = Hat()
#hat.sort("Harry")
Hat.sort("Harry")
