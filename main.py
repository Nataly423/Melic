import sqlite3
import csv
import json


class SecureInfo:
    def __init__(self):
        pass

    def read_csv(self, file_name):
        with open(file_name, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    print('\n \n Las columnas son {}\n \n '.format(", ".join(row)))
                    line_count += 1
                print("row_id: ", row["row_id"], " ", end='')
                print("user_id: ", row["user_id"], " ", end='')
                print("user_state: ", row["user_state"], " ", end='')
                print("user_manager: ", row["user_manager"], " ", '\n', end='')
                line_count += 1
                self.storage_user_manager([row["row_id"], row["user_id"], row["user_state"], row["user_manager"]])

            print('\n \n Se procesaron {} lineas correctamente.'.format(line_count - 1))

    def read_json(self, json_file):
        """
            [
                {
                    "db_name": "pagos",
                    "email_owner": "caztro@demo.com",
                    "classification": "low",
                },
                {
                    "db_name": "retiros",
                    "email_owner": "cambeta@demo.com",
                    "classification": "high",
                }
            ]
        """

        with open(json_file, "r") as read_file:
            data = json.load(read_file)
            for owner in data:
                email_manager = self.get_values(email_owner=owner['email_owner'])

                if email_manager:
                    email_manager = email_manager[0]
                    owner["email_manager"] = email_manager["user_manager_email"]
                    print("Registrando manager {} \n\n".format(email_manager["user_manager_email"]))
                else:
                    owner["email_manager"] = None
                    print("****ERROR***** El usuario {} no tiene manager \n\n".format(owner["email_owner"]))

                self.storage_db(data=owner.values())

        self.send_email()

    def create_db(self):
        conn = sqlite3.connect('database.db')
        print("conectó a la ddbb correctamente.....")

        # nombre de la DB (origen JSON), email del owner (origen JSON), email del manager (origen CSV), clasificación de la DB (origen JSON).

        conn.execute('CREATE TABLE registers (id INTEGER PRIMARY KEY AUTOINCREMENT, db_name TEXT, email_owner TEXT, email_manager TEXT, classification TEXT)')
        conn.execute('CREATE TABLE user (id INTEGER PRIMARY KEY, email TEXT, name TEXT, age TEXT, phone TEXT)')
        conn.execute('CREATE TABLE user_manager (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id REFERENCES user(id), user_state TEXT, user_manager_email TEXT)')

        print("ddbb creada correctamente**********")
        conn.close()

    def storage_db(self, data):
        """
        data = {
            db_name: str,
            email_owner: str,
            email_manager: str,
            classification: str
        }
        """
        try:
            conn = sqlite3.connect('database.db')

            val_db_name, val_email_owner, val_email_manager, val_classification = data
            cur = conn.cursor()
            query = '''INSERT INTO registers (db_name, email_owner, classification, email_manager) 
            VALUES ("{}", "{}", "{}", "{}")'''.format(
                val_db_name, val_email_owner, val_email_manager, val_classification
            )

            cur.execute(query)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print("error in insert operation {}".format(e))

        finally:
            conn.close()

    def storage_user_manager(self, data):
        """
        data = {
            row_id: str,
            user_id: str,
            user_state: str,
            user_manager_email: str
        }
        """
        try:
            conn = sqlite3.connect('database.db')
            print("Conectó a la ddbb correctamente.....")

            val_row_id, val_user_id, val_user_state, val_user_manager_email = data
            cur = conn.cursor()
            query = '''INSERT INTO user_manager (user_id, user_state, user_manager_email) 
            VALUES ("{}", "{}", "{}")'''.format(val_user_id, val_user_state, val_user_manager_email)

            cur.execute(query)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print("error in insert operation {}".format(e))

        finally:
            print("Registro creado correctamente**********")
            conn.close()

    def storage_user(self, data):
        """
        data = {
            email: str,
            name: str,
            age: str,
            phone: str
        }
        """
        try:
            conn = sqlite3.connect('database.db')
            print("Conectó a la ddbb correctamente.....")

            for user in data:
                val_email, val_name, val_age, val_phone = user
                cur = conn.cursor()
                query = '''INSERT INTO user (email, name, age, phone) 
                VALUES ("{}", "{}", "{}", "{}")'''.format(val_email, val_name, val_age, val_phone)

                cur.execute(query)
                conn.commit()

        except Exception as e:
            conn.rollback()
            print("error in insert operation {}".format(e))

        finally:
            print("Registro creado correctamente**********")
            conn.close()

    def get_values(self, email_owner):
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()

        print("\n\nObteniendo manager del usuario {}\n".format(email_owner))
        query = """
            select user_manager_email from user_manager where 
            user_id=(select id from user where email='{}' LIMIT 1) LIMIT 1""".format(email_owner)

        cur.execute(query)

        rows = cur.fetchall()
        return rows

    def send_email(self):
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()

        query = """select * from registers where classification='high'"""

        cur.execute(query)

        rows = cur.fetchall();
        for value in rows:
            if value["email_manager"]:
                print(
                        '\nEnviando email a: ' + value["email_manager"] +
                        '\n con clasificación: '+
                        value["classification"] +
                        '\n del usuario: '+
                        value["email_owner"]
                )
                print("......................")

        return rows
 
