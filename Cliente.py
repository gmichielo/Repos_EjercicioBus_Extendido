class Cliente:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
    def SetNombre(self, nombre):
        self._nombre = nombre    
    def SetApellido(self, apellido):
        self._apellido = apellido
    def GetNombre(self):
        return self._nombre
    def GetApellido(self):
        return self._apellido
    def __str__(self):
        return f'Mi nombre es {self.GetNombre()} {self.GetApellido()}'