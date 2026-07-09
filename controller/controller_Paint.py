from model.mao_livre import Mao_Livre
from model.reta import Reta
from model.retangulo import Retangulo
from model.oval import Oval
from model.circulo import Circulo


class ControllerPaint:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.ini_x = 0
        self.ini_y = 0
        self.view.controller = self
        self.view.criar_elementos()
        self.ferramentas = {"Mao_Livre": Mao_Livre, "Reta": Reta, "Retangulo":Retangulo, "Oval": Oval, "Circulo": Circulo}
        self.selecionar_livre()
        

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


#Criação dos eventos de mouse#
    def mouse_ini(self, event):
        self.ini_x = event.x 
        self.ini_y = event.y

    # metodo que capta as coordenadas enquanto movimenta o mouse e continua criando a figura (fazendo o preview)
    def mouse_movimentacao(self, event):
        self.x1 = event.x
        self.y1 = event.y

        preview = self.criar_figura(self.x1, self.y1)
        
        # se for mao_livre então vai adicionando na hora do movimento todos os previews e desenhando a figura, ou seja, desenhando o preview

        if self.model.ferramenta_atual == "Mao_Livre":
            self.model.figuras.append(preview)
            self.ini_x = event.x
            self.ini_y = event.y
            self.view.desenhar_figuras(self.model.figuras)
        else:
            self.view.desenhar_figuras(self.model.figuras, preview=preview)
    

     #quando solta o mouse pega as coordenadas finais (x2,y2) e cria a figura final com essas coordenadas
    def fim_mouse(self, event):
        #verifica se a figura é valida ou não (cada figura sabe se ela mesmo é valida ou se não é)
        # se não for válida, ela não se desenha, caso contrário, leva até o model e adiciona na lista das figuras e desenha
        self.x2 = event.x
        self.y2 = event.y

        figura = self.criar_figura(event.x, event.y)
        
        if not figura.validar():
            self.view.desenhar_figuras()
            return
        else:
            self.model.figuras.append(figura)
        self.view.desenhar_figuras(self.model.figuras)

    # os parâmetros x,y dependem do que for, por exemplo, se for o mouse_movimentacao (preview) que chama o metodo, então será passado x1,y1
    # caso for fim_mouse será passado x2,y2
    def criar_figura(self, x, y):
        classe_da_figura = self.ferramentas.get(self.model.ferramenta_atual)
        
        if self.model.ferramenta_atual in ["Mao_Livre", "Reta"]:
            return classe_da_figura(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda)
        else:
            return classe_da_figura(self.ini_x, self.ini_y, x, y, self.model.cor_selecionada_borda, self.model.cor_selecionada_preenchimento)