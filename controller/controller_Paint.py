from state.S_mao_livre import S_Mao_Livre
from state.S_reta import S_Reta
from state.S_retangulo import S_Retangulo
from state.S_oval import S_Oval
from state.S_circulo import S_Circulo
from state.S_borracha import S_Borracha
from state.S_quadrado import S_Quadrado


class ControllerPaint:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

        self.states = {"Mao_Livre": S_Mao_Livre, "Reta": S_Reta, "Retangulo":S_Retangulo, "Oval": S_Oval, "Circulo": S_Circulo, "Borracha": S_Borracha, "Quadrado": S_Quadrado}

        self.view.criar_elementos()
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


# sera deletado dps, apenas como BASE para criar 
'''
#Criação dos eventos de mouse#
    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

    # metodo que capta as coordenadas enquanto movimenta o mouse e continua criando a figura (fazendo o preview)
    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)
        
        # se for mao_livre ou borracha então vai adicionando na hora do movimento todos os previews e desenhando a figura, ou seja, desenhando o preview

        if self.model.ferramenta_atual in ["Mao_Livre","Borracha"]:
            self.model.figuras.append(preview)
            self.ini_x = event.x
            self.ini_y = event.y
            self.view.desenhar_figuras(self.model.figuras)
        else:
            #desenha todas as figuras ja feitas
            self.view.desenhar_figuras(self.model.figuras)
            #recebe todos os previews ja feitos para serem desenhados
            self.view.desenhar_figuras([preview], apagarAtela=False)
    


    #quando solta o mouse pega as coordenadas finais (x2,y2) e cria a figura final com essas coordenadas
    def fim_mouse(self, event):
        #verifica se a figura é valida ou não (cada figura sabe se ela mesmo é valida ou se não é)
        # se não for válida, ela não se desenha, caso contrário, leva até o model e adiciona na lista das figuras e desenha
        self.x2 = event.x
        self.y2 = event.y

        figura = self.criar_figura(event.x, event.y)
        
        if not figura.validar():
            self.view.desenhar_figuras(self.model.figuras)
            return

        self.model.figuras.append(figura)
        self.view.desenhar_figuras(self.model.figuras)
'''

# será deletado tbm dps
# parte para ser a base de criar o state das outras figuras como a borracha e os demais que faltam
'''
    # os parâmetros x,y dependem do que for, por exemplo, se for o mouse_movimentacao (preview) que chama o metodo, então será passado x1,y1, caso for fim_mouse será passado x2,y2
    def criar_figura(self, x, y):
        classe_da_figura = self.ferramentas.get(self.model.ferramenta_atual)
        
        if self.model.ferramenta_atual in ["Mao_Livre", "Reta"]:
            return classe_da_figura(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda)
        elif self.model.ferramenta_atual == "Borracha":
            return classe_da_figura(self.ini_x,self.ini_y,x,y)
        else:
            return classe_da_figura(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)
        
'''