class Vehicle:
  def __init__(self, spot_size: int):
    self._spot_size = spot_size

  def get_spot_size(self) -> int:
    return self._spot_size
  

class Driver:
  def __init__(self, id: int, vehicle: Vehicle):
    self._id = id
    self._vehicle = vehicle
    self._payment_due = 0


  def get_vehicle(self) -> Vehicle:
    return self._vehicle
  
  def get_id(self) -> int:
    return self._id
  
  def charge(self, amount: int):
    self._payment_due += amount

class Car(Vehicle):
  def __init__(self):
    super().__init__(1)

class Limo(Vehicle):
  def __init__(self):
    super().__init__(2)

class SemiTruck(Vehicle):
  def __init__(self):
    super().__init__(3)

class ParkingFloor:
  def __init__(self, spot_count: int):
    self._spots = [0] * spot_count
    self._vehicle_map = {}

  def park_vehicle(self, vehicle: Vehicle):
    size = vehicle.get_spot_size()
    l, r = 0, 0
    while r < len(self._spots):
      if self._spots[r] != 0:
        l = r + 1
      if r - l + 1 == size:
        # we found a spot
        for k in range(l, r + 1):
          self._spots[k] = 1
        self._vehicle_map[vehicle] = [l, r]
        return True
      r += 1

    return False

  def remove_vehicle(self, vehicle: Vehicle):
    start, end = self._vehicle_map[vehicle]
    for i in range(start, end + 1):
      self._spots[i] = 0
    del self._vehicle_map[vehicle]

  def get_parking_spots(self):
    return self._spots 
  
  def get_vehicle_spots(self, vehicle: Vehicle):
    return self._vehicle_map.get(vehicle, None)
  
class ParkingGarage:
  def __init__(self, floor_count: int, spots_per_floor: int):
    self._parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

  def park_vehicle(self, vehicle: Vehicle):
    for floor in self._parking_floors:
      if floor.park_vehicle(vehicle):
        return True
      
    return False
  
  def remove_vehicle(self, vehicle: Vehicle):
    for floor in self._parking_floors:
      if floor.get_vehicle_spots(vehicle):
        floor.remove_vehicle(vehicle)
        return True
      
    return False
  

import datetime
import math

class ParkingSystem:
  def __init__(self, parking_garage: ParkingGarage, hourlyRate: int):
    self._parkingGarage = parking_garage
    self._hourlyRate = hourlyRate
    self._timeParked = {} # map driverId to time that they parked

  def park_vehicle(self, driver: Driver):
    currentHour = datetime.datetime.now().hour
    isParked = self._parkingGarage.park_vehicle(driver.get_vehicle())
    if isParked:
      self._timeParked[driver.get_id()] = currentHour

    return isParked
  
  def remove_vehicle(self, driver: Driver):
    if driver.get_id() not in self._timeParked:
      return False
    
    currentHour = datetime.datetime.now().hour
    timeParked = math.ceil((currentHour - self._timeParked[driver.get_id()]))
    driver.charge(timeParked * self._hourlyRate)

    del self._timeParked[driver.get_id()]
    return self._parkingGarage.remove_vehicle(driver.get_vehicle())
  
if __name__ == '__main__':
  parkingGarage = ParkingGarage(3, 2)
  parkingSystem = ParkingSystem(parkingGarage, 5)

  driver1 = Driver(1, Car())
  driver2 = Driver(2, Limo())
  driver3 = Driver(3, SemiTruck())

  print(parkingSystem.park_vehicle(driver1)) # True
  print(parkingSystem.park_vehicle(driver2)) # True
  print(parkingSystem.park_vehicle(driver3)) # False

  print(parkingSystem.remove_vehicle(driver1)) # True
  print(parkingSystem.remove_vehicle(driver2)) # True
  print(parkingSystem.remove_vehicle(driver3)) # False


      