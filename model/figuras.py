from abc import ABC, abstractmethod
#classe figuras que vai inicializar cada ferramenta e verificar se ela será ou não desenhada#
class Figuras(ABC):
    def __init__(self,ini_x,ini_y,posx,posy):
        self.ini_x = ini_x
        self.ini_y = ini_y
        self.posx = posx
        self.posy = posy
    
    #metodo para validar a figura antes de criar
    @abstractmethod
    def validar(self):
        pass

    # serve para retornar os dados das figuras
    @abstractmethod
    def pegar_dados(self):
        pass

    # serve para verificar se a figura contem os pontos, ou seja, se o ponto(x,y) está dentro do desenho
    @abstractmethod
    def contem(self, x, y):
        pass

    # verifica se a figura inteira está contida dentro da seleção
    def esta_dentro(self, sel_x1, sel_y1, sel_x2, sel_y2):
        fig_x1 = min(self.ini_x, self.posx)
        fig_y1 = min(self.ini_y, self.posy)
        fig_x2 = max(self.ini_x, self.posx)
        fig_y2 = max(self.ini_y, self.posy)

        return (fig_x1 >= sel_x1 and fig_y1 >= sel_y1 and fig_x2 <= sel_x2 and fig_y2 <= sel_y2)

    #serve para mover a figura
    @abstractmethod
    def mover(self, dx, dy):
        pass

    #serve para mudar cor da figura
    def trocarcor(self,cor_borda,cor_preenchimento):
        pass        

    def alterar_espessura(self, nova_espessura):
        self.espessura = nova_espessura