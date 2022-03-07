import random

import tryout


class Wordle:

    def __init__(self):
        self.yellow = '\x1b[6;30;43m'
        self.green = '\x1b[6;30;42m'
        self.endColor = '\x1b[0m'
        f = open("words.txt", "r")
        self.targetWordList = f.readlines()
        f.close()
        self.targetWord = self.targetWordList[random.randint(0,5756)]

    def checkWord(self, s: str) -> str:
        a = ""
        for i in range(len(s)):
            if s[i] == self.targetWord[i]:
                a = a+self.green+s[i]+self.endColor
            elif self.targetWord.__contains__(s[i]):
                a = a+self.yellow+s[i]+self.endColor
            else:
                a = a+s[i]
        return a

    def startGame(self):
        for i in range(6):
            while True:
                s = input("Versuch:")
                if len(s)==5 and s.isalpha() and tryout.WordleGetWord().isvalid(s):
                    break
                else:
                    print("Ungültig!")
            if s==self.targetWord:
                print('Richtig! Du hast {} Versuche gebraucht.'.format(i+1))
                print('Das Wort war: '+self.green+s+self.endColor)
                return
            else:
                print(self.checkWord(s))
        print("Schade! Das Wort war: "+self.targetWord)
        return


a = Wordle()
a.startGame()
