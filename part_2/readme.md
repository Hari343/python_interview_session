# Zig-Wheels

Zig-Wheels is a car showroom and they are planning to implement a Python-based system to store 
their car collection in order to provide their customers a digital interactive experience.

In this project you will be working on a part of their system that reads the list of cars
from a file to the application. 

## Tasks

To complete this part you have to do three tasks

## Task 1

In sports_car.py:

Create a SportsCar class by subclassing Car.Anda add the following properties:
    1. max_acceleration: float
    2. max_speed: int

## Task 2

In showroom.py:

Implement the following methods:

1. populate_cars: this method should read the car list given the file "car_list.json" and create respective Car objects
 for each car in the given car list and add it to the Showroom cars list.

2. dump_car_list: this method should convert the cars list in the Showroom and store it in the file car_list.json
 in JSON format
 
3. filter_sports_cars: this method will return a list of all Sports Cars from the Showroom cars list

4. filter_long_range_cars: this method should return a list of cars with range >= 300

5. filter_cars_by_type: this method should return all the cars that has the given CarType as its car type property

 
## Task 3

In main.py:

1. Instantiate the Showroom class and call the populate_cars method .

2. Add the following car to the cars list of the showroom instance:

    {
        brand: "Bentley"
        model: "Continental GT"
        car_type: CarType.COUPE
        fuel_capacity: 30
        milege: 20
    }

3. Remove all the cars of type, CarType.HATCHBACK from the showroom cars list.

4. Call the dump_car_list method and write out the current cars list to the file.

5. Implement a function to read the car_names.txt which contains the names of required cars
 (eg: Bentley Continental GT) and return a list of boolean values stating whether the car
  is in the showroom or not. Your search algorithm should be implemented in a scalable and efficient manner. 



That is all. You have completed Part 2 
