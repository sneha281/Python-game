import random
lst = ['r','p','s']
chance = 3
no_of_chance = 0
computer_point = 0
human_point = 0
print("\t \t \t \t \t \t  Rock,Paper and Scissor Game by Sneha\n\n")
print("r for Rock\n p for Paper\n s for Scissor")

while no_of_chance<chance:
    _input = input('Rock ,Paper and Scissor Game  :' )
    _random = random.choice(lst)
    if _input == _random:
        print("computer aur aapne same choose kra hai try again")
     #if user enter r
    if _input == "r" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("aap haar gye \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif _input == "r" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("aap jeet gye \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
     #if user enter p
    elif _input == "p" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("aap jeet gye \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
    elif _input=="p" and _random== "r":
        computer_point = computer_point+1
        print(f"your guess{_input} and computer guess is {_random}\n")
        print("aap haar gye \ n")
        print(f"computer_point is {computer_point}and your point is {human_point}\n")
     #if user enter s
    elif _input == "s" and _random == "r":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("aap haar gye \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")
    elif _input == "s" and _random =="p":
        human_point = human_point + 1
        print(f"your guess{_input} and computer guess is {_random}\n")
        print("aap jeet gye \ n")
        print(f"computer_point is {computer_point}and your point is {human_point}\n")
    else:
        print("you have input wrong\n")


    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > human_point:
    print("aap haar gye")

if computer_point < human_point:
    print("aap jeet gye")

print(f"your point is {human_point} and computer point is {computer_point}")





