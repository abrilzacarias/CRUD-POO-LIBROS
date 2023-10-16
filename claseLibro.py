from claseDocumento import Documento
#Clase CLIENTE hereda de PERSONA, la cual actua como superclase
class Libro(Documento):
    def __init__(self, nombre, autor, edicion, cantPaginas):
        super().__init__(nombre, autor, edicion)
        self.__cantPaginas = cantPaginas
        self.__idLibro = None
    #ABSTRACCION Y ENCAPSULAMIENTO
    def getIdLibro(self):
        return self.__idLibro
    
    def setIdLibro(self, idLibro):
        self.__idLibro = idLibro
    
    def getCantPaginas(self):
        return self.__cantPaginas
    
    def setCantPaginas(self, cantPaginas):
        self.__cantPaginas = cantPaginas

    #POLIMORFISMO: tanto la clase LIBRO como la clase DOCUMENTO poseen un metodo llamado obtenerDatos, pero este se comporta de manera distinta.
    def obtenerDatos(self):
        return f'''
        Nombre del libro {self.getNombre()} del autor: {self.getAutor()}.
        Edicion: {self.getEdicion()}
        Cantidad de paginas {self.getCantPaginas()}
        ID del libro: {self.getIdLibro()} '''
        