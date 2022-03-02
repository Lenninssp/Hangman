import random


class game:
    
    def __init__ (self):
        pass

    def juego(self):
        
        lenn_palabra={ "".join(self.lenn_palabra_oculta) : self.lenn_palabra_descubierta}
        
        lenn_input= input()
        print(lenn_palabra[self.lenn_palabra_descubierta])
            
        while True:

            if lenn_input == lenn_palabra [self.lenn_palabra_oculta]:
                print('pasaste')
                break
                
            else: 
                print('intentalo otra vez')
                        
            
    def eleccion(self):
        with open('/mnt/c/Users/lenni/Desktop/progamación/python/Proyectos/Hangman/hangman/lista.txt', 'r') as f:
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
            self.juego()
            return self
        
        
