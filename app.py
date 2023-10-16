from flask import Flask, render_template, request, redirect, url_for
from firebaseConfig import *
from claseBibliotecario import Bibliotecario

app = Flask(__name__)
#instancia del modelo de cliente
# Crear una instancia de Bibliotecario en un contexto de aplicación
with app.app_context():
    administrador = Bibliotecario('abril', 'zacaria', 'abril15')

@app.route('/')
def index():
    busqueda=True
    nombre = request.args.get('nombre')
    
    if nombre:
        # Si se proporciona un apellido, realiza la búsqueda
        resultadosLibrosNombre = administrador.obtenerLibroPorNombre(nombre)
        if resultadosLibrosNombre:
            # Si hay resultados, los mostramos
            return render_template('index.html', libros=resultadosLibrosNombre, search_term=nombre, busqueda=False, msj="Resultados para libros con el nombre: " + nombre)
        else:
            # Si no hay resultados, mostramos un mensaje
            return render_template('index.html', message="No se encontraron resultados para libros con el nombre: " + nombre)
    else:
        # Si no se proporciona un apellido, muestra a todos los clientes
        librosLista = administrador.obtenerLibros() 
        if librosLista:
            # Si hay clientes, los mostramos
            return render_template('index.html', libros=librosLista, busqueda=busqueda)
        else:
            # Si no hay clientes, mostramos un mensaje
            return render_template('index.html', message="No hay clientes en la base de datos. Agregue uno para visualizar.")

@app.route('/anadirLibro', methods = ['GET','POST'])
def anadirLibro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        edicion = request.form['edicion']
        cantPaginas = request.form['cantPaginas']

        administrador.agregarLibro(nombre, autor, edicion, cantPaginas)
        
        return redirect('/')
    else:  
        return render_template('anadirLibro.html')
    
@app.route('/modificarLibro/<idLibro>', methods=['GET', 'POST'])
def modificarLibro(idLibro):
    libro = administrador.obtenerLibroPorId(idLibro)

    if request.method == 'POST':
        nombre = request.form['nombre']
        autor = request.form['autor']
        edicion = request.form['edicion']
        cantPaginas = request.form['cantPaginas']
        administrador.actualizarLibro(idLibro, nombre, autor, edicion, cantPaginas)
        return redirect('/')
    else:
        return render_template('modificarLibro.html', libro=libro, idLibro=idLibro)

@app.route('/eliminarLibro/<idLibro>', methods=['GET', 'POST'])
def eliminarLibro(idLibro):
    administrador.eliminarLibro(idLibro)
    return redirect('/')

@app.route('/buscarLibro')
def buscarLibro():
    nombre = request.args.get('nombre')
    return redirect(url_for('index', nombre=nombre))

if __name__ == '__main__':
    app.run(debug=True)