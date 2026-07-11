from state.S_ferramentas import Ferramenta
from model.circulo import Circulo

class S_Circulo(Ferramenta):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.ini_x = 0
        self.ini_y = 0

    def criar_figura(self, x, y):
        return Circulo(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)
    
    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)

        #desenha todas as figuras ja feitas
        self.view.desenhar_figuras(self.model.figuras)
        #recebe o preview para ser desenhado
        self.view.desenhar_figuras([preview], apagarAtela=False)

    def fim_mouse(self, event):
        #verifica se a figura é valida ou não (cada figura sabe se ela mesmo é valida ou se não é)
        # se não for válida, ela não se desenha, caso contrário, leva até o model e adiciona na lista das figuras e desenha
        self.x2 = event.x
        self.y2 = event.y

        figura = self.criar_figura(event.x, event.y)
        
        if not figura.validar():
            self.view.desenhar_figuras(self.model.figuras)
            return

        self.model.figuras.append(figura)
        self.view.desenhar_figuras(self.model.figuras)