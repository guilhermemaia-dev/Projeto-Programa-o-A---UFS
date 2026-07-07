from tkinter import *

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

        # pede ao controlador para obter a lista de cores, ele pede para o model, o model devolve a ele, e ele devolve para o view
        cores = self.controller.obter_cor()
        
        #cria os botões do seletor de cores e quando clica, manda uma mensagem para o controller para informar a cor clicada e o estado do marcador
        for cor in cores:
            if cor == "#E7E7E7":
                bot_cor = Button(self.janela, width=2, height=1, highlightbackground="black", command=lambda COR='': self.controller.receberAcor(COR, self.estado_marcador.get()))
            else:
                bot_cor = Button(self.janela, width=2, height=1,bg=cor, command=lambda COR=cor: self.controller.receberAcor(COR, self.estado_marcador.get()))

            bot_cor.pack(side=LEFT, pady=1)

        #criar os botões do seletor de figuras e colocar na janela logo
        bot_livre = Button(self.janela, text="MÃO LIVRE", command=self.controller.selecionar_livre)
        bot_reta = Button(self.janela, text="RETA", command=self.controller.selecionar_reta)
        bot_retangulo = Button(self.janela, text="RETANGULAR", command=self.controller.selecionar_retangulo)
        bot_oval = Button(self.janela, text="OVAL", command=self.controller.selecionar_oval)
        bot_circulo = Button(self.janela, text="CIRCULAR", command=self.controller.selecionar_circulo)

        #Coloca os botões na janela
        bot_livre.pack(side=LEFT)
        bot_reta.pack(side=LEFT)
        bot_retangulo.pack(side=LEFT)
        bot_oval.pack(side=LEFT)
        bot_circulo.pack(side=LEFT)


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