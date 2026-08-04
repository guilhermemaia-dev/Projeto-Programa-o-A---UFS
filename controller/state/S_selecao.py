from controller.state.S_ferramentas import Ferramenta

class S_Selecao(Ferramenta):
    ultimo_x : int = 0
    ultimo_y : int = 0
    estado_foi_salvo = False

    # no momento do clique do mouse ele guarda as posições, recebe as selecionadas, verifica se houve clique na selecionada e se houver, seleciona
    def mouse_ini(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y
        self.estado_foi_salvo = False

        selecionadas = self.model.obter_selecionadas()
        clique_na_selecionada = any(fig.contem(event.x, event.y) for fig in selecionadas)

        if not clique_na_selecionada:
            self.model.seleciona(event.x, event.y)


        selecionadas = self.model.obter_selecionadas()
        self.view.desenhar_figuras(self.model.figuras, selecionadas)


    # se houver uma figura selecionada calcula a diferença da posicao do mouse atual com o ultimo e move a diferença.
    def mouse_movimentacao(self, event):
        if len(self.model.indices_selecionados) > 0:

            if not self.estado_foi_salvo:
                self.model.salvar_estado()
                self.estado_foi_salvo = True

            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y

            self.model.mover_selecionadas(dx, dy)

            self.ultimo_x = event.x
            self.ultimo_y = event.y

            selecionadas = self.model.obter_selecionadas()
            self.view.desenhar_figuras(self.model.figuras, selecionadas)


    # quando solta o mouse redesenha a tela
    def fim_mouse(self, event):
        selecionadas = self.model.obter_selecionadas()
        self.view.desenhar_figuras(self.model.figuras, selecionadas)