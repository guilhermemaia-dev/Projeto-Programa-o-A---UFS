from state.S_ferramentas import Ferramenta
from model.quadrado import Quadrado

class S_Quadrado(Ferramenta):
    preview : Quadrado = None
    
    # cria a figura no momento do clique
    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

        self.preview = Quadrado(self.ini_x, self.ini_y, event.x, event.y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)

    # enquanto o mouse se movimenta, vai atualizando o quadrado
    def mouse_movimentacao(self, event):
        if self.preview is None:
            return

        self.preview.atualizar_quadrado(event.x, event.y)

        # a cada evento de mouse movimentado, vai desenhando tudo que ja está salvo
        self.view.desenhar_figuras(self.model.figuras)
        self.view.desenhar_quadrado(self.preview, dash=(4,2))

    # se a figura for válida, adiciona na lista limpa o preview e redesenha a tela toda com a nova figura salva
    def fim_mouse(self, event):
        if self.preview is not None:
            if self.preview.validar():
                self.model.adcionar_figura(self.preview)

            self.preview = None

        self.view.desenhar_figuras(self.model.figuras)