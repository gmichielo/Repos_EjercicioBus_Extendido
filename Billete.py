from Cliente import Cliente

class Billete:
    def __init__(self, bus, cliente, num_billete):
        self.__busId = bus
        self.__cliente = cliente
        self.__num_billete = num_billete
    
    def GetBus(self):
        return self.__busId
    
    def GetCliente(self):
        return self.__cliente
    
    def GetNum_Billete(self):
        return self.__num_billete
    
    def SetBus(self, bus):
        self.__busId = bus

    def SetCliente(self, cliente):
        self.__cliente = cliente
    
    def SetNum_Billete(self, num):
        self.__num_billete = num