from Billete import Billete

class Bus:
    def __init__(self, bus_id, capacidad, destino):
        self.__bus_id = bus_id
        self.__capacidad = capacidad
        self.__billetes = []
        self.__destino = destino
        
    def SetBusId(self, bus_id):
        self.__bus_id = bus_id
        
    def SetCapacidad(self, capacidad):
        self.__capacidad = capacidad

    def SetDestino(self, destino):
        self.__destino = destino
        
    def GetBusID(self):
        return self.__bus_id
    
    def GetCapacidad(self):
        return self.__capacidad
    
    def GetBilletes(self):
        return self.__billetes
    
    def GetDestino(self):
        return self.__destino
    
    def GetVendidos(self):
        return len(self.__billetes)
    
    def GetLibres(self):
        return self.__capacidad - len(self.__billetes)
    
    def VenderBilletes(self, billete):
        if self.GetLibres() <= 0:
            return None, f"\033[31mError, el bus {self.__bus_id} esta lleno. No hay asientos libres.\033[0m\n"
        else:
            self.__billetes.append(billete)
            return f"\033[32mTu compra se hizo con exito: Tu numero de billete es #{billete.GetNum_Billete()} en el Bus #{self.__bus_id}, con destino {self.__destino}\033[0m\n"  
            
    def DevolverBilletes(self, cliente, num_billete):
        for b in self.__billetes:
            c = b.GetCliente()
            mismo_cliente = (
                c.GetNombre().strip().lower() == cliente.GetNombre().strip().lower() and
                c.GetApellido().strip().lower() == cliente.GetApellido().strip().lower()
            )
            if b.GetNum_Billete() == num_billete and mismo_cliente:
                self.__billetes.remove(b)
                return f"Billete {num_billete} de {c.GetNombre()} {c.GetApellido()} devuelto en bus {self.__bus_id}."
            
        return f"\033[31mError, el cliente {cliente.GetNombre()} {cliente.GetApellido()} no tiene billetes en este bus.\033[0m\n"
    
    def Estado(self):
        return f"\033[35mBus {self.__bus_id} Destino: {self.__destino}\n Capacidad: {self.__capacidad}\n Vendidos: {len(self.__billetes)}\n Libres: {self.__capacidad - len(self.__billetes)}\033[0m\n"


        


    
        
        
        