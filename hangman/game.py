import random


class game:
    
    def __init__ (self):
        print('hola')
        game.eleccion()

    def juego(self):
        ganar = False
        
        while ganar == False:
            #len_input= input()
            print(self.lenn_palabra_descubierta, self.lenn_palabra_oculta)
            
            
    def eleccion(self):
        with open('lista.txt', 'r') as f:
            l = [a for a in f.readlines()]
            n=0
            for a in l:
                n += 1
            word= random.randint(0, n)
            num=[]
            for a in l[word-1]:
                if a != '\n':
                    num.append('_')
            self.lenn_palabra_descubierta= l[word-1]
            self.lenn_palabra_oculta= num
            print(l[word-1])
            print(''.join(num))
            game.juego()
            return self
            
                