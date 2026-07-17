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
    
    # verificar se o clique ocorreu dentro do retangulo, encontrando a largura e altura, ou seja, retornará True se tiver dentro dos limites do retângulo
    def contem(self, x, y):
        x_min, x_max = min(self.ini_x, self.posx), max(self.ini_x, self.posx)
        y_min, y_max = min(self.ini_y, self.posy), max(self.ini_y, self.posy)
        return x_min <= x <= x_max and y_min <= y <= y_max

    # deslocamento (somando a variação)
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

