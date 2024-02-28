import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt
from Crypto.Cipher import AES


def getChromeDateTime(ChromDate):
    if ChromDate != 86400000000 and ChromDate:
        try:
            return datetime(1601, 1, 1) + timedelta(microseconds=ChromDate)
        except Exception as e:
            print(e)
            return ChromDate
    else:
        return " "
