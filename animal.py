class Animal(object):
    def __init__(self, weight=0):
        self.animalType = input("What is your animal's type?\n")
        self.name = input("What is your animal's name?\n")
        self.age = input("What is %s\'s age?\n" % self.name)
        self.weight = weight




