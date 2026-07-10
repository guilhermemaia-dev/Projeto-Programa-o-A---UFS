from model.figuras import Figuras

class Retangulo(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor_borda, self.cor_preenchimento)
    
    def validar(self):
        return abs(self.posx - self.ini_x) >= 2 and abs(self.posy - self.ini_y) >= 2
