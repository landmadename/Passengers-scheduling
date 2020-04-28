from random_coordinates_generator import random_coordinates_generator 
import random


def load_driver_data():
    coordinates = random_coordinates_generator(25)
    drivers = []
    for e,i in enumerate(coordinates):
        driver = {
            "id" : e,
            "coordinate" : i,
            "order" : e,
            "sites" : random.choice([4,6])
        }
        drivers.append(driver)
    return drivers
