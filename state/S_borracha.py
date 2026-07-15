from state.S_ferramentas import Ferramenta
from model.borracha import Borracha

class S_Borracha(Ferramenta):
    preview : Borracha = None

    def mouse_ini(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

        self.preview = Borracha(self.ini_x, self.ini_y, event.x, event.y)

    def mouse_movimentacao(self, event):
        self.preview.adicionar_ponto(event.x, event.y)

        self.view.desenhar_figuras(self.model.figuras)

        self.view.desenhar_borracha(self.preview)

    def fim_mouse(self, event):
        if self.preview.validar():
            self.model.figuras.append(self.preview)

        self.preview = None
        self.view.desenhar_figuras(self.model.figuras)