from abc import ABC, abstractmethod
#classe figuras que vai inicializar cada ferramenta e verificar se ela será ou não desenhada#
class Figuras(ABC):
    def __init__(self,ini_x,ini_y,posx,posy):
        self.ini_x = ini_x
        self.ini_y = ini_y
        self.posx = posx
        self.posy = posy
    @abstractmethod
    def validar(self):
        pass

