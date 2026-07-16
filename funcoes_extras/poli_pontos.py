from model.figuras import Figuras
from abc import ABC, abstractmethod
from funcoes_extras.tres_pontos_alinhados import tres_pontos_alinhados

class PoliPontos(Figuras, ABC) :
    pontos: list

    # Adiciona ponto se não está alinhado com os dois anteriores
    # Se alinhado, elimina o anterior
    def adiciona_ponto(self, x, y) :
        if len(self.pontos) >= 2 and\
           tres_pontos_alinhados(self.pontos[-2], self.pontos[-1], (x, y)) :
            self.pontos[-1] = (x,y)
        else :
            self.pontos.append((x,y))

    def mover(self, dx, dy) :
        for i in range(len(self.pontos)) :
            (x, y) = self.pontos[i]
            self.pontos[i] = (x+dx, y+dy)