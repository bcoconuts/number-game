'''Themed number-guessing game'''

import random

MIN_GAME_SIZE = 10
MAX_GAME_SIZE = 100


def get_game_settings():
    """ Prompt user to select game size"""
    while True:
        try:
            size = int(input(f"How big a boy are ya... Pick a number ({MIN_GAME_SIZE}-{MAX_GAME_SIZE}): "))
            while True:
                if (MIN_GAME_SIZE <= size <= MAX_GAME_SIZE//3):
                    print(f"{size}?? I've seen bigger men come out of a womb!\n")
                    difficulty = "easy"
                    break
                elif (MAX_GAME_SIZE//3 <= size <= MAX_GAME_SIZE//2):
                    print(f"{size}... You aint special. I've faced down bigger men.\n")
                    difficulty = "medium"
                    break 
                elif (MAX_GAME_SIZE//2 <= size <= MAX_GAME_SIZE):
                    print(f"{size}!! Looks like we're gonna find out if this towns big enough for the both of us.\n")
                    difficulty = "hard"
                    break                
                elif size > MAX_GAME_SIZE:
                    print(f"Ha! I Bet you wish you had {size} notches on you gun. Let's try again\n")
                else:
                    print("Whats the matter? Scared?\n")
                    
                size = int(input(f"Now, how big a boy are ya... Pick a number ({MIN_GAME_SIZE}-{MAX_GAME_SIZE}): "))
            break
        except ValueError:
            print("Whats the matter boy? Momma didn't raise you right? Lets try that again.\n")
    
    return size, difficulty


def play_guessing_game(game_size):
    """
    Run the main guessing game loop
    
    Returns: 
        tuple: The random number and number of attempts.
    """
    attempts = 1
    random_number = random.randint(1, game_size)
    while True:
        try:
            guess = int(input(f"Let's Play. pick a number between 1 and {game_size}: "))
            while True:
                if guess == random_number:
                    break
                elif not (1 <= guess <= game_size):
                    print("Sawbones! Come check this guy's brain...\n")
                elif guess < random_number:
                    print(f"{guess}!? That guess was lower than you, Little man!\n")
                else:
                    print(f'''{guess}? When they said "Hang em' High", they werent talking about your guesses.\n''')
                
                attempts += 1 
                
                while True:
                    try:
                        guess = int(input("Guess Again: "))
                        break
                    except ValueError: 
                        print("I'm gonna say it again. Slower for you this time.\n")
                        attempts += 1  
            break
        except ValueError:
            print("I'm gonna say it again. Slower for you this time.\n")
            attempts += 1
        
    print("\n")    
    return random_number, attempts
        

def display_results(game_size, random_number, attempts, difficulty):
    """Display results based on player performance"""
    if attempts == 1 and difficulty != "easy":
        print(
            "You might be the best guesser this side of the Mississippi! "
            "Guess I'll be moving on from town now!"
        )
    elif attempts == 1 and difficulty == "easy":
        print("Not bad, Little man.")
    elif attempts == 2 and difficulty != "easy":
        print(
            "Well I'll be... Not too bad!"
            "You got me on the second try!!!"
        )
    elif attempts == 2 and difficulty == "easy":
        print("Might make a killer out of you yet, boy")
    elif (3 <= attempts <= (game_size//2)):
        print(
            "There are two kinds of people in this world: The Quick and the Dead.\n"
            "You guessed right, "
            f"but it took you {attempts} tries. "
            "Guess which group you belong to..."
        )
    elif (game_size//2) <= attempts:
        print(
            "Even a blind squirrel finds an acorn now and again.... "
            f"Congrats on guessing {random_number} in... *looks at notes* {attempts} tries..."
        )        
    
def prompt_play_again():
    '''Determine if player wants to play again, and add to game tally''' 
    while True:
        try:
            while True:
                run_game = int(input("Think you got what it takes to try your hand again?\n(0 to Quit, 1 to Play): "))
                if run_game == 0:
                    break
                elif run_game == 1:
                    print("\n I'll be your Huckleberry.\n")
                    break
                else:
                    print("I'm gonna say it again. Slower for you this time.\n")
            break
        except ValueError:
            print("I'm gonna say it again. Slower for you this time.\n")
    
    return run_game
    

def display_game_stats(total_attempts):
    '''Calculate and display game statistics'''
    average = round(sum(total_attempts) / len(total_attempts), 2)
    if len(total_attempts) == 1:
        print("Here's the part where I'd give you how you did... But all ya did was play once")
    else:
        print(
            f"Well cowboy, over {len(total_attempts)} games,\n"
            f"looks like it took you an average of {average} guesses."
        )    
    
def main():
    """Run the game"""
    run_game = 1
    total_attempts = []
    while run_game == 1:
        game_size, difficulty = get_game_settings()
        random_number, attempts = play_guessing_game(game_size)
        total_attempts.append(attempts)
        display_results(game_size, random_number, attempts, difficulty)
        run_game = prompt_play_again()
    display_game_stats(total_attempts)
        
    
if __name__ == "__main__":
    main()
