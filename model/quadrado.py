from model.figuras import Figuras

class Quadrado(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.tamanho = max(abs(self.posx - self.ini_x), abs(self.posy - self.ini_y))
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.x_quadrado = self.ini_x + (self.tamanho if (self.posx - self.ini_x) >= 0 else -tamanho)
        self.y_quadrado = self.ini_x + (self.tamanho if (self.posy - self.ini_y) >= 0 else -tamanho)

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.cor_borda, self.cor_preenchimento, self.tamanho, self.x_quadrado, self.y_quadrado)
    
    def validar(self):
        return abs(self.ini_x - self.posx) >= 2 and abs(self.ini_y - self.posy) >= 2
