class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.maxb = big
        self.maxm = medium
        self.maxs = small
        self.curb = 0
        self.curm = 0
        self.curs = 0

    def addCar(self, carType: int) -> bool:
        if carType == 3 and self.curs < self.maxs:
            self.curs += 1
            return True
        elif carType == 2 and self.curm < self.maxm:
            self.curm += 1
            return True
        elif carType == 1 and self.curb < self.maxb:
            self.curb += 1
            return True
        else:
            return False
