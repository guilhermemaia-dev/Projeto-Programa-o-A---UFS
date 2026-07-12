from model.figuras import Figuras

class Borracha(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = "white"
        self.tamanho = 20

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor, self.tamanho)

    def validar(self):
        return (self.posx - self.ini_x)**2 > 0 or (self.posy - self.ini_y)**2 > 0