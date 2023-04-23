import sys
from utils import *
class Solver(Wordle):
    def __init__(self):
        super().__init__()

    def generate_guess(self, feedback=None):
        guess = "hello"     #larger number of vowels, a faster way 
        if not len(self.guesses):
            return guess
        temp = self.words;
        for k in range(len(self.feedbacks)):
            for i in range(5):
                if self.feedbacks[k][i] == 0:
                    for t in temp:
                        if self.guesses[k][i] in t:
                            temp.remove(t)
                elif self.feedbacks[k][i] == 2:
                    for t in temp:
                        if self.guesses[k][i] not in t or t[i] == self.guesses[k][i]:
                            temp.remove(t)
                elif self.feedbacks[k][i] == 1:
                    t=0
                    length = len(temp)
                    while t < length:
                        if temp[t][i] != self.guesses[k][i]:
                            print(temp[t],'\t',len(temp), end = '\n')
                            temp.remove(temp[t])
                        t+=1
                        length = len(temp)
        guess = random.choice(temp)
        return guess

game = Game(Solver, N=6)
game.run()