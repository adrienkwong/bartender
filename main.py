from bicycle import Bicycle
from bicycle import BikeShops
from bicycle import Customers

BikeA = Bicycle("BikeA","5kg","$100") 
BikeB = Bicycle("BikeB","7kg","$250")
BikeC = Bicycle("BikeC","9kg","$500")

HappyBikeShop = BikeShops("HappyBikeShop", 5,3,1, 200, 500, 1000, 100, 250, 500)
        
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
        
    
    