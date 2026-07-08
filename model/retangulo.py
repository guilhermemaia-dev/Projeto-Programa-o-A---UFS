class Retangulo(Figuras):
    def __init__(self, ini_x, ini_y, posx, posy, cor_borda, cor_preenchimento):
        super().__init__(ini_x, ini_y, posx, posy)
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
    
    def validar(self):
        return (self.posx - self.ini_x)**2 >= 20 or (self.posy - self.ini_y)**2 >= 20

        #LEMBRAR DE VERIFICAR SE ESSA MARGEM ESTÁ BOA!!!#