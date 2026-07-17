from model.figuras import Figuras
from funcoes_extras.distancia import distancia

class Reta(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = cor

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor)
        
    def validar(self):
        return abs(self.posx - self.ini_x) > 0 or abs(self.posy - self.ini_y) > 0
    
    # (px, py) está perto (<=epsilon) de self
    def contem(self, px, py) :
        epsilon = 3
        return distancia(self.ini_x, self.ini_y, self.posx, self.posy, px, py) <= epsilon
    
    #deslocamento (somando a variação)
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor = cor_borda
        