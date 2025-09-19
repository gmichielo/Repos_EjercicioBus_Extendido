class Cliente:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def SetNombre(self, nombre):
        self.__nombre = nombre  
          
    def SetApellido(self, apellido):
        self.__apellido = apellido
        
    def GetNombre(self):
        return self.__nombre
    
    def GetApellido(self):
        return self.__apellido
    
    def __str__(self):
        return f'Mi nombre es {self.GetNombre()} {self.GetApellido()}'