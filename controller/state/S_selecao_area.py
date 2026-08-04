from controller.state.S_ferramentas import Ferramenta
from model.retangulo import Retangulo

class S_SelecaoArea(Ferramenta):
    preview = None
    arrastando_todas = False
    ultimo_x = ultimo_y = 0
    estado_foi_salvo = False

    def mouse_ini(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y
        self.estado_foi_salvo = False

        # verifica se clicou em uma figura que já faz parte da seleção
        selecionadas = self.model.obter_selecionadas()
        clique_na_selecionada = any(fig.contem(event.x, event.y) for fig in selecionadas)

        # se clicou em alguma figura do grupo vai arrastar todas
        if clique_na_selecionada:
            self.arrastando_todas = True

        # se clicou no vazio, limpa tudo e recomeça a desenhar
        else:
            self.arrastando_todas = False
            self.model.limpa_selecao()
            self.ini_x = event.x 
            self.ini_y = event.y
            self.preview = Retangulo(self.ini_x, self.ini_y, event.x, event.y, "#000000", "")

    def mouse_movimentacao(self, event):
        # se tiver arrastando, move todas as figuras selecionadas
        if self.arrastando_todas:

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

        else:
            if self.preview is None:
                return

            self.preview.posx = event.x
            self.preview.posy = event.y

            self.view.desenhar_figuras(self.model.figuras)
            self.view.desenhar_retangulo(self.preview, dash=(4, 2))

    def fim_mouse(self, event):
        if self.arrastando_todas:
            self.arrastando_todas = False
        else:
            if self.preview is not None:
                #envia as coordenadas para o model interface selecionar tudo que está dentro
                self.model.selecionar_por_area(self.ini_x, self.ini_y, event.x, event.y)
                self.preview = None

        selecionadas = self.model.obter_selecionadas()
        self.view.desenhar_figuras(self.model.figuras, selecionadas)