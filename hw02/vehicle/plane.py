from vehicle_base import VehicleBase

from vehicle_base import VehicleBase

class Plane(VehicleBase):
    def __init__(self, vendor, model, power, passengers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._passengers = passengers

    def beep(self):
        return "Сlickety-clack"

    def __str__(self):
        return f"Train.\n" \
               f"{self._vendor} {self._model} {self._power}. {self._wagons} wagons." \
               f"Signal: {self.beep()}"

if __name__ == '__main__':
    DemoTrain = Train(vendor="Vendor",
                  model="Model",
                  weight_kg="weight",
                  speed_km_h="speed",
                  payload_kg="payload",
                  power="power",
                  environment="ground",
                  wagons=20)
    print(DemoTrain)
    print(DemoTrain.beep())
