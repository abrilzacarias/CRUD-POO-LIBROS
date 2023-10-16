import firebase_admin  
from firebase_admin import db
from clasePersona import Persona
from claseLibro import Libro

class Bibliotecario(Persona):
    def __init__(self, nombre, apellido, usuario): #faltaria contrasena para un login
        super().__init__(nombre, apellido)
        self.__usuario = usuario
        self.__stockLibros = []

    def getUsuario(self):
        return self.__usuario
    
    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getStockLibros(self):
        return self.__stockLibros
    
    def setStockLibros(self, stockLibros):
        self.__stockLibros = stockLibros

    #metodo privado que se encarga del get y set del stock de libros
    def __agregarStockLibros(self, libroNuevo):
        stock = self.getStockLibros()
        print(f'stock actual {self.getStockLibros()}')
        stock.append(libroNuevo)
        self.setStockLibros(stock)
        print(f'stock nuevo {self.getStockLibros()}')
        return stock
    
    def getAgregarStockLibros(self, libroNuevo):
        return self.__agregarStockLibros(libroNuevo)

    #Método encargado de recibir los datos del cliente y crearlo en la base de datos
    def agregarLibro(self, nombre, autor, edicion, cantPaginas):
        # Crea un nuevo cliente en Firebase
        ref = db.reference('/libros')
        idLibro = ref.push({
            'nombre': nombre,
            'autor': autor,
            'edicion': edicion,
            'cantidadPaginas': cantPaginas
        })
        libro = Libro(nombre, autor, edicion, cantPaginas)
        libro.setIdLibro(idLibro.key)
        self.getAgregarStockLibros(libro)
        return libro
    
    #Método encargado de obtener los datos de todos los clientes
    def obtenerLibros(self):
        # Lee todos los clientes desde Firebase
        ref = db.reference('/libros')
        return ref.get()

    #Método encargado de obtener los datos de un cliente por su ID
    def obtenerLibroPorId(self, idLibro):
        # Lee un cliente específico por su ID
        ref = db.reference('/libros')
        return ref.child(idLibro).get()

    #Método encargado de actualizar los datos de un cliente
    def actualizarLibro(self, idLibro, nombre, autor, edicion, cantPaginas):
        # Actualiza un cliente existente
        ref = db.reference('/libros')
        ref.child(idLibro).update({
            'nombre': nombre,
            'autor': autor,
            'edicion': edicion,
            'cantidadPaginas': cantPaginas
        })
        
        librosStock=self.getStockLibros()
        print(f'stock libros actualizar {self.getStockLibros()}') #
        print(librosStock)
        for libro in librosStock:
            print(libro.obtenerDatos())

        for libro in librosStock:
            if libro.getIdLibro() == idLibro:
                libro.setNombre(nombre) 
                libro.setAutor(autor)
                libro.setEdicion(edicion)
                libro.setCantPaginas(cantPaginas)
        return librosStock

    #Método encargado de eliminar los datos de un cliente
    def eliminarLibro(self, idLibro):
        # Elimina un cliente por su ID
        ref = db.reference('/libros')
        ref.child(idLibro).delete()

        librosStock=self.getStockLibros()
        for libro in librosStock:
            if libro.getIdLibro() == idLibro:
                librosStock.remove(libro)
        print(librosStock)
        return librosStock

    #Método encargado de obtener los datos de un cliente por su apellido
    def obtenerLibroPorNombre(self, nombreLibro):
        ref = db.reference('/libros')
        # Realiza una consulta para buscar clientes por nombre
        resultados = ref.order_by_child('nombre').equal_to(nombreLibro).get()
        return resultados