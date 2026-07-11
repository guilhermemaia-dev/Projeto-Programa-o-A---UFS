from tkinter import *
from tkinter import colorchooser
import os

from model.mao_livre import Mao_Livre
from model.reta import Reta
from model.retangulo import Retangulo
from model.oval import Oval
from model.circulo import Circulo
from model.borracha import Borracha
from model.quadrado import Quadrado

class JanelaPaint:
    def __init__(self):
        self.janela = Tk()
        self.configuracao_janela()
        #obs: o controlador ainda n foi criado (apenas é criado na proxima linha do main)
        self.controller = None

    def configuracao_janela(self):
        self.janela.title("PAINT 2.1")
        self.janela.geometry("1600x900")


    def criar_elementos(self):
        self.canvas = Canvas(self.janela, width=1024, height=576, bg="white")
        self.canvas.pack(pady=20)

        self.estado_marcador = IntVar(value=0)
        self.marcador = Checkbutton(self.janela, text="Escolher preenchimento", variable=self.estado_marcador)
        self.marcador.pack(side=LEFT, padx=10)

        label_seletor_cor = Label(self.janela, text="SELETOR DE CORES")
        label_seletor_cor.pack(side=LEFT, padx=10)

        self.canvas.bind("<Button-1>", self.controller.mouse_ini)    
        self.canvas.bind("<B1-Motion>", self.controller.mouse_movimentacao) 
        self.canvas.bind("<ButtonRelease-1>", self.controller.fim_mouse)   

        # pede ao controlador para obter a lista de cores, ele pede para o model, o model devolve a ele, e ele devolve para o view
        cores = self.controller.obter_cor()
        
        #cria os botões do seletor de cores e quando clica, manda uma mensagem para o controller para informar a cor clicada e o estado do marcador
        for cor in cores:
            if cor == "#E7E7E7":
                bot_cor = Button(self.janela, width=2, height=1, highlightbackground="black", command=lambda COR='': self.controller.receberAcor(COR, self.estado_marcador.get()))
            else:
                bot_cor = Button(self.janela, width=2, height=1,bg=cor, command=lambda COR=cor: self.controller.receberAcor(COR, self.estado_marcador.get()))

            bot_cor.pack(side=LEFT, pady=1)

        #criar botão para escolher mais cores
        caminho = os.path.join(os.path.dirname(__file__), "maiscores.png")
        self.imagem = PhotoImage(file=caminho)
        self.imagem = self.imagem.subsample(10, 11)
        bot_mais_cores = Button(self.janela, image=self.imagem,command=self.abrir_seletor_cor)
        bot_mais_cores.pack(side=LEFT)

        #criar os botões do seletor de figuras e colocar na janela logo
        bot_livre = Button(self.janela, text="MÃO LIVRE", command=lambda: self.controller.selecionar_ferramenta("Mao_Livre"))
        bot_reta = Button(self.janela, text="RETA", command=lambda: self.controller.selecionar_ferramenta("Reta"))
        bot_retangulo = Button(self.janela, text="RETANGULAR", command=lambda: self.controller.selecionar_ferramenta("Retangulo"))
        bot_oval = Button(self.janela, text="OVAL", command=lambda: self.controller.selecionar_ferramenta("Oval"))
        bot_circulo = Button(self.janela, text="CIRCULAR", command=lambda: self.controller.selecionar_ferramenta("Circulo"))
        bot_borracha = Button(self.janela, text="BORRACHA", command=lambda: self.controller.selecionar_ferramenta("Borracha"))

        #Coloca os botões na janela
        bot_livre.pack(side=LEFT)
        bot_reta.pack(side=LEFT)
        bot_retangulo.pack(side=LEFT)
        bot_oval.pack(side=LEFT)
        bot_circulo.pack(side=LEFT)
        bot_borracha.pack(side=LEFT)

        #cria o botão para apagar tudo
        bot_limpar = Button(self.janela, text="LIMPAR",command=self.controller.limpar_tela)
        bot_limpar.pack(side=LEFT)

        # mostra a cor da borda atual na interface
        label_indicar_cor_borda = Label(self.janela, text="BORDA:")
        label_indicar_cor_borda.pack(side=LEFT, padx=10)
        self.label_cor_selecionadaBorda = Label(self.janela, bg=self.controller.model.cor_selecionada_borda, width=2, height=1)
        self.label_cor_selecionadaBorda.pack(side=LEFT, padx=10)

        # mostra a cor do preenchimento atual
        cor_preenc_default = self.controller.model.cor_selecionada_preenchimento
        if cor_preenc_default == "":
            cor_preenc_default = "#E7E7E7"
        label_indicar_cor_preenchimento = Label(self.janela, text="PREENCHIMENTO:")
        label_indicar_cor_preenchimento.pack(side=LEFT, padx=10)
        self.label_corPreench_selecionada = Label(self.janela, bg=cor_preenc_default, width=2, height=1)
        self.label_corPreench_selecionada.pack(side=LEFT, padx=10)

        # mostrar a ferramenta selecionada atualmente
        label_indicar_ferramenta_atual = Label(self.janela, text="Ferramenta selecionada:")
        label_indicar_ferramenta_atual.pack(side=LEFT, padx=10)
        self.mostrar_ferramenta_atual = Label(self.janela, text=self.controller.model.ferramenta_atual)
        self.mostrar_ferramenta_atual.pack(side=LEFT,padx=10)



    #metodo para o próprio view atualizar as cores do preview na tela
    def alterar_cor_preview(self, cor_borda, cor_preenchimento):
        self.label_cor_selecionadaBorda.configure(bg=cor_borda)
        if cor_preenchimento != "":
            self.label_corPreench_selecionada.configure(bg=cor_preenchimento)
        else:
            self.label_corPreench_selecionada.configure(bg="#E7E7E7")

    # metodo para alterar a ferramenta atual mostrada na tela
    def alterar_ferramenta_preview(self, ferramenta_atual):
        self.mostrar_ferramenta_atual.configure(text=ferramenta_atual)


    #abre o seletor e manda pro controller a cor escolhida pelo usuario
    def abrir_seletor_cor(self):
        cor = colorchooser.askcolor()[1]
        if cor:
            self.controller.receberAcor(cor, self.estado_marcador.get())



    # metodo simplificado que desenha tudo direto
    def desenhar_figuras(self, lista_figuras, apagarAtela=True):
        
        # se puder apagar a tela, apaga
        if apagarAtela:
            self.canvas.delete("all")


        # pede os dados de cada figura e desenha as figuras
        for figura in lista_figuras:
            if isinstance(figura, Mao_Livre) or isinstance(figura, Reta):
                ini_x, ini_y, posx, posy, cor = figura.pegar_dados()
                self.canvas.create_line(ini_x, ini_y, posx, posy, fill=cor)

            elif isinstance(figura, Borracha):
                self.canvas.create_line( figura.ini_x, figura.ini_y, figura.posx, figura.posy, fill=figura.cor, width=figura.tamanho)
                
            elif isinstance(figura, Retangulo):
                ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
                self.canvas.create_rectangle(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench)
                
            elif isinstance(figura, Oval):
                ini_x, ini_y, posx, posy, cor_borda, cor_preench = figura.pegar_dados()
                self.canvas.create_oval(ini_x, ini_y, posx, posy, outline=cor_borda, fill=cor_preench)
                
            elif isinstance(figura, Circulo):
                x0, y0, x1, y1, cor_borda, cor_preench = figura.pegar_dados()
                self.canvas.create_oval(x0, y0, x1, y1, outline=cor_borda, fill=cor_preench)

            elif isinstance(figura, Quadrado):
                x0, y0, cor_borda, cor_preench, tamanho, x_quadrado, y_quadrado = figura.pegar_dados()
                self.canvas.create_rectangle(x0, y0, x_quadrado, y_quadrado, outline=cor_borda, fill=cor_preench) #essa vai ser a fórmula da construção do quadrado#