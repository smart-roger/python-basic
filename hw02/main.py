from vehicle.plane import Plane
from vehicle.ship import Ship
from vehicle.car import Car

if __name__ == '__main__':
    print("Demo.")
    example_delimiter = "=" * 100

    #RaceCar example
    RaceCar = Car(vendor="Toyota",
                  model="TS050 Hybrid",
                  weight_kg=878,
                  speed_km_h=431,
                  payload_kg=200,
                  passengers=0)

    RaceCar.fill_up(100, "petrol, liter")
    print(RaceCar.fuel)
    RaceCar.use_fuel(50)
    RaceCar.use_fuel(10)
    print(RaceCar.signal())
    print(f"RaceCar example:\n{RaceCar}")
    print(dir(RaceCar))
    print(example_delimiter)

    #Minivan example
    Minivan = Car(vendor="Fiat",
                  model="600",
                  weight_kg=585,
                  speed_km_h=95,
                  payload_kg=500,
                  passengers=3)
    print(f"Minivan example:\n{Minivan}")
    print(dir(Minivan))
    print("="*100)

    #Cutter example
    print("Cutter example:\n")
    Cutter = Ship(model="GT245",
                  vendor="Glastron",
                  weight_kg=1800,
                  speed_km_h=90,
                  payload_kg=1800,
                  )
    print ("After fill up:")
    Cutter.fill_up(100, "petrol, liter")
    print(Cutter)
    print(dir(Cutter))

    print("Using 50 petrol litres.")
    Cutter.use_fuel(50)
    print(Cutter)
    print(example_delimiter)

    #Plane example
    print("Plane example:")
    Plane_MC_21 = Plane(vendor="OAC",
                        model="MC-21-300",
                        weight_kg=72560,
                        speed_km_h=870,
                        payload_kg=22600,
                        passengers=211,
                        range_km=6000)
    Plane_MC_21.fill_up(20400, "kerosene")
    print(Plane_MC_21)
    print(dir(Plane_MC_21))
    print(example_delimiter)