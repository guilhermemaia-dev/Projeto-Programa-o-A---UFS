from state.S_mao_livre import S_Mao_Livre
from state.S_reta import S_Reta
from state.S_retangulo import S_Retangulo
from state.S_oval import S_Oval
from state.S_circulo import S_Circulo
from state.S_borracha import S_Borracha
from state.S_quadrado import S_Quadrado
from state.S_selecao import S_Selecao
from model.arquivo import Arquivo

class ControllerPaint:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

        self.states = {"Mao_Livre": S_Mao_Livre, "Reta": S_Reta, "Retangulo":S_Retangulo, "Oval": S_Oval, "Circulo": S_Circulo, "Borracha": S_Borracha, "Quadrado": S_Quadrado, "Seleção": S_Selecao}

        self.view.criar_elementos()
        self.selecionar_ferramenta("Mao_Livre")
        #Atualização da etapa 4
        self.gerenciador_arquivo = Arquivo(self.model)

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


    # receber a ferramenta de forma mais simplificada quando clica no botão, cria logo a figura e manda para a view atualizar a tela de preview
    def selecionar_ferramenta(self, ferramenta):
        atual = self.states.get(ferramenta)
        self.model.ferramenta_atual = ferramenta
        self.model.state_atual = atual(self.model, self.view)
        self.view.alterar_ferramenta_preview(ferramenta)

    def mouse_ini(self, event):
        self.model.state_atual.mouse_ini(event)

    def mouse_movimentacao(self, event):
        self.model.state_atual.mouse_movimentacao(event)

    def fim_mouse(self, event):
        self.model.state_atual.fim_mouse(event)



    #criação do botão para limpar a tela esvaziando a lista de figuras
    def limpar_tela(self):
        self.model.figuras = []
        self.view.desenhar_figuras(self.model.figuras)


    # copiar e colar (recebe o evento do view e manda o model fazer)
    def control_c(self, event):
        self.model.copiar_selecionada()

    def control_v(self, event):
        self.model.colar()
        self.view.desenhar_figuras(self.model.figuras)# redesenha com a parte do buffer
    

    #criação do metodo crtl_z para remover a ultima figura
    def ctrl_z(self,event):
        if self.model.figuras:
            self.model.figuras.pop()
            self.view.desenhar_figuras(self.model.figuras)
    
    #Ctrl Y:
    

    #Funções de salvar e abrir arquivos#
    def salvar_desenho(self):
        #Pede o caminho para o View#
        caminho = self.view.pedir_caminho_salvar()
        
        #Se o usuário escolheu um caminho, salva#
        if caminho: 
            self.gerenciador_arquivo.salvar_para_arquivo(caminho)

    def abrir_desenho(self):
        #Faz o mesmo do de salvar_desenho
        caminho = self.view.pedir_caminho_abrir()
        
        if caminho:
            #Manda o Model carregar os dados#
            self.gerenciador_arquivo.carregar_de_arquivo(caminho)
            
            #Pede para a View desenhar a nova lista de figuras#
            self.view.desenhar_figuras(self.model.figuras)
    #Métodos de camadas, precisa do event=None para não dar erro# 
    def camada_frontal(self, event=None):
        self.model.trazer_frente()
        
    def camada_traseira(self, event=None):
        self.model.trazer_tras()
    
    #Método de remover#
    def remover(self, event=None):
        self.model.deletar_lista()
        
    #Movimentos laterais#
    def mover_esquerda(self, event=None):
        figSel = self.model.selecionada()
        if figSel:
            figSel.mover(-15, 0)

    def mover_direita(self, event=None):
        figSel = self.model.selecionada()
        if figSel:
            figSel.mover(+15, 0)