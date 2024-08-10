import random
target = random.randint(1,100)
while True:
    user_choice = input("Guess the tarrget or Quit : ")
    if user_choice == "Quit":
        print("YOU LOSS . \n becouse you Quit the game ....")
        break
    user_choice= int(user_choice)
    if user_choice < target:
        print("Your guess is too small, guess bigger number.")
    elif user_choice > target:
        print("Your guess is too big , guess a small number .")
    else:
        print("Congrats ....your guess is Right.\nYOU WON.")
        break
