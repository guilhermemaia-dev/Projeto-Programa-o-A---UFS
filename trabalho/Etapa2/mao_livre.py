from figuras import Figuras
from tkinter import *
class Mao_Livre(Figuras):
    def desenhar(self, canvas):
        canvas.create_line(self.ini_x, self.ini_y, self.posx, self.posy)

