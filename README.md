CRUD DE CLIENTES EN PYTHON UTILIZANDO FLASK# Cliente CRUD - Aplicación de Gestión de Clientes con Python, Flask y Firebase

La aplicación Cliente CRUD es un sistema de gestión de clientes que utiliza el framework Flask en Python, así como Firebase para realizar operaciones de Crear, Leer, Actualizar y Eliminar (CRUD) en una base de datos de clientes. Además, se aplica la programación orientada a objetos (POO).

## Características

- Crear un nuevo cliente con los siguientes campos:
  - Nombre
  - Apellido
  - Domicilio
  - Teléfono
  - Correo Electrónico

- Leer información de clientes existentes.

- Actualizar los datos de un cliente existente.

- Eliminar un cliente de la base de datos.

- Buscar un cliente por apellido.

## Requisitos

Para ejecutar la aplicación, se deben tener instalados los siguientes componentes:

Python: Descargar Python
Flask: Instalar usando pip (pip install Flask)
Firebase: Instalar usando pip (pip install firebase-admin)

El archivo que se debe ejecutar es el de app.py

## Organización

El proyecto se organiza de la siguiente manera:

- app: Contiene la lógica principal de la aplicación CRUD.
- clasePersona: Plantilla para crear un Cliente, con sus correspondientes atributos. Funciona como superclase o clase abstracta
- claseCliente: Plantilla que hereda de clasePersona y también posee sus atributos y métodos propios. 
- templates/: Almacena las plantillas HTML utilizadas.
- static/: Contiene archivos estáticos como hojas de estilo (CSS) para dar estilo a la aplicación.
- credentials/: Posee las credenciales de la base de datos de Firebase.
- firebaseConfig: Realiza la configuración de la base de datos de Firebase.
- models/: Es la carpeta que contiene el clienteModel, el cual es el encargado de realizar las consultas a la base de datos de Firebase.
