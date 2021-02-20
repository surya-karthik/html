import random

print('Hello,what is your name?')
name=input()

print('well, '+name +' I am thinking of a number between 1 and 20')
secretNumber= random.randint(1,20)

for guessestaken in range(1,7):
    print('Take a guess')
    guess=int(input())
      
    if guess<secretNumber:
        print('your guess is too low')
    elif guess>secretNumber:
        print('your guess is too high')
    else:
        break
if guess==secretNumber:
    print('good job'+name+'! you guessed my number in'+str(guessestaken)+'guesses') 
else:
    print('nope.The number i was thinking of was '+str(secretNumber))
