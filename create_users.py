#!/usr/bin/python
from main import SecureInfo
import sys


ss = SecureInfo()
json_name = sys.argv

user_list = [
    ["nathaly@demo.com", "nathaly", "25", "535525245"],
    ["nathaly1@demo.com", "nathaly", "21", "131121241"],
    ["nathaly2@demo.com", "nathaly", "22", "232222242"],
    ["nathaly3@demo.com", "nathaly", "23", "333323243"],
    ["nathaly4@demo.com", "nathaly", "24", "434424244"],
    ["nathaly5@demo.com", "nathaly", "25", "535525245"],
    ["nathaly6@demo.com", "nathaly", "26", "636626246"],
    ["nathaly7@demo.com", "nathaly", "27", "737727247"],
    ["nathaly8@demo.com", "nathaly", "28", "838828248"],
    ["nathaly9@demo.com", "nathaly", "29", "939929249"],
    ["nathaly10@demo.com", "nathaly", "17", "737717247"],
]

try:
    ss.storage_user(data=user_list)
except Exception as e:
    print("**********\nHubo un error creando los usuarios .json: {}\n**********".format(e))
