from controller.state.S_ferramentas import Ferramenta

class S_Selecao(Ferramenta):
    ultimo_x : int = 0
    ultimo_y : int = 0

    # no momento do clique do mouse ele guarda as posições, limpa a seleção (por exemplo se já tiver algo selecionado e clicar em algo vazio ele limpará a seleção), seleciona a figura e desenha todas as figuras com a figura selecionada
    def mouse_ini(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y
        self.model.limpa_selecao()
        self.model.seleciona(event.x, event.y)

        figSel = self.model.selecionada()
        self.view.desenhar_figuras(self.model.figuras, figSel)

    # se houver uma figura selecionada calcula a diferença da posicao do mouse atual com o ultimo e move a diferença.
    def mouse_movimentacao(self, event):
        figSel = self.model.selecionada()
        if figSel:
            figSel.mover(event.x - self.ultimo_x, event.y - self.ultimo_y)
            #atualiza a posição atual do mouse, garantindo que a movimentação ocorra no ponto atual
            self.ultimo_x = event.x
            self.ultimo_y = event.y

            self.view.desenhar_figuras(self.model.figuras, figSel)

    # quando solta o mouse redesenha a tela
    def fim_mouse(self, event):
        figSel = self.model.selecionada()
        #garante que o dash continue, já que está com o argumento de figSel
        self.view.desenhar_figuras(self.model.figuras, figSel)