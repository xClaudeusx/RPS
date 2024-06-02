# Rock, Paper, Scissors Application

This project is a very simple Rock Paper Scissors game played as a best of 7, 
created to familiarize one's self with some basic programming logic and 
python fundamentals. The following steps were used:

* Create variables to store and track CPU and Player score
* Create a list of choices (Rock, Paper Scissors) for cpu to choose from
* Create a condition for while loop to run
* Create a while loop for state of the game
* If CPU or Player score reaches 4 game ends
* Prompt player to select from choices
* Compare CPU to Player choices and score accordingly

## Short Sample
```python
import random # for cpu to randomly select from choices

while active:
        if(user_score == 4 or cpu_score == 4): # ends game if either player reaches 4
            break

        cpu_choice = random.choice(choices) # for cpu to randomly select from choices
        user_choice = input('\nChoose between "Rock", "Paper", or "Scissors": ').lower() # stores player choice in a variable

        if(user_choice not in choices): # accounts for incorrect user input
            print('Please Choose Between "Rock", "Paper", or "Scissors" Only\n')
```

## Additional Notes
... My first project and ReadMe file ...




