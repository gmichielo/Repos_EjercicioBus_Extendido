class Bus:
    def __init__(self, bus_id, capacidad):
        self.__bus_id = bus_id
        self.__capacidad = capacidad
        self.__billetes = []
        
    def SetBusId(self, bus_id):
        self.__bus_id = bus_id
        
    def SetCapacidad(self, capacidad):
        self.__capacidad = capacidad
        
    def GetBusID(self):
        return self.__bus_id
    
    def GetCapacidad(self):
        return self.__capacidad
    
    def GetBilletes(self):
        return self.__billetes
    
    def GetVendidos(self):
        return len(self.__billetes)
    
    def GetLibres(self):
        return self.__capacidad - len(self.__billetes)
    
    def VenderBilletes(self, billete):
        if self.GetLibres() <= 0:
            return None, f"Error, el bus {self.__bus_id} esta lleno. No hay asientos libres."
        else:
            self.__billetes.append(billete)
    def DevolverBilletes(self, cliente):
        for b in self._billetes:
            c = b.GetCliente()
            if c.GetNombre() == cliente.GetNombre() and c.GetApellido() == cliente.GetApellido():
                self._billetes.remove(b)
                return f"Billete {b.GetTicketId()} de {c.GetNombre()} {c.GetApellido()} devuelto."
        return f"Error, el cliente {cliente.GetNombre()} {cliente.GetApellido()} no tiene billetes en este bus."
    
        


    
        
        
        