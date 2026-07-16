import copy

class ModelInterface:
    def __init__(self):
        self.lista_cores = ["#00a8ff", "#c01414", "#10eb09", "#000000", "#ffffff", "#d9ff00", "#a200ff", "#ff5e00", "#858585", "#E7E7E7"]
        self.cor_selecionada_borda = "#000000"
        self.cor_selecionada_preenchimento = ''
        self.ferramenta_atual = "Mao_Livre"
        self.state_atual = None
        self.figuras = []
        self.indice_selecionado = -1
        self.buffer = None


    def limpa_selecao(self) :#|
        self.indice_selecionado = -1

    def seleciona(self, px, py) :
        i = len(self.figuras)-1
        while i >= 0 and not self.figuras[i].contem(px, py) :
            i -= 1
        self.indice_selecionado = i

    def selecionada(self) :
        if self.indice_selecionado >= 0 :
            return self.figuras[self.indice_selecionado]
        else :
            return None
        
        
    # Copiar/Colar
    def copiar_selecionada(self) :
        self.buffer = copy.deepcopy(self.selecionada())

    def colar(self) :
        if self.buffer != None :
            f = self.buffer
            f.mover(5, 5)
            self.figuras.append(f)
            self.buffer = copy.deepcopy(f)
    #criação dos métodos de camadas e manipulação da lista#
    #o programa desenha as figuras e suas camadas baseado na sua posição na lista de figuras#
    
    def trazer_frente(self):
        figSel = self.selecionada()
        if figSel:
            #Colocando a figura como último termo#
            self.figuras.remove(figSel)
            self.figuras.append(figSel)
            #Atualizando o índice para a última posição e mantém selecionada a figura#
            self.indice_selecionado = len(self.figuras) - 1
    def trazer_tras(self):
        figSel = self.selecionada()
        if figSel:
            self.figuras.remove(figSel)
            #Coloca a figura no último termo e atualiza o índice e mantém selecionada a figura#
            self.figuras.insert(0, figSel)
            self.indice_selecionado = 0

    #Métodos de deletar e mover com atalhos do teclado#
    def deletar_lista(self):
        figSel = self.selecionada()
        if figSel:
            self.figuras.remove(figSel)
