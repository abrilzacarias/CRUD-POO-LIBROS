#Clase PERSONA la cual actua de superclase
class Persona:
    def __init__(self, nombre, apellido, domicilio=None, telefono=None, email=None):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__domicilio = domicilio
        self.__telefono = telefono 
        self.__email = email
    
    #ENCAPSULAMIENTO Y ABSTRACCION

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, apellido):
        self.__apellido = apellido

    def getDomicilio(self):
        return self.__domicilio
    
    def setDomicilio(self, domicilio):
        self.__domicilio = domicilio

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__telefono = telefono
    
    def getEmail(self):
        return self.__email 
    
    def setEmail(self, email):
        self.__email = email

    #POLIMORFISMO: tanto la clase Cliente como la clase Persona poseen un metodo llamado obtenerDatos, pero este se comporta de manera distinta.
    def obtenerDatos(self):
        return self.getNombre(), self.getApellido(), self.getDomicilio(), self.getTelefono(), self.getEmail()