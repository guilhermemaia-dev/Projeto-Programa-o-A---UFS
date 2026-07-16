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


    def limpa_selecao(self) :
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
    