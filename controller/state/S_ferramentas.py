from abc import ABC, abstractmethod

class Ferramenta(ABC):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.ini_x = 0
        self.ini_y = 0
    @abstractmethod
    def mouse_ini(self, event):
        pass

    @abstractmethod
    def mouse_movimentacao(self, event):
        pass

    @abstractmethod
    def fim_mouse(self, event):
        pass