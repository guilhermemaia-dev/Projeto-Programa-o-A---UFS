from state.S_ferramentas import Ferramenta
from model.oval import Oval

class S_Oval(Ferramenta):
    def criar_figura(self, x, y):
        return Oval(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)
    
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

        figura = self.criar_figura(self.x2, self.y2)
        
        if not figura.validar():
            self.view.desenhar_figuras(self.model.figuras)
            return

        self.model.figuras.append(figura)
        self.view.desenhar_figuras(self.model.figuras)