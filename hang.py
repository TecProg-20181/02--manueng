import random
import string

WORDLIST_FILENAME = "palavras.txt"





class secretletters(object):

     secretword=  []
     
  
     def __init__ (self,secretword): 
         self.secretword=secretword
     
     def issecretword(self,jogador): 
      letter=jogador.letter 
      guessed=''
      lettersGuessed=jogador.lettersGuessed
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

     def quandif(self,secretWord):
         quantityletters=len(secretWord)   
         i2=0
         i=0
         iquals=[]
         letter3="w"
         numberofdifferents=0     
         Indexwent=[]      
         for letter in secretWord:
          i=i+1
          result =True          
          for letter2 in secretWord:  
            i2=i2+1  
            if letter==letter2 and i2>i:
               for n in Indexwent : 
                  if n==i2:
                     result=False 
               if result:                  
                   Indexwent.append(i2) 
                   numberofdifferent=quantityletters-1    
                        
          i2=0      
         print "number of different:", numberofdifferent           
         return numberofdifferent                  
             
            
          
               


       
          
class jogador(object):
    guesses=8
    lettersGuessed =  []
    letter='y'
     
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
      secretlettera.quandif(secretWord)
      guessed=' '    
      while secretlettera.isWordGuessed(self) == False and self.guesses >0:
         print 'You have ', self.guesses, 'guesses left.'
         self.lettersavailable()
         letter = raw_input('Please guess a letter: ')
         self.setletter(letter) 
         result=self.triedletter(guessed)     
         if result :
            guessed=self.pontuar(secretlettera)    
      else:
           if secretlettera.isWordGuessed(self) == True:
             print 'Congratulations, you won!'
           else:
             print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'
    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available
    def lettersavailable(self):
         available = self.getAvailableLetters()
         for letter in available:
          if letter in self.getletterguessed():
                available = available.replace(letter, '')
         print 'Available letters', available 
    def  triedletter(self,guessed):
         letter=self.getletter()     
         if letter in self.getletterguessed():
               print 'Oops! You have already guessed that letter: ', guessed
               return False
         else: 
            self.lettersGuessed.append(letter) 
         return True 
    def pontuar(self,secretlettera):
         letter=self.letter          
         guessed=secretlettera.issecretword(self)          
         if self.getletter() in secretlettera.secretword:
            print 'Good Guess: ', guessed
         else:
            self.guesses -=1 
            print 'Oops! That letter is not in my word: ',  guessed
         print '------------'
         return guessed
    def setletter(self,letter):
           self.letter=letter 
    def getletter(self):
           return self.letter
    def getletterguessed(self):
            return self.lettersGuessed

      
jogador1=jogador()
secretWord = jogador1.loadWords().lower()
jogador1.jogada(secretWord)
