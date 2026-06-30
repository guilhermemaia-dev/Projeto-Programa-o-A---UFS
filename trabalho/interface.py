import estado
import ferramentas
from tkinter import *
import config

def receberAcor(cor_clicada):
    
    if estado.estado_marcador.get() == 1:
        estado.cor_Dopreenchimento = cor_clicada
        if estado.cor_Dopreenchimento != '':
            estado.label_corPreench_selecionada.configure(bg=estado.cor_Dopreenchimento)
        else:
            estado.label_corPreench_selecionada.configure(bg="#E7E7E7")
    else:
        if cor_clicada == '':
            estado.cor_selecionadaBorda = "#000000"
        else:
            estado.cor_selecionadaBorda = cor_clicada
            
        estado.label_cor_selecionadaBorda.configure(bg=estado.cor_selecionadaBorda)

# MARCADOR DE PREENCHIMENTO: Se ativo, seletor de cores escolhe o preenchimento, caso contrário serve apenas para a borda
estado.estado_marcador = IntVar(estado.root, value=0)
marcador = Checkbutton(estado.root, text="Escolher preenchimento", variable=estado.estado_marcador)
marcador.pack(side=LEFT, padx=10)

#Painel para alterar cor
estado.escolha_cor = Label(text="SELETOR DE CORES : ")
estado.escolha_cor.pack(side=LEFT, padx=10)

# cria os botões de cores
for cor in config.cores:
    if cor == "#E7E7E7":
        bot_cor = Button(estado.root, width=2, height=1, highlightbackground="black", command=lambda COR='': receberAcor(COR))
    else:
        bot_cor = Button(estado.root, bg=cor, width=2, height=1, command=lambda COR=cor: receberAcor(COR))

    bot_cor.pack(side=LEFT, padx=1)

#Os 'bot_' criam os botões para alterar o formato#
bot_livre = Button(estado.root, text="MÃO LIVRE", command=ferramentas.livre)
bot_reta = Button(estado.root, text="RETA", command=ferramentas.reta)
bot_retangulo = Button(estado.root, text="RETANGULAR", command=ferramentas.retangulo)
bot_oval = Button(estado.root, text="OVAL", command=ferramentas.oval)
bot_circulo = Button(estado.root, text="CIRCULAR", command=ferramentas.circulo)

#Coloca os botões na janela#
bot_livre.pack(side=LEFT)
bot_reta.pack(side=LEFT)
bot_retangulo.pack(side=LEFT)
bot_oval.pack(side=LEFT)
bot_circulo.pack(side=LEFT)


# mostra a cor da borda atual
label_indicar_cor_borda = Label(estado.root, text="BORDA:")
label_indicar_cor_borda.pack(side=LEFT, padx=10)
estado.label_cor_selecionadaBorda = Label(estado.root, bg=estado.cor_selecionadaBorda, width=2, height=1)
estado.label_cor_selecionadaBorda.pack(side=LEFT, padx=10)

# mostra a cor do preenchimento atual
label_indicar_cor_preenchimento = Label(estado.root, text="PREENCHIMENTO:")
label_indicar_cor_preenchimento.pack(side=LEFT, padx=10)
estado.label_corPreench_selecionada = Label(estado.root, bg="#E7E7E7", width=2, height=1)
estado.label_corPreench_selecionada.pack(side=LEFT, padx=10)