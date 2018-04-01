import random
import string

WORDLIST_FILENAME = "palavras.txt"





class secretletters(object):

     secretword=  []

     def __init__ (self,secretword): 
         self.secretword=secretword

     def issecretwordletter(self,tentativa):
      letter=tentativa.letter
      jogador=tentativa.jogador 
      jogador.lettersGuessed.append(letter)       
      return self.issecretword(tentativa)
     
     def issecretword(self,tentativa): 
      guessed = ''
      letter=tentativa.letter 
      lettersGuessed=tentativa.jogador.lettersGuessed
      for letter in self.secretword:
       if letter in lettersGuessed:
         guessed += letter
       else:
         guessed += '_ '
      return guessed
     def isWordGuessed(self, jogador):
        lettersGuessed=jogador.lettersGuessed
        for letter in self.secretword:
         if letter in lettersGuessed:
            pass
         else:
            return False

        return True
             


       
          
class jogador(object):
    guesses=8
    lettersGuessed =  []
     
    def __init__(self):
        pass 
    def loadWords(self):
     """
     Depending on the size of the word list, this function may
     take a while to finish.
     """
     print "Loading word list from file..."
     # inFile: file
     inFile = open(WORDLIST_FILENAME, 'r', 0)
     # line: string
     line = inFile.readline()
     # wordlist: list of strings
     wordlist = string.split(line)
     print "  ", len(wordlist), "words loaded."
     return random.choice(wordlist)
    def jogada(self,secretWord) :
    
      print 'Welcome to the game, Hangam!'
      print 'I am thinking of a word that is', len(secretWord), ' letters long.'
      print '-------------'
      secretlettera= secretletters(secretWord)
      while secretlettera.isWordGuessed(self) == False and self.guesses >0:
         print 'You have ', self.guesses, 'guesses left.'
         
         available = self.getAvailableLetters()
         for letter in available:
          if letter in self.lettersGuessed:
                available = available.replace(letter, '')

         print 'Available letters', available
         letter = raw_input('Please guess a letter: ')
         tentativaa=tentativa(letter,jogador)
         if letter in self.lettersGuessed:
                guessed=secretlettera.issecretword(tentativaa)
                print 'Oops! You have already guessed that letter: ', guessed
         else:
           tentativaa.pontuar(secretlettera)  
      else:
         tentivaa=tentativa(letter,self)
         tentivaa.ultima(secretlettera)
    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available 

class tentativa:
      letter='y'
      jogador2=jogador()
      def __init__(self,letter,jogador):
       self.letter=letter
       self.jogador= jogador
      def pontuar(self,secretlettera):            
         if self.letter in secretWord:
            guessed=secretlettera.issecretwordletter(self)
            print 'Good Guess: ', guessed
         else:
            jogador.guesses -=1
            guessed=secretlettera.issecretwordletter(self)
            print 'Oops! That letter is not in my word: ',  guessed
         print '------------'
         return guessed
      def ultima(self,secretlettera):  
           if secretlettera.isWordGuessed(self.jogador2) == True:
             print 'Congratulations, you won!'
           else:
             print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'
jogador1=jogador()
secretWord = jogador1.loadWords().lower()
jogador1.jogada(secretWord)
