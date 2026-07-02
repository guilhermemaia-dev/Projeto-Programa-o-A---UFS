from figura import Figuras
from tkinter import *

#CRIA O CIRCULO
class Circulo(Figuras):
    def __init__(self, ini_x, ini_y,raio,cor_borda,cor_preenchimento):
        super().__init__(ini_x, ini_y,ini_x,ini_y) #USA AS COORDENADAS SALVAS
          
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.raio = raio
    def desenhar(self, canvas): 
        canvas.create_oval(self.ini_x-self.raio, self.ini_y-self.raio, self.ini_x+self.raio, self.ini_y+self.raio, outline=self.cor_borda, fill=self.cor_preenchimento)

    