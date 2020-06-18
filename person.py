class Person(object):
    def __init__(self):
        self.name = input("What is your first name?\n")
        self.gender = input("What is your gender\n")
        self.age = int(input("What is your age?\n"))
        self.weightType = input("Do you want to be weighed in KG or LB?\n")
        self.weight = input("What is your current weight in %s?\n" % self.weightType)
