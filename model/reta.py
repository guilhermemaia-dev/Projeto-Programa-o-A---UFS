from model.figuras import Figuras

class Reta(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = cor

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor)
        
    def validar(self):
        return abs(self.posx - self.ini_x) > 0 or abs(self.posy - self.ini_y) > 0