from abc import abstractmethod

class VehicleBase:
    """Base class for vehicle classes. """
    def __init__(self, weight_kg, speed_km_h, payload_kg, environment):
        self._weight_kg = weight_kg
        self._speed_km_h = speed_km_h
        self._payload_kg = payload_kg
        self._environment = environment

    @abstractmethod
    def beep(self):
        """Demonstrate vehicle sound."""
        pass

    def __str__(self):
        return f"Base class for vehicle. Weight: {self._weight}. Speed (km\h): {self._speed_km_h}. Payload: {self._payload}. Environment: {self._environment}."

if __name__ == '__main__':
    print("""Base class for vehicle classes.""")
    print(dir(VehicleBase))