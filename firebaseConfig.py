import firebase_admin
from firebase_admin import credentials, db

#carga del certificado del proyecto
cred = credentials.Certificate("credentials/crudLibros.json")

#referencia a la base de datos en tiempo real
firebase_admin.initialize_app(cred,{'databaseURL':'https://crud-libros-15de0-default-rtdb.firebaseio.com/'})
