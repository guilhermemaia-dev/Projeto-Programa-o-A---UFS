from figuras import Figuras
from tkinter import *
class Mao_Livre(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas):
        if self.cor_preenchimento == "":
            self.cor_preenchimento = "black"
            canvas.create_line(self.ini_x, self.ini_y, self.posx, self.posy, fill=self.cor_preenchimento)
        else:
            canvas.create_line(self.ini_x, self.ini_y, self.posx, self.posy, fill=self.cor_preenchimento)

