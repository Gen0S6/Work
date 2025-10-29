import random
import json
from pathlib import Path

HIGHSCORE_FILE = Path("highscore.json")

def load_highscore():
    if HIGHSCORE_FILE.exists():
        try:
            return json.loads(HIGHSCORE_FILE.read_text()).get("highscore", 0)
        except Exception:
            return 0
    return 0

def save_highscore(score):
    HIGHSCORE_FILE.write_text(json.dumps({"highscore": score}))


difficulty_levels={
    'easy': (100, 10),
    'medium': (500, 15),
    'hard': (1000, 25),
}

print("Welcome to the Guess the Number game!")



def Score(difficulty):
    print("Starting a new game...")

    max_number, max_attempts = difficulty_levels.get(difficulty, 'easy')
    secret_number = random.randint(0, max_number)
    attempts= 0


    print(f"You have {max_attempts} attempts to guess a number between 0 and {max_number}. Good Luck")

    while attempts < max_attempts:
        while True:
            try:
                raw = input(f"Guess the number between 0 and {max_number}: ")
                guess = int(raw)
                break
            except ValueError:
                print("Please enter a valid integer.")
                continue

        if 0 <= guess <= max_number:
            attempts += 1
            if guess < secret_number:
                print(f"Too low! This is your {attempts} attempt.")
            elif guess > secret_number:
                print(f"Too high! This is your {attempts} attempt.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                score = 1
                return score

            if attempts==max_attempts: 
                print(f"Sorry, you've used all your attempts. The number was {secret_number}.")
        else:
            print(f"Your guess is out of bounds.")
        




def Start_game() :
    high = load_highscore()
    print(f"(Current high score: {high})")
    total_score = 0 
    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in difficulty_levels:
            score = Score(difficulty)
            total_score += score 
        else:
            print("Invalid choice. Please select from easy, medium, or hard.")
            continue    
        if total_score > high:
            save_highscore(total_score)
            high = total_score
        while True:
            resart = input("Do you want to play again? (yes/no): ").lower() 
            if resart in ['yes','no']:
                if resart == 'yes':
                    break
                else :
                    print(f"Thank you for playing! Your score was {total_score}. Goodbye.")
                    if total_score > high:
                        print(f"New HIGH SCORE: {high}")    
                    return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                
    

if __name__=="__main__":
    Start_game()
