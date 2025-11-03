import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra(self):
        lista_auto = self._model.get_automobili()
        list_view = ft.ListView()
        for item in lista_auto:
            list_view.controls.append(ft.Text(f"{item.marca} {item.modello} {item.anno} {item.posti}"))
        self._view.update()

    def cerca(self):
        lista_auto_modello = self._model.cerca_automobili_per_modello(modello=self._model.nome)
        list_view_modello = ft.ListView()
        for items in lista_auto_modello:
            list_view_modello.controls.append(ft.Text(f"{items.marca} {items.modello}"))
        self._view.update()

