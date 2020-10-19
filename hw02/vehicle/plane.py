from vehicle.vehicle_base import VehicleBase

class Plane(VehicleBase):
    def __init__(self, passengers, range_km, *args, **kwargs):
        kwargs["environment"] = "air"
        kwargs["fuel_type"] = "kerosene"
        super().__init__(*args, **kwargs)

        self._passengers = passengers
        self._range_km = range_km


    def beep(self):
        return "Nope"

    def __str__(self):
        return f"Plane.\n" \
               f"{super().__str__()} \n" \
               f"Passengers: {self._passengers} passengers. Flight range: {self._range_km} km.\n" \
               f"Signal: {self.beep()}"

if __name__ == '__main__':
    DemoPlane = Plane(0, 1, "demo_vendor", "demo_model", 2, 3, 4)
    print(DemoPlane)