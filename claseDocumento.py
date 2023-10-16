#Clase DOCUMENTO la cual actua de superclase
class Documento:
    def __init__(self, nombre, autor, edicion):
        self.__nombre = nombre
        self.__autor = autor
        self.__edicion = edicion
    
    #ENCAPSULAMIENTO Y ABSTRACCION
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, autor):
        self.__autor = autor

    def getEdicion(self):
        return self.__edicion
    
    def setEdicion(self, edicion):
        self.__edicion = edicion

    #POLIMORFISMO: tanto la clase LIBRO como la clase DOCUMENTO poseen un metodo llamado obtenerDatos, pero este se comporta de manera distinta.
    def obtenerDatos(self):
        return self.getNombre(), self.getAutor(), self.getEdicion()