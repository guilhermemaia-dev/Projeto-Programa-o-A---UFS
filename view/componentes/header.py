from tkinter import *
from tkinter import colorchooser
import os

class Header(Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg="#1E1E2E", highlightthickness=0, bd=0)
        self.controller = controller

        self.bg_bloco = "#2A2A3C"
        self.fg_texto = "#CDD6F4"
        self.fg_preview = "#A6ADC8"
        self.bg_botao_ferramentas = "#A7A9C4"

        self.cor_lixo_padrao = "#E05757"
        self.cor_lixo_hover = "#E02323"
        self.cor_acoes_padrao = "#3163C0"
        self.cor_acoes_hover = "#183772"

        self.botoes_ferramentas = {}
        self.frame_superior = Frame(self, bg="#1E1E2E", padx=12, pady=8)
        self.frame_superior.pack(fill=X)

        # caminho para a pasta assets
        pasta_assets = os.path.join(os.path.dirname(__file__), "..", 'assets')




        # BARRA DE DESFAZER E REFAZER
        self.bloco_acoes = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8, highlightbackground="#313244", highlightthickness=1)
        self.bloco_acoes.pack(side=LEFT, fill=Y, padx=(0,10))

        caminho_undo = os.path.join(pasta_assets, "undo.png")
        self.imagem_undo = PhotoImage(file=caminho_undo).subsample(20, 20)
        caminho_redo = os.path.join(pasta_assets, "redo.png")
        self.imagem_redo = PhotoImage(file=caminho_redo).subsample(20, 20)

        bot_desfazer = Button(self.bloco_acoes,
                                image=self.imagem_undo,
                                bg=self.cor_acoes_padrao,
                                activebackground=self.cor_acoes_hover,
                                relief=FLAT,
                                bd=0,
                                padx=10,
                                pady=4,
                                font=("Segoe UI", 9, "bold"),
                                cursor="hand2",
                                command=self.controller.ctrl_z)
        bot_desfazer.grid(row=0, column=0, padx=2, pady=4)

        bot_refazer = Button(self.bloco_acoes,
                                image=self.imagem_redo,
                                bg=self.cor_acoes_padrao,
                                activebackground=self.cor_acoes_hover,
                                relief=FLAT,
                                bd=0,
                                padx=10,
                                pady=4,
                                font=("Segoe UI", 9, "bold"),
                                cursor="hand2",
                                command=self.controller.ctrl_y)
        bot_refazer.grid(row=1, column=0, padx=2, pady=4)

        bot_desfazer.bind("<Enter>", lambda e: e.widget.configure(bg=self.cor_acoes_hover))
        bot_desfazer.bind("<Leave>", lambda e: e.widget.configure(bg=self.cor_acoes_padrao))
        bot_refazer.bind("<Enter>", lambda e: e.widget.configure(bg=self.cor_acoes_hover))
        bot_refazer.bind("<Leave>", lambda e: e.widget.configure(bg=self.cor_acoes_padrao))


        

        #BARRA DE FERRAMENTAS
        self.bloco_ferramentas = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8, highlightbackground="#313244", highlightthickness=1)
        self.bloco_ferramentas.pack(side=LEFT, fill=Y, padx=(0,10))

        label_titulo_ferramentas = Label(self.bloco_ferramentas, text="FERRAMENTAS", bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 8, "bold"))
        label_titulo_ferramentas.grid(row=0, column=0, columnspan=5, sticky="w", pady=(0,4))

        botoes = [
            ("pencil.png", "Mao_Livre"),
            ("line.png", "Reta"),
            ("retangulo.png", "Retangulo"),
            ("oval.png", "Oval"),
            ("circle.png", "Circulo"),
            ("square.png", "Quadrado"),
            ("paint-brush.png", "Pincel"),
            ("selection.png", "Seleção"),
            ("selection_area.png", "Selecao_Area"),]

        self.imagens_ferramentas = {}

        for i, (arq_img, nome_ferramenta) in enumerate(botoes):
            linha_btn = (i // 5) + 1
            coluna_btn = i % 5

            caminho = os.path.join(pasta_assets, arq_img)
            img = PhotoImage(file=caminho)

            img = img.subsample(20, 20)

            self.imagens_ferramentas[nome_ferramenta] = img

            btn = Button(self.bloco_ferramentas,
                            image=self.imagens_ferramentas[nome_ferramenta],
                            bg=self.bg_botao_ferramentas,
                            fg=self.fg_texto,
                            activeforeground="#1E1E2E",
                            activebackground="white",
                            relief=FLAT,
                            bd=0,
                            padx=8,
                            pady=4,
                            font=("Segoe UI", 9),
                            cursor="hand2",
                            command=lambda f=nome_ferramenta: self.controller.selecionar_ferramenta(f))
            btn.grid(row=linha_btn, column=coluna_btn, padx=2, pady=2)

            self.botoes_ferramentas[nome_ferramenta] = btn

            btn.bind("<Enter>", lambda event, f=nome_ferramenta: self.hover_enter(event, f))
            btn.bind("<Leave>", lambda event, f=nome_ferramenta: self.hover_leave(event, f))

        #BOTAO DE LIMPAR A TELA
        caminho_delete = os.path.join(pasta_assets, "trash.png")
        self.imagem_delete = PhotoImage(file=caminho_delete).subsample(20, 20)

        bot_limpar = Button(self.bloco_ferramentas,
                            image=self.imagem_delete,
                            bg=self.cor_lixo_padrao,
                            activebackground=self.cor_lixo_hover,
                            relief=FLAT,
                            bd=0,
                            padx=10,
                            pady=4,
                            font=("Segoe UI", 9, "bold"),
                            cursor="hand2",
                            command=self.controller.limpar_tela)
        bot_limpar.grid(row=2, column=4, padx=2, pady=2)

        bot_limpar.bind("<Enter>", lambda e: e.widget.configure(bg=self.cor_lixo_hover))
        bot_limpar.bind("<Leave>", lambda e: e.widget.configure(bg=self.cor_lixo_padrao))






        #CRIAÇÃO DO FRAME DO BLOCO QUE SELECIONA AS CORES
        self.bloco_sel_cores = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8, highlightbackground="#313244", highlightthickness=1)
        self.bloco_sel_cores.pack(side=LEFT, fill=Y, padx=(0,10))

        self.estado_marcador = IntVar(value=0)
        self.marcador = Checkbutton(self.bloco_sel_cores, 
                                    font=("Segoe UI", 9, "bold"), 
                                    text="Escolher preenchimento", 
                                    variable=self.estado_marcador, 
                                    bg=self.bg_bloco, 
                                    fg=self.fg_texto, 
                                    selectcolor="#181825", 
                                    activebackground=self.bg_bloco, 
                                    activeforeground=self.fg_texto)
        self.marcador.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,4))



        #CRIAÇÃO DO FRAME DA PALETA DE CORES
        frame_paleta = Frame(self.bloco_sel_cores, bg=self.bg_bloco)
        frame_paleta.grid(row=1, column=0, columnspan=2)

        cores = self.controller.obter_cor()
        linha, coluna = 0,0
        for cor in cores:
            if cor == "":
                bot_cor = Button(frame_paleta,
                                 text="∅",
                                 width=2,
                                 height=1,
                                 bg=self.bg_bloco,
                                 relief=SOLID,
                                 bd=1,
                                 cursor="hand2",
                                 activebackground="#313244",
                                 activeforeground="#CDD6F4",
                                 command=lambda: self.controller.receberAcor("", self.estado_marcador.get()))
            else:
                bot_cor = Button(frame_paleta, 
                                width=2, 
                                height=1, 
                                bg=cor,
                                relief=FLAT,
                                bd=0,
                                cursor="hand2",
                                activebackground=cor,
                                command=lambda COR=cor: self.controller.receberAcor(COR, self.estado_marcador.get()))
            
            bot_cor.grid(row=linha, column=coluna, padx=2, pady=2)
            coluna += 1
            if coluna > 9:
                coluna = 0
                linha += 1



        #BOTAO PARA ESCOLHER MAIS CORES

        self.bloco_mais_cores = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8,highlightbackground="#313244", highlightthickness=1)
        self.bloco_mais_cores.pack(side=LEFT, fill=Y, padx=(0,10))

        caminho = os.path.join(pasta_assets, "maiscores.png")
        self.imagem = PhotoImage(file=caminho)
        self.imagem = self.imagem.subsample(15,5)
        bot_mais_cores = Button(self.bloco_mais_cores, image=self.imagem, bg="#313244", relief=FLAT, bd=0, cursor="hand2", command=self.abrir_seletor_cor, width=40, height=60)
        bot_mais_cores.grid(row=linha, column=coluna, padx=2, pady=2)

        label_mais_cores = Label(self.bloco_mais_cores, text="EDITAR CORES", bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 8, "bold"))
        label_mais_cores.grid(row=1, column=0, pady=(0, 4))





        #PREVIEW
        self.bloco_preview = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8, highlightbackground="#313244", highlightthickness=1)
        self.bloco_preview.pack(side=LEFT, padx=(0, 10), fill=Y)

        label_titulo_preview = Label(self.bloco_preview, text="ESTADO DAS CORES", bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 8, "bold"))
        label_titulo_preview.grid(row=0, column=0, columnspan=2, pady=(0, 4))



        #COR DA BORDA
        label_indicar_cor_borda = Label(self.bloco_preview, text="Borda:", bg=self.bg_bloco, fg=self.fg_texto, font=("Segoe UI", 9))
        label_indicar_cor_borda.grid(row=1, column=0, sticky="e", padx=(0,4))

        self.label_cor_selecionadaBorda = Label(self.bloco_preview, 
                                                bg=self.controller.obter_cor_borda(), 
                                                width=2, 
                                                height=1, 
                                                relief=SOLID, 
                                                bd=1)
        self.label_cor_selecionadaBorda.grid(row=1, column=1, padx=(0,10))




        #COR DO PREENCHIMENTO
        cor_preenc_default = self.controller.obter_cor_preenchimento() or "#E7E7E7"
        label_indicar_cor_preenchimento = Label(self.bloco_preview, text="Preenchimento:", bg=self.bg_bloco, fg=self.fg_texto, font=("Segoe UI", 9))

        label_indicar_cor_preenchimento.grid(row=2, column=0, sticky="e", padx=(0, 4))

        self.label_corPreench_selecionada = Label(self.bloco_preview, 
                                                  bg=cor_preenc_default, 
                                                  width=2, 
                                                  height=1, 
                                                  bd=1, 
                                                  relief=SOLID)
        self.label_corPreench_selecionada.grid(row=2, column=1, padx=(0,10))



        # ESPESSURA

        self.bloco_espessura = Frame(self.frame_superior, bg=self.bg_bloco, padx=12, pady=8, highlightbackground="#313244", highlightthickness=1)
        self.bloco_espessura.pack(side=LEFT, padx=(0, 10), fill=Y)

        label_titulo_espessura = Label(self.bloco_espessura, text="ESPESSURA", bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 8, "bold"))
        label_titulo_espessura.grid(row=0, column=0, columnspan=2, pady=(0,4), sticky="w")

        self.scale_espessura = Scale(self.bloco_espessura,
                                     from_=1,
                                     to=40,
                                     orient=HORIZONTAL,
                                     showvalue=0,
                                     bg=self.bg_bloco,
                                     fg=self.fg_texto,
                                     troughcolor="#15151D",
                                     activebackground="white",
                                     highlightthickness=0,
                                     length=100,
                                     bd=0,
                                     cursor="hand2",
                                     command=self.controller.atualizar_espessura)

        self.scale_espessura.set(3)
        self.scale_espessura.grid(row=1, column=0, sticky="ew")

        label_titulo_espessura_atual = Label(self.bloco_espessura, text="Atual:", bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 8, "bold"))
        label_titulo_espessura_atual.grid(row=3, column=0, pady=(0,4), sticky="w")
        
        self.label_espessura_atual = Label(self.bloco_espessura, text=self.controller.obter_espessura_atual(), bg=self.bg_bloco, fg=self.fg_preview, font=("Segoe UI", 11, "bold"))
        self.label_espessura_atual.grid(row=4, column=0, columnspan=2, pady=(0,4), sticky="w")



    # metodos para mudar a cor no hover 
    def hover_enter(self, event, nome_ferramenta):
        if self.controller.obter_ferramenta_atual() != nome_ferramenta:
            event.widget.configure(bg="white")

    def hover_leave(self, event, nome_ferramenta):
        if self.controller.obter_ferramenta_atual() != nome_ferramenta:
            event.widget.configure(bg=self.bg_botao_ferramentas)


    # metodo para alterar o preview da espessura
    def atualizar_label_espessura(self, valor):
        self.label_espessura_atual.config(text=str(valor))



    #metodo para o próprio view atualizar as cores do preview na tela
    def alterar_cor_preview(self, cor_borda, cor_preenchimento):
        self.label_cor_selecionadaBorda.configure(bg=cor_borda)
        if cor_preenchimento != "":
            self.label_corPreench_selecionada.configure(bg=cor_preenchimento)
        else:
            self.label_corPreench_selecionada.configure(bg="white")


    # metodo para alterar a ferramenta atual mostrada na tela
    def alterar_ferramenta_preview(self, ferramenta_atual):
        for nome_ferramenta, btn in self.botoes_ferramentas.items():
            if nome_ferramenta == ferramenta_atual:
                btn.configure(bg="white", fg="#11111B", font=("Segoe UI", 9, "bold"))
            else:
                btn.configure(bg=self.bg_botao_ferramentas, fg=self.fg_texto, font=("Segoe UI", 9))



    #abre o seletor e manda pro controller a cor escolhida pelo usuario
    def abrir_seletor_cor(self):
        cor = colorchooser.askcolor()[1]
        if cor:
            self.controller.receberAcor(cor, self.estado_marcador.get())