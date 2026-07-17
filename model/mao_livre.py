from funcoes_extras.poli_pontos import PoliPontos
from funcoes_extras.distancia import distancia

class Mao_Livre(PoliPontos):
    def __init__(self, ini_x, ini_y, posx, posy, cor):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = cor
        self.pontos = [(ini_x, ini_y), (posx, posy)]

    def adicionar_ponto(self, x, y):
        self.pontos.append((x,y))
        self.posx = x
        self.posy = y

    def pegar_dados(self):
        return (self.pontos, self.cor)

    def validar(self):
        return len(self.pontos) > 2
    
    def contem(self, px, py) :
        epsilon = 3
        return any(distancia(ini_x, ini_y, posx, posy, px, py) <= epsilon
                    for (ini_x, ini_y), (posx, posy) in zip(self.pontos, self.pontos[1:])
                  )
    
    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor = cor_borda