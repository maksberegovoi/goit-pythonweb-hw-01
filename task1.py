import logging
from abc import abstractmethod, ABC

logging.basicConfig(level=logging.INFO, format="%(message)s")


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "EU Spec")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Yamaha", "MT-07")
vehicle2.start_engine()
