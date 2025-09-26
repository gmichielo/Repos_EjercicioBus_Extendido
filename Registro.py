class Registro:
    def __init__(self, usuario, contrasenya, correo):
        self.__usuario = usuario
        self.__contrasenya = contrasenya
        self.__correo = correo

    def GetUsuario(self): 
        return self.__usuario
    def GetContrasenya(self): 
        return self.__contrasenya
    def GetCorreo(self): 
        return self.__correo

    def SetUsuario(self, usuario):
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío")
        self.__usuario = usuario

    def SetContrasenya(self, contrasenya):
        if len(contrasenya) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        self.__contrasenya = contrasenya

    def SetCorreo(self, correo):
        dominio_empresa = "@viajesterrestres.com"
        if not correo.endswith(dominio_empresa):
            raise ValueError(f"El correo debe terminar en {dominio_empresa}")
        self.__correo = correo