from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input("place your bet on numbers between 1 to 10 : "))
        if guess > 0 and guess < 11:
            if guess == answer:
                print("you are a genius you win this bet $$$$$$")
                break
            # else:
            #     print("sorry man you lose the bet you should put it on number : ",answer)
            # break
        else:
            print("hee pal i said 1 to 10")
    except ValueError:
        print("enter a number not string you dumass")
        continue