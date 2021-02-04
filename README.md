# Melic
Python 🐍

### Pasos:

Instalar python 
https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg

####Ejecutar 
`$pip3 install -r requirements.txt`

Esto instalará la base de datos y la consola

`$pip3 install -r requirements.txt`

Para popular la base de datos de usuarios:

`$python3 create_users.py`

Para crear los managers relacionados a los Usuarios en el **CSV**
dónde demo.csv es el archivo con la data:
https://github.com/Nataly423/Melic/blob/main/demo.csv

`$python3 read_csv.py demo.csv`

Luego de esto vamos a subir el **json** on la información a validar por los managers
https://github.com/Nataly423/Melic/blob/main/demo.json

`$python3 read_json.py demo.json`

Finalmente podemos validar en un gestor de bases de datos, con el archivo database.db


