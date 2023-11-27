from CarType import CarType


class Car:
    def __init__(self, brand: str, model: str, car_type: CarType, fuel_capacity: int, milege: int):
        self.brand = brand
        self.model = model
        self.car_type = car_type
        self.fuel_capacity = fuel_capacity
        self.milege = milege

        self.additional_features = []

    def get_range(self):
        return self.fuel_capacity / self.milege

