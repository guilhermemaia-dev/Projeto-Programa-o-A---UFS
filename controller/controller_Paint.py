from controller.state.S_mao_livre import S_Mao_Livre
from controller.state.S_reta import S_Reta
from controller.state.S_retangulo import S_Retangulo
from controller.state.S_oval import S_Oval
from controller.state.S_circulo import S_Circulo
from controller.state.S_quadrado import S_Quadrado
from controller.state.S_selecao import S_Selecao
from controller.state.S_selecao_area import S_SelecaoArea
from controller.state.S_pincel import S_Pincel
from model.arquivo import Arquivo

class ControllerPaint:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.states = {"Mao_Livre": S_Mao_Livre, 
                       "Reta": S_Reta, 
                       "Retangulo":S_Retangulo, 
                       "Oval": S_Oval, 
                       "Circulo": S_Circulo, 
                       "Quadrado": S_Quadrado, 
                       "Seleção": S_Selecao, 
                       "Selecao_Area": S_SelecaoArea,
                       "Pincel": S_Pincel}

        self.gerenciador_arquivo = Arquivo(self.model)
        self.model.alterar_espessura(5)
        self.view.iniciar(self)
        self.selecionar_ferramenta("Mao_Livre")

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

        self.view.alterar_cor_preview(self.obter_cor_borda(), self.obter_cor_preenchimento())
        
        selecionadas = self.model.obter_selecionadas()
        if selecionadas is not None:
            self.model.salvar_estado()
            for figura in selecionadas:
                figura.trocarcor(self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)

            self.view.desenhar_figuras(self.model.figuras, selecionadas)


    # receber a ferramenta de forma mais simplificada quando clica no botão, cria logo a figura e manda para a view atualizar a tela de preview
    def selecionar_ferramenta(self, ferramenta):
        atual = self.states.get(ferramenta)
        self.model.ferramenta_atual = ferramenta
        self.model.state_atual = atual(self.model, self.view)
        self.view.alterar_ferramenta_preview(ferramenta)

    def mouse_ini(self, event):
        self.model.state_atual.mouse_ini(event)

    def mouse_movimentacao(self, event):
        self.view.atualizar_label_posicao(event.x, event.y)
        self.model.state_atual.mouse_movimentacao(event)

    def fim_mouse(self, event):
        self.model.state_atual.fim_mouse(event)

    def rastrear_mouse(self, event):
            self.view.atualizar_label_posicao(event.x, event.y)
    
    def mouse_saiu(self, event=None):
        self.view.atualizar_label_posicao(None, None)



    #criação do botão para limpar a tela esvaziando a lista de figuras
    def limpar_tela(self):
        self.model.limpar_tudo()
        self.view.desenhar_figuras(self.model.figuras)


    # copiar e colar (recebe o evento do view e manda o model fazer)
    def control_c(self, event):
        self.model.copiar_selecionada()

    def control_v(self, event):
        self.model.colar()
        self.view.desenhar_figuras(self.model.figuras)# redesenha com a parte do buffer
    

    #criação do metodo ctrl z para remover a ultima figura
    def ctrl_z(self,event=None):    
        self.model.desfazer()
        self.view.desenhar_figuras(self.model.figuras)
    
    #Criação do metodo ctrl y para readcionar a figura removida
    def ctrl_y(self,event=None):
        self.model.refazer()
        self.view.desenhar_figuras(self.model.figuras)

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
        #método necessário para todos os seguintes para aplicar imediatamente a alteração#
        self.view.desenhar_figuras(self.model.figuras)
    def camada_traseira(self, event=None):
        self.model.trazer_tras()
        self.view.desenhar_figuras(self.model.figuras)
    
    #Método de remover#
    def remover(self, event=None):
        self.model.deletar_lista()
        self.view.desenhar_figuras(self.model.figuras)
    
    #Movimentos de 1 camada#
    def mover_uma_frente(self, event=None):
        self.model.uma_frente()
        self.view.desenhar_figuras(self.model.figuras)

    def mover_uma_atras(self, event=None):
        self.model.uma_atras()
        self.view.desenhar_figuras(self.model.figuras)

    def atualizar_espessura(self, valor):
        valor_inteiro = int(float(valor))
        self.model.alterar_espessura(valor_inteiro)
        self.view.header.atualizar_label_espessura(valor_inteiro)

    def obter_cor_borda(self):
        return self.model.cor_selecionada_borda

    def obter_cor_preenchimento(self):
        return self.model.cor_selecionada_preenchimento

    def obter_espessura_atual(self):
        return self.model.espessura

    def obter_ferramenta_atual(self):
        return self.model.ferramenta_atual