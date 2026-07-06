from tkinter import *
from abc import ABC, abstractmethod
#Criação da classe pai (molde) denominada Figuras 
class Figuras(ABC):
    def __init__(self, ini_x, ini_y, posx, posy):
        self.ini_x = ini_x
        self.ini_y = ini_y
        self.posx = posx
        self.posy = posy


#Cria o método abstrato desenhar, que as classes filhas terão que completar
    @abstractmethod
    def desenhar(self, canvas):
        pass

    @abstractmethod
    def validar(self):
        pass

