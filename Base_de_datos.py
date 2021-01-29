import psycopg2
import sys
import pprint 

class BaseDeDatos:
    def __init__(self):
        try:
            self.conexion=psycopg2.connect(
                "host='localhost' port='5432' dbname='Inversiones' user=postgres password=sergiosx12330")
            self.conexion.autocommit = True
            self.cursor = self.conexion.cursor()
        except:
            print("No se pudo conectar a la base de datos")
    

    
