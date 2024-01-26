class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.size = [0, big, medium, small]
        self.cars = [0] * 4

    def addCar(self, carType: int) -> bool:
        if self.cars[carType] == self.size[carType]:
            return False
        self.cars[carType] += 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
