from model.figuras import Figuras

class Reta(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = cor

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.posx, self.posy, self.cor)
        
    def validar(self):
        return abs(self.posx - self.ini_x) > 0 or abs(self.posy - self.ini_y) > 0
    
    def contem(self, x, y):
        return min(self.ini_x,self.posx) <= x <= max(self.posx,self.ini_x) and min(self.ini_y,self.posy) <= y <= max(self.posy,self.ini_y)
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

    def limites(self):
        x_min = min(self.ini_x, self.posx)
        y_min = min(self.ini_y, self.posy)
        x_max = max(self.ini_x, self.posx)
        y_max = max(self.ini_y, self.posy)
        return (x_min, y_min, x_max, y_max)