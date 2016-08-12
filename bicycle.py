class Bicycle(object):
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
        
BikeA = Bicycle("BikeA","5kg","$100")
BikeB = Bicycle("BikeB","7kg","$250")
BikeC = Bicycle("BikeC","9kg","$500")

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

HappyBikeShop = BikeShops("HappyBikeShop", 5,3,1, 200, 500, 1000, 100, 250, 500)
class Customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    def buy(self, price):
        self.price = price
        self.fund -= self.price
        
Mark = Customers("Mark", 200)
Tim = Customers("Tim", 500)
Carol = Customers("Carol", 1000)



def PrintCustomers():
    print (Mark.name + " has " + str(Mark.fund) + " so he can buy " + str(Mark.fund/HappyBikeShop.AP) + " BikeA or "+str(Mark.fund/HappyBikeShop.BP) + " BikeB or " + str(Mark.fund/HappyBikeShop.CP)+ " BikeC")
    print (Tim.name + " has " + str(Tim.fund) + " so he can buy " + str(Tim.fund/HappyBikeShop.AP) + " BikeA or "+str(Tim.fund/HappyBikeShop.BP) + " BikeB or " + str(Tim.fund/HappyBikeShop.CP)+ " BikeC")
    print (Carol.name + " has " + str(Carol.fund) + " so she can buy " + str(Carol.fund/HappyBikeShop.AP) + " BikeA or "+str(Carol.fund/HappyBikeShop.BP) + " BikeB or " + str(Carol.fund/HappyBikeShop.CP)+ " BikeC")
    
def PrintInventory():
    print (HappyBikeShop.name + " has "+str(HappyBikeShop.AInventory)+" BikeA ", str(HappyBikeShop.BInventory)+" BikeB & "+ str(HappyBikeShop.CInventory)+" BikeC ")
    
def Purchase():
 
    MarkLeft = Mark.fund - HappyBikeShop.AP
    TimLeft = Tim.fund - HappyBikeShop.BP 
    CarolLeft = Carol.fund - HappyBikeShop.CP
    
    print("Mark bought "+ BikeA.modelName + " for "+str(HappyBikeShop.AP) +" and got " +str(MarkLeft) + " left.")
    print("Tim bought "+ BikeB.modelName + " for "+str(HappyBikeShop.BP) + " and got " +str(TimLeft) + " left.")
    print("Carol bought "+ BikeC.modelName + " for "+str(HappyBikeShop.CP) + " and got " +str(CarolLeft) + " left.")
    
def End():
    
    HappyBikeShop.sell(1,1,1)
    print(str(HappyBikeShop.AInventory)+" BikeA left.")
    print(str(HappyBikeShop.BInventory)+" BikeB left.")
    print(str(HappyBikeShop.CInventory)+" BikeC left.")
    Total = str(HappyBikeShop.calProfit())
    print("They made "+ Total+'.')


if __name__ == '__main__':
    PrintCustomers()
    PrintInventory()
    Purchase()
    End()
        
    
    