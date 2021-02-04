#!/usr/bin/python
from main import SecureInfo


ss = SecureInfo()

try:
    ss.send_email()
except Exception as e:
    print("**********\nHubo un error leyendo el archivo .json: {}\n**********".format(e))
