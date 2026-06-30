import estado

#Pega a coordenada inicial do mouse (no momento do clique)
def mouse_ini(event):
    estado.ini_x = event.x
    estado.ini_y = event.y

    estado.pre_x = event.x
    estado.pre_y = event.y

#Pego a posição inicial e a atual e cria uma linha, então transforma a atual na inicial e repete o processo#
def mao_livre(event):
    x1 = event.x
    y1 = event.y
    estado.canva.create_line(estado.ini_x, estado.ini_y, x1, y1, fill=estado.cor_selecionadaBorda)
    estado.traco.append((estado.ini_x, estado.ini_y, x1, y1, estado.cor_selecionadaBorda))
    estado.ini_x = x1
    estado.ini_y = y1

#Cria as previews durante o movimento de uma reta, usando o movimento do mouse#
def linha_preview(event):
    x1 = event.x
    y1 = event.y
    estado.canva.delete("all")
    redesenhar()
    estado.canva.create_line(estado.ini_x, estado.ini_y, x1, y1, fill=estado.cor_selecionadaBorda)

#Adiciona a reta para a lista de linha e redesenha tudo adicionando esse item#
def linha_fim(event):
    x2 = event.x
    y2 = event.y
    estado.linha.append ((estado.ini_x, estado.ini_y, x2, y2, estado.cor_selecionadaBorda))

#Cria as previews durante o movimento do retangulo, usando o movimento do mouse#
def retangulo_preview(event):
    estado.pre_x = event.x
    estado.pre_y = event.y
    estado.canva.delete("all")
    redesenhar()
    estado.canva.create_rectangle(estado.ini_x, estado.ini_y, estado.pre_x, estado.pre_y, outline=estado.cor_selecionadaBorda, fill=estado.cor_Dopreenchimento)

#Adiciona o retângulo a lista de retangulos e redesenha com esse novo item#
def retangulo_fim(event):
    x2 = event.x
    y2 = event.y
    #garante que não crie retangulos com um único clique
    if estado.ini_x != estado.pre_x or estado.ini_y != estado.pre_y:
        estado.retangulos.append((estado.ini_x, estado.ini_y, x2, y2, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento))
    redesenhar()

#Cria as previews durante o movimento do objeto oval, usando o movimento do mouse#
def oval_preview(event):
    estado.pre_x = event.x
    estado.pre_y = event.y
    estado.canva.delete("all")
    redesenhar()
    estado.canva.create_oval(estado.ini_x, estado.ini_y, estado.pre_x, estado.pre_y, fill=estado.cor_Dopreenchimento, outline=estado.cor_selecionadaBorda)

    #Adiciona o objeto oval a lista de ovais e redesenha com esse novo item#
def oval_fim(event):
    x2 = event.x
    y2 = event.y
    #garante que não crie um oval com um único clique
    if estado.ini_x != estado.pre_x or estado.ini_y != estado.pre_y:
        estado.ovais.append((estado.ini_x, estado.ini_y, x2, y2, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento))
    redesenhar()

#Cria as previews durante o movimento do circulo, usando o movimento do mouse#
def circulo_preview(event):
    estado.pre_x = event.x
    estado.pre_y = event.y
    raio = (((estado.ini_x - estado.pre_x)**2 + (estado.ini_y - estado.pre_y)**2) ** 0.5)
    estado.canva.delete("all")
    redesenhar()
    estado.canva.create_oval(estado.ini_x-raio, estado.ini_y-raio, estado.ini_x+raio, estado.ini_y+raio, outline=estado.cor_selecionadaBorda, fill=estado.cor_Dopreenchimento)

#Adiciona o círculo a lista de circulos e redesenha com esse novo item#
def circulo_fim(event):
    x2 = event.x
    y2 = event.y
    raio = (((estado.ini_x - x2)**2 + (estado.ini_y - y2)**2) ** 0.5)
    #garante que não crie um circulo com um único clique
    if estado.ini_x != estado.pre_x or estado.ini_y != estado.pre_y:
        estado.circulos.append ((estado.ini_x, estado.ini_y, raio, estado.cor_selecionadaBorda, estado.cor_Dopreenchimento))
    redesenhar()

#REDESENHA TODOS OS OBJETOS JÁ COLOCADOS USANDO AS LISTAS DELES#
def redesenhar():
    for rabisco in estado.traco:
        x1,y1,x2,y2,cor_selecionadaBorda = rabisco
        estado.canva.create_line(x1,y1,x2,y2, fill=cor_selecionadaBorda)
    for reta in estado.linha:
        x1,y1,x2,y2,cor_selecionadaBorda = reta
        estado.canva.create_line(x1,y1,x2,y2, fill=cor_selecionadaBorda)
    for retangulo in estado.retangulos:
        x1, y1, x2, y2, cor_selecionadaBorda, cor_Dopreenchimento = retangulo
        estado.canva.create_rectangle(x1, y1, x2, y2, outline=cor_selecionadaBorda, fill=cor_Dopreenchimento)
    for oval in estado.ovais:
        x1,y1,x2,y2, cor_selecionadaBorda, cor_Dopreenchimento = oval
        estado.canva.create_oval(x1,y1,x2,y2, outline=cor_selecionadaBorda, fill=cor_Dopreenchimento)  
    for circulo in estado.circulos:
        x1,y1,r, cor_selecionadaBorda, cor_Dopreenchimento = circulo
        estado.canva.create_oval(x1-r, y1-r, x1+r, y1+r, outline=cor_selecionadaBorda, fill=cor_Dopreenchimento)

#Escolha de formatos que serão usados pelos botões, ou seja, a função retangulo, por exemplo, vai ser usada como comando no botão
def livre():
    estado.canva.bind('<B1-Motion>', mao_livre)
    estado.canva.unbind('<ButtonRelease-1>')

def reta():
    estado.canva.bind('<B1-Motion>', linha_preview)
    estado.canva.bind('<ButtonRelease-1>', linha_fim)

def retangulo():
    estado.canva.bind('<B1-Motion>', retangulo_preview)
    estado.canva.bind('<ButtonRelease-1>', retangulo_fim)

def oval():
    estado.canva.bind('<B1-Motion>', oval_preview)
    estado.canva.bind('<ButtonRelease-1>', oval_fim)

def circulo():
    estado.canva.bind('<B1-Motion>', circulo_preview)
    estado.canva.bind('<ButtonRelease-1>', circulo_fim)

