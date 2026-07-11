from state.S_ferramentas import Ferramenta
from model.quadrado import Quadrado

class S_Quadrado(Ferramenta):
    def criar_figura(self, x, y):
        return Quadrado(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)
    
    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)

        self.view.desenhar_figuras(self.model.figuras)
        self.view.desenhar_figuras([preview], apagarAtela=False)

    def fim_mouse(self, event):
        self.x2 = event.x
        self.y2 = event.y

        figura = self.criar_figura(event.x, event.y)
        
        if not figura.validar():
            self.view.desenhar_figuras(self.model.figuras)
            return

        self.model.figuras.append(figura)
        self.view.desenhar_figuras(self.model.figuras)