from controller.state.S_ferramentas import Ferramenta
from model.mao_livre import Mao_Livre

class S_Mao_Livre(Ferramenta):    
    preview : Mao_Livre = None

    #cria a figura no momento do clique
    def mouse_ini(self, event):
        self.ini_x = event.x
        self.ini_y = event.y

        self.preview = Mao_Livre(self.ini_x, self.ini_y, event.x, event.y, self.model.cor_selecionada_borda)

    #enquanto o mouse movimenta, se houver uma figura criada (ou seja, de houver um preview), ele adiciona os pontos na lista dos pontos.
    def mouse_movimentacao(self, event):
        if self.preview is None:
            return

        self.preview.adicionar_ponto(event.x, event.y)

        # a cada evento de mouse movimentado, vai desenhando tudo que ja está salvo e a própria mão livre
        self.view.desenhar_figuras(self.model.figuras)
        self.view.desenhar_mao_livre(self.preview, dash=(4,2))

    # se existir uma figura e a figura for válida, adiciona na lista, limpa o preview e redesenha a tela toda com a nova figura salva
    def fim_mouse(self, event):
        if self.preview is not None:
            if self.preview.validar():
                self.model.adcionar_figura(self.preview)

            self.preview = None

        self.view.desenhar_figuras(self.model.figuras)