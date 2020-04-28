from random_coordinates_generator import random_coordinates_generator 


def load_user_data():
    coordinates = random_coordinates_generator(100)
    users = []
    for e,i in enumerate(coordinates):
        user = {
            "id" : e,
            "coordinate" : i
        }
        users.append(user)
    return users
