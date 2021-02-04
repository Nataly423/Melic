# Melic
Python 🐍

### Pasos:

Instalar python 
https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg

####Ejecutar 
`$pip3 install -r requirements.txt`

Crear las bases de datos por medio de:

`$python create_db.py`

se crearán las bases de datos:

        **registers**
        -------------
        id
        db_name
        email_owner
        email_manager
        classification

        **user**
        -------------
        id
        email
        name
        age
        phone

        **user_manager**
        -------------
        id
        user_id
        user_state
        user_manager_email


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
![alt text](https://github.com/Nataly423/Melic/blob/main/1.png)
![alt text](https://github.com/Nataly423/Melic/blob/main/2.png)

Revisar el registro final en la tabla user_manager:
`$SELECT * FROM user_manager`

![alt text](https://github.com/Nataly423/Melic/blob/main/3.png)

