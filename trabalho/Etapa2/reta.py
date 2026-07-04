from figuras import Figuras
from tkinter import *
#Criação da Reta
class Reta(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_preenchimento):
        #herda o init da classe Figuras e adiciona o self.cor_preenchimento em seguida
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_preenchimento = cor_preenchimento
    def desenhar(self, canvas):
        canvas.create_line(self.ini_x, self.ini_y, self.posx, self.posy, fill=self.cor_preenchimento)

    # metodo para validar se a figura é ou não um ponto, ou seja, deu apenas um clique na tela
    def validar(self):
        largura = abs(self.posx - self.ini_x)
        altura = abs(self.posy - self.ini_y)

        return largura > 0 or altura > 0