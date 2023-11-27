from car import Car
from CarType import CarType
from typing import List

"""

In the Showroom class, implement the following methods,

1. populate_cars: this method should read the car list given the file "car_list.json" and create respective Car objects
 for each car in the given car list and add it to the Showroom cars list.

2. dump_car_list: this method should convert the cars list in the Showroom and store it in the file car_list.json
 in JSON format
 
3. filter_sports_cars: this method will return a list of all Sports Cars from the Showroom cars list

4. filter_long_range_cars: this method should return a list of cars with range >= 300

5. filter_cars_by_type: this method should return all the cars that has the given CarType as its car type property
 
"""


class Showroom:
    def __init__(self):
        self.cars = []

        self.car_list = "car_list.json"

    def populate_cars(self):
        # write your code here
        return

    def dump_car_list(self):
        # write your code here
        return

    def filter_sports_cars(self) -> List[Car]:
        # write your code here
        return []

    def filter_long_range_cars(self) -> List[Car]:
        # write your code here. Long range cars are cars with range >= 300
        return []

    def filter_cars_by_type(self, car_type: CarType) -> List[Car]:
        # write your code here
        return []






