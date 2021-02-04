#!/usr/bin/python
from main import SecureInfo
import sys


ss = SecureInfo()
csv_name = sys.argv

try:
    ss.read_csv(csv_name[1])
except Exception as e:
    print("**********\nHubo un error leyendo el archivo .csv: {}\n**********".format(e))
