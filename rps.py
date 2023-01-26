import random

#Utility Function to Convert Letters into a Full Word
def util(letter):
    if letter == 'R':
        return "Rock"
    elif letter == 'P':
        return "Paper"
    else:
        return "Scissors"

#Checks if User Won!
def is_win(user, comp):
    if user == 'R' and comp == 'S' or user == 'P' and comp == 'R' or  user == 'S' and comp == 'P':
        return True

#Main Play Function!
def play():
    print("-- ROCK, PAPER, SCISSORS --")

    user_input = input("ENTER: \nR for Rock \nS for Scissors\nP for Paper\nChoice: ").capitalize()
    computer = random.choice(['R', 'P', 'S'])

#Only Checks if the game is a Draw or User has Won! Otherwise, Computer Wins Automatically
    if user_input == computer:
        print(f"User Entered {util(user_input)}\nComputer Chose {util(computer)}")
        print("Draw")
    elif is_win(user_input, computer):
        print(f"User Entered {util(user_input)}\nComputer Chose {util(computer)}")
        print("User Wins!")
    
    elif not(is_win(user_input, computer)):
        print(f"User Entered {util(user_input)}\nComputer Chose {util(computer)}")
        print("Computer Wins!")

    else:
        print("Wrong Input!")

choice = 'A'
while choice !='E':
    if choice == 'A':
        play()
    
    else:
        print('Wrong Input!')
    choice = input('\nENTER: \tA - Play Again \n\tE - Exit\nSelect: ').capitalize()