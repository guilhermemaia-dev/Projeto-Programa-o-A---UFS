from controller.state.S_ferramentas import Ferramenta
from model.pincel import Pincel

class S_Pincel(Ferramenta):    
    preview : Pincel = None

    #cria a figura no momento do clique
    def mouse_ini(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

        self.preview = Pincel(self.ini_x, self.ini_y, event.x, event.y, self.model.cor_selecionada_borda, self.model.espessura)

    #enquanto o mouse movimenta, se houver uma figura criada (ou seja, de houver um preview), ele adiciona os pontos na lista dos pontos.
    def mouse_movimentacao(self, event):
        if self.preview is None:
            return

        self.preview.adicionar_ponto(event.x, event.y)

        # a cada evento de mouse movimentado, vai desenhando tudo que ja está salvo e o próprio pincel
        self.view.desenhar_figuras(self.model.figuras)
        self.view.desenhar_pincel(self.preview)

    # se existir uma figura e a figura for válida, adiciona na lista, limpa o preview e redesenha a tela toda com a nova figura salva
    def fim_mouse(self, event):
        if self.preview is not None:
            if self.preview.validar():
                self.model.adcionar_figura(self.preview)

            self.preview = None

        self.view.desenhar_figuras(self.model.figuras)