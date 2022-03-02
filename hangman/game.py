import random


class game:
    
    def __init__ (self):
        pass

    def juego(self):
        oculta= "".join(self.lenn_palabra_oculta)
        lenn_palabra={ oculta : self.lenn_palabra_descubierta}
        print(list(lenn_palabra)[0])
        lenn_input= input('>')

        while True:
            count=0
            for _ in lenn_input.strip():
                count +=1
            if count > 1:
                print('solo puedes poner un digito a la vez')    
                lenn_input= input('>')
            elif lenn_input.strip() != lenn_palabra [oculta]:
                print('intentalo otra vez')
                lenn_input= input('>')
            elif lenn_input.strip() == lenn_palabra [oculta]: 
                print(lenn_palabra[oculta])
                print('pasaste')
                break
                        
            
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
        
        
