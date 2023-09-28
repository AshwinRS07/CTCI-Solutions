# Parking Lot: Design a parking lot using object-oriented principles

# Objects: Vehicle, Motorcycle, Car, Bus, Parking Spot

from enum import Enum

class VehicleType(Enum):
    Motorcycle, Car, Bus = 0, 1, 2

class Vehicle:
    def __init__(self):
        self.parking_spots = []
        self.license_plate = ''
        self.vehicle_type = None
        self.vehicle_size = 0

    def get_spots_needed(self):
        return self.vehicle_size
    
    def park_in_spot(self, parking_spot):
        parking_spot.add(self.license_plate)

    def vacate_spot(self):
        pass

    def check_fit(parking_spot):
        pass

class Motorcycle(Vehicle):
    def __init__(self):
        self.vehicle_size = 1
        self.vehicle_type = VehicleType.Motorcycle
    def check_fit(parking_spot):
        return super().check_fit()

class Car(Vehicle):
    def __init__(self):
        self.vehicle_size = 1
        self.vehicle_type = VehicleType.Car
    def check_fit(parking_spot):
        return super().check_fit()

class Motorcycle(Vehicle):
    def __init__(self):
        self.vehicle_size = 10
        self.vehicle_type = VehicleType.Bus
    def check_fit(parking_spot):
        return super().check_fit()
    

class ParkingLot:
    def __init__(self):
        self.level = None
        self.num_levels = 3
        pass

# has floor, parking_spots array, free spot number, spots per row
class Level:
    def __init__(self, floor, num_spots, free_spots, spots_per_row):
        pass

    def get_available_spots(self):
        pass

    def park_vehicle(self, vehicle: Vehicle):
        pass

    def park_at_spot(self, vehicle, spot):
        pass

    def find_spot(self, vehicle):
        pass
    def free_spot(self, spot):
        pass


class ParkingSpot:
    def __init__(self, lvl: Level, row, spot_num, vehicle_size):
        self.vehicle = None
        pass

    def is_available(self):
        return self.vehicle == None
    
    def can_fit_vehicle(self, vehicle:Vehicle):
        pass

    def park(self, vehicle):
        pass

    def get_row(self):
        pass

    def get_spot_num(self):
        pass

    def remove_vehicle(self):
        pass
