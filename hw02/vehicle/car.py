from vehicle.vehicle_base import VehicleBase


class Car(VehicleBase):
    def __init__(self, passengers, *args, **kwargs):
        kwargs["environment"] = "ground"
        kwargs["fuel_type"] = "petrol, liter"
        print(kwargs)
        super().__init__(*args, **kwargs)
        self._passengers = passengers

    def signal(self) -> str:
        return "beep"

    @property
    def fuel(self):
        return f"{super().fuel} + {self.fuel_type()}"

    def __str__(self):
        return (f"Car.\n"
               f"{self._passengers} passengers.\n"
               f"{super().__str__()}\n"
               f"Signal: {self.signal()}\n")


if __name__ == '__main__':
    DemoCar = Car(vendor="Vendor demo",
                  model="Demo model",
                  weight_kg=3000,
                  speed_km_h=120,
                  payload_kg=1000,
                  passengers=3)
    print(DemoCar)
    print(f"Car signal: {DemoCar.beep()}")
