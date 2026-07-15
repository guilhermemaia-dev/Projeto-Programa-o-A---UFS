from model.figuras import Figuras

class Mao_Livre(Figuras):
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
    
    def contem(self, x, y):
        lista_x = []
        lista_y = []
        for pontox, pontoy in self.pontos:
            lista_x.append(pontox)
            lista_y.append(pontoy)

        x_min = min(lista_x)
        y_min = min(lista_y)
        x_max = max(lista_x)
        y_max = max(lista_y)
        return x_min <= x <= x_max and y_min <= y <= y_max
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy
        pontos_movimentando = []
        for x, y in self.pontos:
            pontos_movimentando.append((x + dx, y + dy))
        self.pontos = pontos_movimentando
            
    def limites(self):
        lista_x = []
        lista_y = []
        for x, y in self.pontos:
            lista_x.append(x)
            lista_y.append(y)

        x_min = min(lista_x)
        y_min = min(lista_y)
        x_max = max(lista_x)
        y_max = max(lista_y)
        return (x_min, y_min, x_max, y_max)
