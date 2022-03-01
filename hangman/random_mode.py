import time
import string as lennin_string
from random import randint

class a:

    def __init__ (self, max= None):
        self.max= max
        
    def __iter__(self):
        self.lennin_b = []
        return self
    
    def __next__(self):
        for _ in range(randint(3, 10)):
                loop_election = randint (0,1)
                if loop_election == 0:
                    self.lennin_b.append(lennin_vocals[randint(0, len(lennin_vocals)-1)])
                if loop_election == 1:
                    self.lennin_b.append(lennin_consonants [randint(0, len(lennin_consonants)-1)])
        print("".join(self.lennin_b))
        x = self.lennin_b
        self.lennin_b = []
        return x
    
    
if __name__ == '__main__': 
    lennin_vocals=  [a for a in lennin_string.ascii_lowercase if  a == 'a' or a =='e' or a =='i' or a =='o' or a =='u' ]
    lennin_consonants= [ a for a in lennin_string.ascii_lowercase if a != 'a' and a !='e'  and a !='i' and a !='o' and a !='u']
    aL = a
    for a in aL():
        time.sleep(0.5)
        aL()