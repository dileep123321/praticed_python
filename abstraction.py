class Car:
    def __init__(self, brand):
        self.brand = brand
        self.__engine_on = False  

    
    def start(self):
        self.__engine_on = True
        print(f"{self.brand} engine started ")

    def drive(self, speed):
        if self.__engine_on:
            self.__change_gear(speed)
            print(f"Driving at {speed} km/h")
        else:
            print("Start the engine first!")

    def stop(self):
        self.__engine_on = False
        print(f"{self.brand} car stopped ")

    
    def __change_gear(self, speed):
        print("Gear shifted automatically")


my_car = Car("Toyota Supra GT")
my_car.start()
my_car.drive(40)
my_car.stop()
