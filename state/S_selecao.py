from state.S_ferramentas import Ferramenta


class S_Selecao(Ferramenta):
    def mouse_ini(self, event):
        x = event.x
        y = event.y
        self.ultimo_x = x
        self.ultimo_y = y

        self.model.figura_selecionada = None

        for figura in self.model.figuras:
            if figura.contem(x , y):
                self.model.figura_selecionada = figura
                break
        
        if self.model.figura_selecionada is not None:
            self.view.desenhar_selecao(self.model.figura_selecionada)
    
    def mouse_movimentacao(self, event):
        if self.model.figura_selecionada is not None:
            dx = event.x - self.ultimo_x
            dy = event.y - self.ultimo_y
            self.ultimo_x = event.x
            self.ultimo_y = event.y

            self.model.figura_selecionada.mover(dx,dy)

            self.view.desenhar_figuras(self.model.figuras)

            self.view.desenhar_selecao(self.model.figura_selecionada)

    def fim_mouse(self, event):
        pass