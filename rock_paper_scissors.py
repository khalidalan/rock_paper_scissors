import random

# ASCII art for Rock, Paper, Scissors
ascii_art = {
    'r': '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    'p': '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    's': '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

def get_user_choice():
    """Asks the player to choose rock, paper, or scissors."""
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    while True:
        user_input = input("Make your move: 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
        if user_input in choices:
            return user_input, choices[user_input]
        else:
            print("Invalid choice, please try again.")

def get_pc_choice(user_choice):
    """Selects the PC's choice, making it win 90% of the time."""
    winning_moves = {'r': 'p', 'p': 's', 's': 'r'}  # What beats the player's move
    choices = ['r', 'p', 's']

    # 90% chance PC will choose the winning move, 10% chance for random move
    if random.random() < 0.9:
        return winning_moves[user_choice], ascii_art[winning_moves[user_choice]]
    else:
        random_choice = random.choice(choices)
        return random_choice, ascii_art[random_choice]

def determine_winner(user, pc):
    """Determines the winner between the user and the PC."""
    if user == pc:
        return "It's a tie!"
    elif (user == 'p' and pc == 'r') or (user == 'r' and pc == 's') or (user == 's' and pc == 'p'):
        return "You won!"
    else:
        return "PC wins! You lose."

def play_game():
    """Starts the Rock-Paper-Scissors game with ASCII art."""
    print("Welcome to the Rock-Paper-Scissors game!")
    
    while True:
        user, user_choice = get_user_choice()
        pc, pc_art = get_pc_choice(user)

        print(f"\nYou played: {user_choice}")
        print(ascii_art[user])
        print(f"PC played: {pc}")
        print(pc_art)

        result = determine_winner(user, pc)
        print(result)
        
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
play_game()
