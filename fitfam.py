from animal import Animal
from person import Person
from user import User
from datetime import datetime
import psycopg2

def getCurrentUser(username):
    username = username
    return username

def obtainAnimalWeight(personWeight, personWithAnimalWeight):
   return personWithAnimalWeight - personWeight




if __name__ == '__main__':
    #If the user current user has a record prompt if they want to add or view weights.

    username = input('Please input your username:\n')

    # personWithAnimals = {"addedDate": datetime.today(),
    #                     "personName": newPerson.name,
    #                      "personGender": newPerson.gender,
    #                      "personAge": newPerson.age,
    #                      "personWeight": newPerson.weight,
    #                      "animals": [{animalType: newAnimal.animalType,
    #                                 animalName: newAnimal.name,
    #                                 animalAge: newAnimal.age,
    #                                 animalWeight: newAnimal.weight
    #                                }]
    #                      }



    # Setting up connection of database.

    connection = psycopg2.connect(
                                  host='localhost',
                                  database='FitPets',
                                  user='postgres',
                                  password='admin')

    connection.set_session(autocommit=True)

    # Checks to see if username provided exists in database.

    with connection.cursor() as cursor:
        cursor.execute ("SELECT  u.username\n"
                        "FROM    users u\n"
                        "WHERE   u.username = '{0}'".format(username))
        rows = cursor.rowcount

    # If the username does not exist, asks user if they want to create.

    if rows == 0:
        print('Username does not exist in the database.\n')
        response = ''

        while response != 'Y' or 'N':

            response = input('Would you like to create a user?\n'
                             'Type Y or N and press enter.\n')

    # If user wants to create a user, call User Class to create.

            if response == 'Y':
                user = User()

                record_tuple = (user.username
                                ,user.password
                                ,user.email
                                ,user.created_on
                                ,user.last_login)

    #   Insert provided results into open connection.

                with connection.cursor() as cursor:
                    cursor.execute (""" INSERT INTO users(username
                                                          ,password
                                                          ,email
                                                          ,created_on
                                                          ,last_login)

                                        VALUES (%s -- username
                                                ,%s -- password
                                                ,%s-- email
                                                ,%s -- created_on
                                                ,%s -- last_login
                                               )
                                    """, record_tuple)
                break

            elif response == 'N':
                print('Okay thanks anyways.\n')
                exit()

            else:
                print('Please key in either Y or N.\n')
    else:
        print('Username already exists!')



    menu_selection = int(input('Hi {0}! What would you like to do?\n'
                          '1. Add a new person.\n'
                          '2. Add a new animal. \n'
                          '3. Log weights. \n'
                          '4. View weights. \n'
                          .format(username)))

    def menu_switcher(argument):
        switcher = {1: Person(),
                    2: 'Animal',
                    3: 'Log weights',
                    4: 'View eights'
                    }
        print(switcher.get(argument, 'Invalid number'))

    menu_switcher(menu_selection)


    # animal = Animal(newPerson.weight)





    # with connection.cursor() as cursor:
    #     cursor.execute("""SELECT *
    #                       FROM users u
    #                       WHERE u.username = %(username)s
    #                    """, {
    #                             'username': current_user
    #                    })
    #     result = cursor.fetchone()
    #     print(result)


    cursor.close()
    connection.close()

