from state.S_ferramentas import Ferramenta
from model.retangulo import Retangulo

class S_Retangulo(Ferramenta):
    preview : Retangulo =None

    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

        self.preview = Retangulo(self.ini_x, self.ini_y, event.x, event.y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)

    def mouse_movimentacao(self, event):
        self.preview.posx = event.x
        self.preview.posy = event.y

        # a cada evento de mouse movimentado, vai desenhando tudo que ja está salvo
        self.view.desenhar_figuras(self.model.figuras)

        self.view.desenhar_retangulo(self.preview, dash=(4,2))

    # se a figura for válida, adiciona na lista, limpa o preview e redesenha a tela toda com a nova figura salva
    def fim_mouse(self, event):
        if self.preview.validar():
            self.model.figuras.append(self.preview)

        self.preview = None
        self.view.desenhar_figuras(self.model.figuras)
