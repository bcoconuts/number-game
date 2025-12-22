import random

def get_game_size():
    int(input("How big a boy are ya... Pick a number (10-100): "))
    return


def guessing_game(game_size):
    random_number = random.randint(1, game_size)
    guess = int(input(f"Let's Play. pick a number between 1 and {game_size}: "))
    attempts = 0
    while guess != random_number:
        if not (1 <= guess <= game_size):
            print("Sawbones! Come checck this guy's brain...\n")
        elif guess < random_number:
            print(f"Yeah, you wish it was {guess}. Try something higher!\n")
        elif guess > random_number:
            print(f"Yeha, you wish it was {guess}. Try something lower!\n")
        
        attempts += 1    
        guess = int(input("Guess Again: "))
        
        return attempts
        

def results(attempts):       
    if attempts == 1:
        print(f"""You might be the best guesser this side of the Mississippi. 
        You guessed right on the first try!!!""")        
    elif (2 <= attempts <= (game_size//2)):
        print(f"""Better luck next time partner.
        You guessed right, but damn... it took you {attempts} tries.""")
    elif ((game_size//2) <= attempts <= (game_size//1)):
        print(f"""Even a blind squirrel finds an acorn now and again....
        Congrats on guessing {random_number} {attempts} tries...""")        
    
game_size = get_game_size()    
attempts = guessing_game(game_size)
results(attempts)
