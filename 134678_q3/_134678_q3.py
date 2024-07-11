
class Vehicle:
  """
  Base class for all vehicles.
  """
  def __init__(self, registration_number, make, model):
    self.registration_number = registration_number
    self.make = make
    self.model = model

  def __str__(self):
    """
    Defines how a Vehicle object is printed.
    """
    return f"Registration Number: {self.registration_number}\nMake: {self.make}\nModel: {self.model}\n"


class Car(Vehicle):
  """
  Car class inherits from Vehicle with added attribute for number of seats.
  """
  def __init__(self, registration_number, make, model, seats):
    super().__init__(registration_number, make, model)
    self.seats = seats

  def __str__(self):
    """
    Overrides the base class __str__ method to include seats information.
    """
    return super().__str__() + f"Seats: {self.seats}\n"


class Truck(Vehicle):
  """
  Truck class inherits from Vehicle with added attribute for cargo capacity.
  """
  def __init__(self, registration_number, make, model, cargo_capacity):
    super().__init__(registration_number, make, model)
    self.cargo_capacity = cargo_capacity

  def __str__(self):
    """
    Overrides the base class __str__ method to include cargo capacity information.
    """
    return super().__str__() + f"Cargo Capacity: {self.cargo_capacity}\n"


class Motorcycle(Vehicle):
  """
  Motorcycle class inherits from Vehicle with added attribute for engine capacity.
  """
  def __init__(self, registration_number, make, model, engine_capacity):
    super().__init__(registration_number, make, model)
    self.engine_capacity = engine_capacity

  def __str__(self):
    """
    Overrides the base class __str__ method to include engine capacity information.
    """
    return super().__str__() + f"Engine Capacity: {self.engine_capacity}\n"


class Fleet:
  """
  Fleet class manages a list of vehicles and provides functionalities to add, display, and search.
  """
  def __init__(self):
    self.vehicles = []

  def add_vehicle(self, vehicle):
    """
    Adds a vehicle object to the fleet list.
    """
    self.vehicles.append(vehicle)

  def display_all_vehicles(self):
    """
    Iterates over the vehicle list and prints details of each vehicle.
    """
    if not self.vehicles:
      print("No vehicles in the fleet yet.")
      return
    for vehicle in self.vehicles:
      print(vehicle)
      print("-" * 20)

  def search_vehicle(self, registration_number):
    """
    Searches the fleet list for a vehicle with the provided registration number.
    Returns the vehicle object if found, otherwise None.
    """
    for vehicle in self.vehicles:
      if vehicle.registration_number == registration_number:
        return vehicle
    return None


# Demonstration
fleet = Fleet()

# Add some vehicles
fleet.add_vehicle(Car("ABC123", "Toyota", "Corolla", 5))
fleet.add_vehicle(Truck("DEF456", "Ford", "F-150", 10000))
fleet.add_vehicle(Motorcycle("GHI789", "Yamaha", "R6", 600))

# Display all vehicles
print("Fleet Vehicles:")
fleet.display_all_vehicles()

# Search for a specific vehicle
search_result = fleet.search_vehicle("DEF456")
if search_result:
  print(f"\nVehicle with registration number DEF456 found:\n {search_result}")
else:
  print(f"\nVehicle with registration number DEF456 not found.")
