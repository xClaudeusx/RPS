import random
def rps():
    
    user_score = 0
    cpu_score = 0
    choices = ["rock", "paper", "scissors"]
    active = True

    while active:
        if(user_score == 4 or cpu_score == 4):
            break

        cpu_choice = random.choice(choices)
        user_choice = input('\nChoose between "Rock", "Paper", or "Scissors": ').lower()

        if(user_choice not in choices):
            print('Please Choose Between "Rock", "Paper", or "Scissors" Only\n')
        elif user_choice == "rock" and cpu_choice == "paper":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nCPU WON !\n")
            cpu_score += 1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        elif user_choice == "rock" and cpu_choice == "scissors":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nYOU WON !\n")
            user_score += 1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        elif user_choice == "paper" and cpu_choice == "rock":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nYOU WON !\n")
            user_score += 1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        elif user_choice == "paper" and cpu_choice == "scissors":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nCPU WON !\n")
            cpu_score +=1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        elif user_choice == "scissors" and cpu_choice == "paper":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nYOU WON !\n")
            user_score += 1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        elif user_choice == "scissors" and cpu_choice == "rock":
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice} \nCPU WON !\n")
            cpu_score += 1
            print(f"CPU Score: {cpu_score} \nYour Score: {user_score}\n")
        else:
            print(f"\nCPU has chosen {cpu_choice} & You have chosen {user_choice}\nIt IS A TIE ! \nCPU Score: {cpu_score} \nYour Score: {user_score}\n")


if __name__ == '__main__':
    rps()

        



