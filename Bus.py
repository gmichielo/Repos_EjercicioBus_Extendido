class Bus:
    def __init__(self, bus_id, capacidad):
        self._bus_id = bus_id
        self._capacidad = capacidad
        self._billetes = []
    def SetBusId(self, bus_id):
        self._bus_id = bus_id
    def SetCapacidad(self, capacidad):
        self._capacidad = capacidad
    def GetBusID(self):
        return self._bus_id
    def GetCapacidad(self):
        return self._capacidad
    def GetBilletes(self):
        return self._billetes

    
        
        
        