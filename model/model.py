from msilib.schema import ListView
import flet as ft
import mysql.connector

from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        try :
            connection = get_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM automobile"
            cursor.execute(query)
            righe = cursor.fetchall()
            lista_auto = []
            for row in righe:
                auto = Automobile(codice=row["codice"],
                                        marca=row["marca"],
                                        modello=row["modello"],
                                        anno=row["anno"],
                                        posti=row["posti"],
                                        disponibile=row["disponibile"])
                lista_auto.append(auto)
            return lista_auto
        except mysql.connector.Error as err:
            print(err)
            return None
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query_modello = "SELECT * FROM automobile WHERE modello = '%s'"
            cursor.execute(query_modello, (modello,))
            righe = cursor.fetchall()
            lista_auto_modello = []
            for row in righe:
                automobili = Automobile(codice = row[0],
                                        marca = row[1],
                                        modello = row[2],
                                        anno = row[3],
                                        posti = row[4],
                                        disponibile=row[5])
                lista_auto_modello.append(automobili)
            return lista_auto_modello
        except mysql.connector.Error as err:
            print(err)
            return None
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

