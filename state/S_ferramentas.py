from abc import ABC, abstractmethod

class Ferramenta(ABC):
    
    @abstractmethod
    def mouse_ini(self, event):
        pass

    @abstractmethod
    def mouse_movimentacao(self, event):
        pass

    @abstractmethod
    def fim_mouse(self, event):
        pass