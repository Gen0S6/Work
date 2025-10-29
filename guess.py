import random

def play(min_n=1, max_n=100, max_attempts=7):
    secret = random.randint(min_n, max_n)
    attempts = 0
    print(f"Guess the number between {min_n} and {max_n}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        raw = input(f"Attempt {attempts+1}/{max_attempts} → Your guess: ")
        try:
            guess = int(raw)
        except ValueError:
            print("Invalid input. Enter an integer.")
            continue

        if guess < min_n or guess > max_n:
            print(f"Out of range. Stay within [{min_n}, {max_n}].")
            continue

        attempts += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct. You win in {attempts} attempts.")
            return True

    print(f"You lose. The number was {secret}.")
    return False

if __name__ == "__main__":
    play()
