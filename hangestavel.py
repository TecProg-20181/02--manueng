import random
import string

WORDLIST_FILENAME = "palavras.txt"





class word(object):

     secretword=  []
     def test_triedletter(self,guessed):
         game2.triedletter(guessed);
         print game2.getletterguessed()
     def test_isecretwordGuessed(self,letter):
        game2=game()
        game2.setletter("d")
        if game2.getletter()=="d":
            print "deu tudo certo no setletter"
        self.setsecretword("aba") 
        print self.getsecretword(); 
        if  not self.isWordGuessed(game2):
           game2.setletter("a")
           guessed=''
           game2.triedletter(guessed);
           print game2.getletterguessed()
           if not  self.isWordGuessed(game2):
             game2.setletter("b")
             if  self.isWordGuessed(game2):
                print "deu tudo certo no metodo iswordguessed"  
        
     def __init__ (self,secretword): 
         self.secretword=secretword
     
     def guessedword(self,game): 
      letter=game.getletter()
      guessed=''
      lettersGuessed=game.lettersGuessed
      for letter in self.secretword:
       if letter in lettersGuessed:
         guessed += letter      
       else:
         guessed += '_ ' 
      
      return guessed

     def isWordGuessed(self, game):
        lettersGuessed=game.lettersGuessed
        i=0
        for letter in self.getsecretword():
         if letter in lettersGuessed:
            i=i+1
            print i
            if i==2:
              return True  
         else:
            return False
  	 
     def quantitydifferent(self):
         secretword=self.getsecretword()
         quantityletters=len(secretword)   
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
             
            
     def setsecretword(self,secretword):
         self.secretword=secretword
     def getsecretword(self):
         return self.secretword     
               
     

       
          
class game(object):
    guesses=8
    lettersGuessed =  []
    letter='y'
    def test_score(self):
        self.letter="c";
        worda=word("aca")
        guesses2=8;
        self.score(worda)
        if(self.guesses==guesses2):
          print "deu tudo certo no score" 

    def testsetletter(self):
        print " e um boleano"
        letter="a"
        self.setletter(letter)
        if letter==self.getletter():
            print "o metodo funcionou"  
    def validaletra(self,letter):
        if letter in string.ascii_lowercase:
            return True
        else:
            
            if letter.lower() in string.ascii_lowercase:
                return True
            else:
                return False

    def validaletraint(self,letter):
            try:
                letter.lower()
                return self.validaletra(letter) 
            except:
                return False
    def validapalavra(self,result):
        for letter in result :
            if self.validaletra(letter):
               pass
            else:
               return False
            print " e uma palavra"   
    def test_getletterguessed(result):
        result=self.triedletter(guessed)    
        if result or not result:
            print "deu tudo certo"
        if letter==self.getletterguessed():
            print " o metodo de tentativa funcionou" 
        if result :
            guessed=self.score(worda)                              
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
    def validaint(self,integer):
        if not self.validaletraint(integer): 
            if integer>0:
                return True 
    def setletter(self,letter):
           self.letter=letter             
    def gametry(self,secretWord) :
    
      print 'Welcome to the game, Hangam!'
      print 'I am thinking of a word that is', len(secretWord), ' letters long.'
      print '-------------'
      worda= word(secretWord)
      i=worda.quantitydifferent()
      self.validaint(i)
      
      guessed=' '    
      while worda.isWordGuessed(self) == False and self.guesses >0:
         print 'You have ', self.guesses, 'guesses left.'
         self.lettersavailable()
         invalid=True;
         while(invalid):
            letter = raw_input('Please guess a letter: ')
            invalid=not self.validaletra(letter)
         self.setletter(letter)
         self.triedletter(guessed)
         self.score(worda)
         worda.guessedword(self)
      else:
           if worda.isWordGuessed(self) == True:
             print 'Congratulations, you won!'
           else:
             print 'Sorry, you ran out of guesses. The word was ', worda.getsecretword(), '.'
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
    def score(self,worda):
         letter=self.letter          
         guessed=worda.guessedword(self)          
         if letter in worda.getsecretword():
            print 'Good Guess: ', guessed
         else:
            self.guesses -=1 
            print 'Oops! That letter is not in my word: ',  guessed
         print '------------'
         return guessed
   
    def getletter(self):
           return self.letter
    def getletterguessed(self):
            return self.lettersGuessed

      
game1=game()
secretWord = game1.loadWords().lower()
game1.validapalavra(secretWord)
game1.gametry(secretWord)
