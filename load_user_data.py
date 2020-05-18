# 载入用户数据

from coordinates_generator import random_coordinates_generator 


def load_user_data():
    """
    载入用户数据
    """
    coordinates = random_coordinates_generator(100)
    # coordinates.append([104.3,30.6])
    # coordinates.append([104.25,30.7])
    # coordinates.append([104.24,30.625])
    # coordinates.append([104.33,30.69])
    users = []
    for e,i in enumerate(coordinates):
        user = {
            "id" : e,
            "coordinate" : i
        }
        users.append(user)
    return users
