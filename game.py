import random

# user inputs a number
top_range = input("type of number: ")
# checks whether the input is a number
# print(top_range.isdigit())

if top_range.isdigit():
    top_range = int(top_range)
    # checks whether the number is larger than 0
    if top_range <= 0:
        print("please input a number that is larger than 0")
        quit()
else:
    print("please input a number")
    quit()

random_number = random.randint(0, top_range)
# print(random_number)

#how many times a user makes a guess
guesses = 0


while True:
    #every time a user makes a guess(start the loop) we increment +=1
    guesses +=1
    user_guess =input("make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please input a number")
        #use continue keyword it brings us back to the top of the loop
        continue
    if user_guess ==random_number:
        print("you got it")
        break
    else:
        #checks whether the user was greater or lower than the number
        if user_guess > random_number:
            print("you were above the number")
        else:
            print("You were below the number")    
        # print("you got it wrong")            
print("you got it in" ,guesses ,"guesses")        