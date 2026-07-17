from model.figuras import Figuras

class Quadrado(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
        self.atualizar_quadrado(posx, posy)

    #quando o objeto é criado já nasce esse metodo com as posicoes iniciais e atualiza o quadrado toda vez que movimenta o mouse
    def atualizar_quadrado(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.tamanho = max(abs(self.posx - self.ini_x), abs(self.posy - self.ini_y))
        self.x_quadrado = self.ini_x + (self.tamanho if (self.posx - self.ini_x) >= 0 else -self.tamanho)
        self.y_quadrado = self.ini_y + (self.tamanho if (self.posy - self.ini_y) >= 0 else -self.tamanho)

    def pegar_dados(self):
        return (self.ini_x, self.ini_y, self.x_quadrado, self.y_quadrado, self.cor_borda, self.cor_preenchimento)
    
    def validar(self):
        return abs(self.ini_x - self.posx) >= 2 and abs(self.ini_y - self.posy) >= 2
    
    # verificar se o clique ocorreu dentro do quadrado, encontrando a largura e altura, ou seja, retornará True se tiver dentro dos limites do quadrado
    def contem(self, x, y):
        return min(self.ini_x, self.x_quadrado) <= x <= max(self.x_quadrado,self.ini_x) and min(self.ini_y,self.y_quadrado) <= y <= max(self.y_quadrado,self.ini_y)

    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.posx += dx
        self.posy += dy
        self.x_quadrado += dx
        self.y_quadrado += dy

    def trocarcor(self,cor_borda,cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
