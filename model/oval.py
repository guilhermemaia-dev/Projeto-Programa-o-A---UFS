from model.figuras import Figuras

class Oval(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor_borda, self.cor_preenchimento)
    
    def validar(self):
        return abs(self.posx - self.ini_x) >= 2 and abs(self.posy - self.ini_y) >= 2
    
    def contem(self, x, y):
        centrox = (self.ini_x + self.posx)/2
        centroy = (self.ini_y + self.posy)/2
        horizontal = abs(self.posx-self.ini_x)/2
        vertical = abs(self.posy-self.ini_y)/2
        return ((x - centrox)**2 / horizontal**2) + ((y - centroy)**2 / vertical**2) <= 1
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        