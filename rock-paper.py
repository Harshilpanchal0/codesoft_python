import random 
def user_choice():
    print("/nChoose your option: Rock,paper,scissors")
    user_input = input("Enter your choice: ").lower()
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return user_choice()
    return user_input

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "its a tie "
    elif (user == "rock" and computer == "scissors"):
        return "You win! Rock crushes scissors."
    elif (user == "paper" and computer == "rock"):
        return "You win! Paper covers rock."
    elif (user == "scissors" and computer == "paper"):
        return "You win! Scissors cut paper."
    else:
        return "you Lose computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user = user_choice()
        computer = computer_choice()
        print(f"Computer chose: {computer}")
        print(f"Your choice: {user}")
        result = determine_winner(user, computer)
        print("Result:", result)
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

play_game()