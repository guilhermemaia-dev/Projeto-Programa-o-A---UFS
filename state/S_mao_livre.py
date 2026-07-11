from state.S_ferramentas import Ferramenta
from model.mao_livre import Mao_Livre

class S_Mao_Livre(Ferramenta):
    def criar_figura(self, x, y):
        return Mao_Livre(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda)

    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)

        if preview.validar():
            self.model.figuras.append(preview)

            self.ini_x = event.x
            self.ini_y = event.y

        self.view.desenhar_figuras(self.model.figuras)

    def fim_mouse(self, event):
        self.view.desenhar_figuras(self.model.figuras)