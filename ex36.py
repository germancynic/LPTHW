import time

name = raw_input("What is your name? ")

print "Hello, " + name, "let us play hangman!"

print ""

time.sleep(1)

print "Choosing a word..."
time.sleep(0.5)

import random

WORDS = ["icecream", "surprise", "television", "computer", "bedroom", "colleague", "doctor"]

word = random.choice(WORDS)

guesses = ''

turns = 10

while turns > 0:         

    failed = 0             
   
    for char in word:      

        if char in guesses:    
    
            print char,    

        else:
    
            print "_",     

            failed += 1    

    if failed == 0:        
        print "Congratulations! You have won."  

        break              

    print

    guess = raw_input("guess a character:") 

    guesses += guess                    

    if guess not in word:  
 
        turns -= 1        
 
        print "Wrong"    
 
        print "You have", + turns, 'more guesses' 
 
        if turns == 0:           
    
            print "Sorry, you lose."
            print "the word was:"
            print(word)