#!/usr/bin/python
from main import SecureInfo
import sys


ss = SecureInfo()
json_name = sys.argv

try:
    ss.create_db()
except Exception as e:
    print("**********\nHubo un error creando la ddbb: {}\n**********".format(e))
