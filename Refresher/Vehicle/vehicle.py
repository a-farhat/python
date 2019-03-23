class vehicle():

    #Class Attributes
    vehicleType = ""
    vehicleYear = ""
    vehicleMake = ""
    vehcileModel = ""    
    wheelCount = 0
    capacity = 0
    doorCount = 0

    #start the vehicle
    def start(self):
        print("Vehicle Started")
    
    #stop the vehicle
    def stop(self):
        print("vehicle Stopped")

    #set the vehicle's number of wheels
    def setNumberOFWheels(self,wheelCount):
        self.wheelCount=wheelCount
    
    def setDoorCount(self,doorCount):
        self.doorCount = doorCount
    
    def setCapacity(self,capacity):
        self.capacity = capacity
    
    def printVehicle(self):
        print("Vehicle Type: " +  self.vehicleType)
        print("Vehicle Year: " +  self.vehicleYear)
        print("Vehicle Make: " +  self.vehicleMake)
        print("Vehicle Model: " +  self.vehcileModel)        
        print("Wheels: " + str(self.wheelCount))
        print("Doors: " + str(self.doorCount))
        print("Capacity: " + str(self.capacity))


    def __init__(self,vehicleInfo):
        #vehicle info is a tuple which is passed when the class is istantiated
        self.vehicleType = vehicleInfo[0]
        self.vehicleYear = vehicleInfo[1]
        self.vehicleMake = vehicleInfo[2]
        self.vehcileModel = vehicleInfo[3]





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