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
    
    def contem(self, x, y):
        raio = ((self.ini_x - self.posx) ** 2 + (self.ini_y - self.posy) ** 2) ** 0.5
        checar = ((x - self.ini_x)**2 + (y - self.ini_y)**2)**0.5
        return checar <= raio
        
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento  