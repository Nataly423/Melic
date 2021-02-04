#!/usr/bin/python
from main import SecureInfo
import sys


ss = SecureInfo()
json_name = sys.argv

try:
    ss.read_json(json_name[1])
except Exception as e:
    print("**********\nHubo un error leyendo el archivo .json: {}\n**********".format(e))
