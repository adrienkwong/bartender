class Bicycle(object):
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        


class BikeShops(object):
    def __init__(self, name, AInventory, BInventory, CInventory, AP, BP, CP, AC, BC, CC):
        self.name = name
        self.AInventory = AInventory
        self.BInventory = BInventory
        self.CInventory = CInventory
        self.AP = AP
        self.BP = BP
        self.CP = CP
        self.AC = AC
        self.BC = BC
        self.CC = CC
    def sell(self, ASold, BSold, CSold):
        self.AInventory -= ASold
        self.BInventory -= BSold
        self.CInventory -= CSold
    
    def calProfit(self):
        profit = (self.AP - self.AC) + (self.BP - self.BC) + (self.CP - self.CC)
        return profit


class Customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    def buy(self, price):
        self.price = price
        self.fund -= self.price
        
