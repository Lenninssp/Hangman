import random


class game:

    def juego():
        pass
    def eleccion():
        with open('lista.txt', 'r') as f:
            l = [a for a in f.readlines()]
            print(l)
            n=0
            for a in l:
                n += 1
            word= random.randint(0, n)
            num=[]
            for a in l[word-1]:
                if a != '\n':
                    num.append('_')
            print(l[word-1])
            print(''.join(num))