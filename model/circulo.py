from model.figuras import Figuras

class Circulo(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy) 
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    
    def pegar_dados(self):
        self.raio = ((self.ini_x - self.posx) ** 2 + (self.ini_y - self.posy) ** 2) ** 0.5
        return (self.ini_x - self.raio, self.ini_y - self.raio, self.ini_x + self.raio, self.ini_y + self.raio, self.cor_borda, self.cor_preenchimento)

    def validar(self):
        raio = ((self.ini_x - self.posx) ** 2 + (self.ini_y - self.posy) ** 2) ** 0.5
        return raio >= 2
        
