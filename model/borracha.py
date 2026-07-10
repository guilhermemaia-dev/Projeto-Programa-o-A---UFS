from model.figuras import Figuras

class Borracha(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy,cor):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = "white"
        self.tamanho = 20

    def validar(self):
        return (self.posx - self.ini_x)**2 > 0 or (self.posy - self.ini_y)**2 > 0