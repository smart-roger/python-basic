from abc import abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class VehicleBaseParams:
    vendor: str
    model: str
    weight_kg: float
    speed_km_h: float
    payload_kg: float
    fuel_type: str
    environment: str


class VehicleBase:
    """Base class for vehicle classes. """

    def __init__(self, vendor, model, weight_kg, speed_km_h, payload_kg, fuel_type, environment):
        self._params = VehicleBaseParams(vendor, model, weight_kg, speed_km_h, payload_kg, fuel_type, environment)
        self._fuel = 0

    @abstractmethod
    def signal(self) -> str:
        """Demonstrate vehicle sound."""
        raise NotImplementedError

    @abstractmethod
    def move(self, km):
        """Simulate vehicle moving"""
        raise NotImplementedError

    @property
    def fuel(self):
        return self._fuel

    def fuel_type(self):
        return self._params.fuel_type

    def fill_up(self, value, fuel_type):
        if value < 0:
            raise ValueError('Fuel must be zero or positive value!')
        if fuel_type != self._params.fuel_type:
            raise ValueError(f"Wrong fuel type. Vehicle use {self._params.fuel_type}! (not {fuel_type})")
        self._fuel = value

    def use_fuel(self, fuel):
        if self._fuel < fuel:
            raise ValueError('No enough fuel!')
        else:
            self._fuel -= fuel

    def __str__(self):
        return (f"{str(self._params)}\n"
               f"Fuel:{self._fuel} {self._params.fuel_type}.")


if __name__ == '__main__':
    print("""Base class for vehicle classes.""")
    print(dir(VehicleBase))
