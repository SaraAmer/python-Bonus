#!/usr/bin/env python3
import random
import os.path
tries = 0;
n = random.randint(0,100)
print(n)
oldTries = []      
def playAgain():
    global tries
    global n
    tries=0
    n = random.randint(0,100)
    print(n)
    
    oldTries.clear() 
def playGame():
    global tries
    while True:
        if(tries < 10):
            x = int(input('Enter a number between 0 and 100'))
            if (x<0 or x > 100):
                print("please enter only numbers between 0 and 10")
            else:
                if(x==n):
                   print("Congratulation your answer is correct")
                   saveResult("won")
                   playAgain();
               
                elif x in oldTries:
                   print(" you have tried this before")    
                elif(x>n):
                    print("a smaller number")
                    oldTries.append(x)
                    tries = tries+1
                elif(x<n):
                   print("a larger number")  
                   oldTries.append(x)  
                   tries = tries+1
        else:
                saveResult("lost")
                answer = input("do You Want to play again Y/N?")
                if(answer.lower() == "y"):
                    playAgain()
                else:
                    break 

        
def saveResult(resultMessage):
        print("file")
       
      
        here = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(here, 'result.txt')
        # f = open(filename, "x")
        f = open(filename, "a")
        f.writelines(resultMessage + "\n")
        f.close()

        
def getResults():
        here = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(here, 'result.txt')
        f=open(filename , "r")
        file_content = f.read()
        file_words = file_content.split()
       
        win = file_words.count('won')
      
        lost = file_words.count('lost')
      
        print(f"you won  {win} times and lost  {lost} times")

getResults()
playGame()        

        


    


