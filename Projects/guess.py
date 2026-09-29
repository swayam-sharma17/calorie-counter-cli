import random
while True:
    secret_number=random.randint(1,100)
    attempts=0



    while True:
        guess=int(input("Guess a number between 1 and 100: "))
        attempts +=1 
        if(attempts>6):
            print("Game Over!")
            break
        elif(guess==secret_number):
            print("You got it in " +str(attempts)+ " guesses!")
            break
        elif guess<secret_number:
            print("The number is a bit bigger!")
        else :
            print("The number is a bit smaller!")
        

    play=str(input("Do you want to play again? Y/N: "))
    
    if(play.upper()=='Y'):
        print("Play Again!")

    elif(play.upper()=='N'):
        print("Goodbye!")
        break

    else:
        print("Error!")
        break        

    