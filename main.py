'''Themed number-guessing game'''

MIN_GAME_SIZE = 10
MAX_GAME_SIZE = 100


import random


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
                    print("Sawbones! Come checck this guy's brain...\n")
                elif guess < random_number:
                    print(f"Yeah, you wish it was {guess}. Try something higher!\n")
                else:
                    print(f"Yeha, you wish it was {guess}. Try something lower!\n")
                
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
    
    
def main():
    """Run the game"""
    game_size, difficulty = get_game_settings()
    random_number, attempts = play_guessing_game(game_size)
    display_results(game_size, random_number, attempts, difficulty)
    
    
if __name__ == "__main__":
    main()
