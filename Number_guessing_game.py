import random
range_limit = input("Enter the number for range:")

if range_limit.isdigit():
    range_limit = int(range_limit)
    
    if range_limit < 0:
        print("Enter the Number above Zero next time")
        quit()
else:
    print("Please enter number next time") 
   
random_number = random.randint(0,int(range_limit))
random_number = int(random_number)

guesses = 0

while True:
    guessed_number = input("Enter Your Guessed Number: ")
    guessed_number = int(guessed_number)
    
    guesses += 1
    
    if guessed_number == random_number:
        print("You Guessed Correctly")
        break
    elif guessed_number > random_number:
        print("you are abvove the number")
    else: 
        print("You Are below the number")
        
print("You guessed the number in",guesses, "times")