from tkinter import *
from tkinter import colorchooser
import os

class Header(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        #cria o frame para armazenar melhor os botoes e labels
        frame_linha1 = Frame(self)
        frame_linha1.pack()

        frame_linha2 = Frame(self)
        frame_linha2.pack()

    
        self.estado_marcador = IntVar(value=0)
        self.marcador = Checkbutton(frame_linha1, text="Escolher preenchimento", variable=self.estado_marcador)
        self.marcador.pack(side=LEFT, padx=10)
    
        label_seletor_cor = Label(frame_linha1, text="SELETOR DE CORES")
        label_seletor_cor.pack(side=LEFT, padx=10)

    
        # pede ao controlador para obter a lista de cores, ele pede para o model, o model devolve a ele, e ele devolve para o view
        cores = self.controller.obter_cor()
        
        #cria os botões do seletor de cores e quando clica, manda uma mensagem para o controller para informar a cor clicada e o estado do marcador
        for cor in cores:
            if cor == "#E7E7E7":
                bot_cor = Button(frame_linha1, width=2, height=1, highlightbackground="black", command=lambda COR='': self.controller.receberAcor(COR, self.estado_marcador.get()))
            else:
                bot_cor = Button(frame_linha1, width=2, height=1,bg=cor, command=lambda COR=cor: self.controller.receberAcor(COR, self.estado_marcador.get()))

            bot_cor.pack(side=LEFT, pady=1)
    
        #criar botão para escolher mais cores
        caminho = os.path.join(os.path.dirname(__file__), "..", "assets", "maiscores.png")
        self.imagem = PhotoImage(file=caminho)
        self.imagem = self.imagem.subsample(10, 11)

        bot_mais_cores = Button(frame_linha1, image=self.imagem,command=self.abrir_seletor_cor)
        bot_mais_cores.pack(side=LEFT)

        # mostra a cor da borda atual na interface
        label_indicar_cor_borda = Label(frame_linha1, text="BORDA:")
        label_indicar_cor_borda.pack(side=LEFT, padx=10)
        self.label_cor_selecionadaBorda = Label(frame_linha1, bg=self.controller.model.cor_selecionada_borda, width=2, height=1)
        self.label_cor_selecionadaBorda.pack(side=LEFT, padx=10)

        # mostra a cor do preenchimento atual
        cor_preenc_default = self.controller.model.cor_selecionada_preenchimento
        if cor_preenc_default == "":
            cor_preenc_default = "#E7E7E7"
        label_indicar_cor_preenchimento = Label(frame_linha1, text="PREENCHIMENTO:")
        label_indicar_cor_preenchimento.pack(side=LEFT, padx=10)
        self.label_corPreench_selecionada = Label(frame_linha1, bg=cor_preenc_default, width=2, height=1)
        self.label_corPreench_selecionada.pack(side=LEFT, padx=10)

    
        #criar os botões do seletor de figuras e colocar na janela logo
        bot_livre = Button(frame_linha2, text="MÃO LIVRE", command=lambda: self.controller.selecionar_ferramenta("Mao_Livre"))
        bot_reta = Button(frame_linha2, text="RETA", command=lambda: self.controller.selecionar_ferramenta("Reta"))
        bot_retangulo = Button(frame_linha2, text="RETANGULAR", command=lambda: self.controller.selecionar_ferramenta("Retangulo"))
        bot_oval = Button(frame_linha2, text="OVAL", command=lambda: self.controller.selecionar_ferramenta("Oval"))
        bot_circulo = Button(frame_linha2, text="CIRCULAR", command=lambda: self.controller.selecionar_ferramenta("Circulo"))
        bot_quadrado = Button(frame_linha2,text="QUADRADO",command=lambda:self.controller.selecionar_ferramenta("Quadrado"))
        bot_borracha = Button(frame_linha2, text="BORRACHA", command=lambda: self.controller.selecionar_ferramenta("Borracha"))
        bot_selecao = Button(frame_linha2, text="SELEÇÃO",command=lambda: self.controller.selecionar_ferramenta("Seleção"))
        bot_selecao_area = Button(frame_linha2, text="SELEÇÃO MÚLTIPLA", command=lambda: self.controller.selecionar_ferramenta("Selecao_Area"))
        bot_limpar = Button(frame_linha2, text="LIMPAR", bg="#9c5b56", fg="white" ,command=self.controller.limpar_tela)
    
        #Coloca os botões na janela
        bot_livre.pack(side=LEFT, padx=1)
        bot_reta.pack(side=LEFT, padx=1)
        bot_retangulo.pack(side=LEFT, padx=1)
        bot_oval.pack(side=LEFT, padx=1)
        bot_circulo.pack(side=LEFT, padx=1)
        bot_quadrado.pack(side=LEFT, padx=1)
        bot_borracha.pack(side=LEFT, padx=1)
        bot_selecao.pack(side=LEFT,padx=1)
        bot_selecao_area.pack(side=LEFT, padx=1)
        bot_limpar.pack(side=LEFT)
    
    
        # mostrar a ferramenta selecionada atualmente
        label_indicar_ferramenta_atual = Label(frame_linha2, text="Ferramenta selecionada:")
        label_indicar_ferramenta_atual.pack(side=LEFT, padx=10)
        self.mostrar_ferramenta_atual = Label(frame_linha2, text=self.controller.model.ferramenta_atual)
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