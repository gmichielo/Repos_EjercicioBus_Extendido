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