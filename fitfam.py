from app import app
from animal import Animal
from person import Person

def obtainAnimalWeight(personWeight, personWithAnimalWeight):
    return personWithAnimalWeight - personWeight

personName = input("Input your first name: ")
personGender = input("Input your gender: ")
personAge = input("Input your age: ")
personWeight = int(input("Input your weight: "))
personWithAnimalWeight = int(input("Input your weight plus your animals weight: "))

newPerson = Person(personName, personGender, personAge, personWeight)

animalType = input("Input your animal's type: ")
animalName = input("Input your %s name: " % animalType)
animalAge = input("Input your %s age: " % animalType)
animalWeight = obtainAnimalWeight(newPerson.weight, personWithAnimalWeight)

newAnimal = Animal(animalType, animalName, animalAge, animalWeight)

#def addAnimalToPerson(personName,)


personWithAnimals = {"personName": newPerson.name,
                     "personGender": newPerson.gender,
                     "personAge": newPerson.age,
                     "personWeight": newPerson.weight,
                     "animals": [{animalType: newAnimal.animalType,
                                animalName: newAnimal.name,
                                animalAge: newAnimal.age,
                                animalWeight: newAnimal.weight
                               }]
                     }

print(personWithAnimals.items())

print(personWithAnimals.values())