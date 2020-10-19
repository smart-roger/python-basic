from vehicle.vehicle_base import VehicleBase

class Ship(VehicleBase):
    def __init__(self, *args, **kwargs):
        kwargs["environment"] = "water"
        kwargs["fuel_type"] = "petrol, liter"
        super().__init__(*args, **kwargs)

    def beep(self)->str:
        return "Tooooo"

    def __str__(self):
        return f"Ship.\n" \
               f"{super().__str__()}\n"\
               f"Signal: {self.beep()}"

if __name__ == '__main__':
    DemoShip = Ship(vendor="Esso International Shipping Co Ltd",
                  model="Esso Atlantic",
                  weight_kg="weight",
                  speed_km_h=29,
                  payload_kg=517000)
    print(DemoShip)
    print(f"Ship signal: {DemoShip.beep()}")