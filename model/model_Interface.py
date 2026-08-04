import copy

class ModelInterface:
    def __init__(self):
        self.lista_cores = ["#00a8ff", "#c01414", "#10eb09", "#000000", "#ffffff", "#d9ff00", "#a200ff", "#ff5e00", "#858585", ""]
        self.cor_selecionada_borda = "#000000"
        self.cor_selecionada_preenchimento = ''
        self.ferramenta_atual = "Mao_Livre"
        self.state_atual = None
        self.espessura = 0

        self.figuras = []
        self.indices_selecionados = []
        self.historico_undo = []
        self.historico_redo = []
        self.buffer = []


    def limpa_selecao(self) :
        self.indices_selecionados.clear()

    def selecionar_por_area(self, x1, y1, x2, y2):
        sel_x1, sel_x2 = min(x1, x2), max(x1, x2)
        sel_y1, sel_y2 = min(y1, y2), max(y1, y2)

        self.indices_selecionados = []

        for index, fig in enumerate(self.figuras):
            if fig.esta_dentro(sel_x1, sel_y1, sel_x2, sel_y2):
                self.indices_selecionados.append(index)


    def mover_selecionadas(self, dx, dy):
        for i in self.indices_selecionados:
            self.figuras[i].mover(dx, dy)


    def seleciona(self, px, py):
        self.indices_selecionados = []

        for i in reversed(range(len(self.figuras))):
            if self.figuras[i].contem(px, py):
                self.indices_selecionados = [i]
                return


    def obter_selecionadas(self):
        return [self.figuras[i] for i in self.indices_selecionados if i < len(self.figuras)]


    def salvar_estado(self):
        copia_identica = copy.deepcopy(self.figuras)
        self.historico_undo.append(copia_identica)
        self.historico_redo.clear()
        
        
    # Copiar/Colar
    def copiar_selecionada(self) :
        self.buffer = copy.deepcopy(self.obter_selecionadas())

    def colar(self) :
        if self.buffer:
            self.salvar_estado()
            novas_figuras = copy.deepcopy(self.buffer)
            self.limpa_selecao()

            for f in novas_figuras:
                f.mover(10, 10)
                self.figuras.append(f)
                self.indices_selecionados.append(len(self.figuras)-1)

            self.buffer = copy.deepcopy(novas_figuras)


    def adcionar_figura(self, figura):
        self.salvar_estado()
        self.figuras.append(figura)



    def desfazer(self):
        if self.historico_undo:
            self.historico_redo.append(copy.deepcopy(self.figuras))
            self.figuras = self.historico_undo.pop()
            self.limpa_selecao()


    def refazer(self):
        if self.historico_redo:
            self.historico_undo.append(copy.deepcopy(self.figuras))
            self.figuras = self.historico_redo.pop()
            self.limpa_selecao()


    #criação dos métodos de camadas e manipulação da lista

    def trazer_frente(self):
        if not self.indices_selecionados:
            return
        
        self.salvar_estado()
        selecionadas = self.obter_selecionadas()

        for index in sorted(self.indices_selecionados, reverse=True):
            self.figuras.pop(index)

        self.figuras.extend(selecionadas)
        self.indices_selecionados = list(range(len(self.figuras) - len(selecionadas), len(self.figuras)))

    def trazer_tras(self):
        if not self.indices_selecionados:
            return

        self.salvar_estado()
        selecionadas = self.obter_selecionadas()

        for index in sorted(self.indices_selecionados, reverse=True):
            self.figuras.pop(index)

        self.figuras = selecionadas + self.figuras
        self.indices_selecionados = list(range(len(selecionadas)))

    #Mover somente uma camada#
    def uma_frente(self):
        if len(self.indices_selecionados) == 1:
            index = self.indices_selecionados[0]
            if index < len(self.figuras) - 1:
                self.salvar_estado()
                self.figuras[index], self.figuras[index + 1] = self.figuras[index + 1], self.figuras[index]
                self.indices_selecionados = [index + 1]

    def uma_atras(self):
        if len(self.indices_selecionados) == 1:
            index = self.indices_selecionados[0]
            if index > 0:
                self.salvar_estado()
                self.figuras[index], self.figuras[index - 1] = self.figuras[index - 1], self.figuras[index]
                self.indices_selecionados = [index - 1]
            

    def deletar_lista(self):
        if self.indices_selecionados:
            self.salvar_estado()
            for index in sorted(self.indices_selecionados, reverse=True):
                self.figuras.pop(index)
            self.limpa_selecao()

    # salva as alterações e limpa a tela inteira quando clica no botão limpar (chama o controller e o controller chama esse método)
    def limpar_tudo(self):
        self.salvar_estado()
        self.figuras = []
        self.limpa_selecao()


    def alterar_espessura(self, valor):
        self.espessura = valor