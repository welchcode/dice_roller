import random

#initial user prompt, number takes on value of user input
print("Would you like to roll 1 or 2 dice?")
number = int(input())

#if user inputs "1" this if runs
if number == 1:
    print('Please enter "roll" to roll die, or "quit" to stop program')
    user_input = input()

    # as long as input does not == quit or Quit, while loop will continue
    while user_input != "quit" and "Quit":
        for x in range(1):
            print("Your dice number is " , random.randint(1,6))
        print('Please enter "roll" to roll dice')
        user_input = input()
    print("Program has ended")

#if user inputs "2" this if runs
elif number == 2:
    print('Please enter "roll" to roll dice, or "quit" to stop program')
    user_input = input()

    #as long as input does not == quit or Quit, while loop will continue
    while user_input != "quit" and "Quit":
        for x in range(1,12):
            # 2 - 12 bc 2 dice requires at least the digits 2-12
            print("Your dice number is ", random.randint(2,12))
            print('Please enter "roll" to roll dice')
            user_input = input()
    print("Program has ended")

#if user inputs anything other than a "1" or "2"
else:
    print("Not a valid input, please restart program")
