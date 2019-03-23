from vehicle import vehicle

def main():
    #Instatiate vehicle here
    #car = vehicle("Car",("",""),{"":"","":""})
    highlander = ("Car","2014","Toyota","Highlander")
    car = vehicle(highlander)
    car.setDoorCount(4)
    car.setNumberOFWheels(4)
    car.setCapacity(7)
    car.printVehicle()
    car.start()
    car.stop()



if __name__ == "__main__":
  main()