from Cliente import Cliente

class Billete:
    def __init__(self, bus, cliente, num_billete):
        self._busId = bus
        self._cliente = cliente
        self._num_billete = num_billete
    
    def GetBus(self):
        return self._busId
    
    def GetCliente(self):
        return self._cliente
    
    def GetNum_Billete(self):
        return self._num_billete
    
    def SetBus(self, bus):
        self._busId = bus

    def SetCliente(self, cliente):
        self._cliente = cliente
    
    def SetNum_Billete(self, num):
        self._num_billete = num