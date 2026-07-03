from figuras import Figuras
from tkinter import *

#CRIA O OVAL
class Oval(Figuras):
    def __init__(self, ini_x, ini_y, pre_x,pre_y,cor_preenchimento,cor_borda):
        super().__init__(ini_x, ini_y, pre_x,pre_y) #USA AS COORDENADAS SALVAS
        self.cor_preenchimento = cor_preenchimento
        self.cor_borda = cor_borda

    def desenhar(self, canvas):
        canvas.create_oval(self.ini_x, self.ini_y, self.posx, self.posy,fill=self.cor_preenchimento, outline=self.cor_borda)

