from funcoes_extras.poli_pontos import PoliPontos
from funcoes_extras.distancia import distancia

class Pincel(PoliPontos):
    def __init__(self, ini_x, ini_y, posx, posy, cor, espessura=6):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor = cor
        self.pontos = [(ini_x, ini_y), (posx, posy)]
        self.espessura = espessura

    def adicionar_ponto(self, x, y):
        self.pontos.append((x,y))
        self.posx = x
        self.posy = y

    def pegar_dados(self):
        return (self.pontos, self.cor, self.espessura)

    def validar(self):
        return len(self.pontos) > 2
    
    def contem(self, px, py) :
        epsilon = 3
        return any(distancia(ini_x, ini_y, posx, posy, px, py) <= epsilon
                    for (ini_x, ini_y), (posx, posy) in zip(self.pontos, self.pontos[1:])
                  )
    
    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor = cor_borda

    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy

        novos_pontos = []
        for x, y in self.pontos:
            novos_pontos.append((x + dx, y + dy))

        self.pontos = novos_pontos

    def esta_dentro(self, x1, y1, x2, y2):
        sel_x1, sel_x2 = min(x1, x2), max(x1, x2)
        sel_y1, sel_y2 = min(y1, y2), max(y1, y2)

        return any(sel_x1 <= x <= sel_x2 and sel_y1 <= y <= sel_y2 for x, y in self.pontos)