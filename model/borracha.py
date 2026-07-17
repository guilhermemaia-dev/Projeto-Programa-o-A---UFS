from model.figuras import Figuras

class Borracha(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = "white"
        self.tamanho = 20
        self.pontos = [(ini_x, ini_y), (posx, posy)]

    def adicionar_ponto(self, x, y):
        self.pontos.append((x,y))
        self.posx = x
        self.posy = y

    def pegar_dados(self):
        return (self.pontos, self.cor, self.tamanho)

    def validar(self):
        return len(self.pontos) > 2
    
    def contem(self, x, y):
        pass
    
    def mover(self, dx, dy):
        pass

    def trocarcor(self, cor_borda, cor_preenchimento):
        pass
