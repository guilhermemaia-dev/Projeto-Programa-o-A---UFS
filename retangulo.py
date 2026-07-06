from figuras import Figuras
from tkinter import *

#CRIA O RETANGULO
class Retangulo(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy,cor_borda,cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    def desenhar(self, canvas):
        canvas.create_rectangle(self.ini_x,self.ini_y,self.posx,self.posy,outline = self.cor_borda, fill = self.cor_preenchimento)

    # metodo para validar se a figura é uma reta ou não
    def validar(self):
        largura = abs(self.posx - self.ini_x)
        altura = abs(self.posy - self.ini_y)

        return largura >= 2 and altura >= 2
