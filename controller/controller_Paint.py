class ControllerPaint:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.controller = self
        self.view.criar_elementos()

    #buscar a lista de cores no model para mandar futuramente para o view
    def obter_cor(self):
        return self.model.lista_cores

    #recebe a cor clicada e faz a "tradução" dela, ou seja, o processamento da cor
    def receberAcor(self, cor_clicada, estado_marcador):
        if estado_marcador == 1: 
            self.model.cor_selecionada_preenchimento = cor_clicada
        else:
            if cor_clicada != "":
                self.model.cor_selecionada_borda = cor_clicada
            else:
                self.model.cor_selecionada_borda = "#000000"

        self.view.alterar_cor_preview(self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)


    #métodos que mandam para o model qual a ferramenta atual selecionada
    def selecionar_livre(self):
        self.model.ferramenta_atual = "Mao_Livre"
        self.view.alterar_ferramenta_preview(self.model.ferramenta_atual)

    def selecionar_reta(self):
        self.model.ferramenta_atual = "Reta"
        self.view.alterar_ferramenta_preview(self.model.ferramenta_atual)

    def selecionar_retangulo(self):
        self.model.ferramenta_atual = "Retangulo"
        self.view.alterar_ferramenta_preview(self.model.ferramenta_atual)

    def selecionar_oval(self):
        self.model.ferramenta_atual = "Oval"
        self.view.alterar_ferramenta_preview(self.model.ferramenta_atual)

    def selecionar_circulo(self):
        self.model.ferramenta_atual = "Circulo"
        self.view.alterar_ferramenta_preview(self.model.ferramenta_atual)

