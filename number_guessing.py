import random

# Generate a random number between 1–100
num = random.randint(1, 100)
tries = 0

print("\n-----------------------------------------------------------")
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.\n")

while True:
    print("-----------------------------------------------------------\n")
    user_input = input("Enter your guess: ")

    # Check if input is a number
    if not user_input.isdigit():
        print("Invalid input! Please enter a number only.\n")
        continue

    guessed = int(user_input)

    # Validate input range
    if guessed < 1 or guessed > 100:
        print("⚠ Please enter a number **between 1 and 100 only.**\n")
        continue

    tries += 1

    # Check guessing conditions
    if guessed == num:
        print("\n-----------------------------------------------------------")
        print(f"Congratulations! You guessed the correct number in {tries} tries.")
        print("-----------------------------------------------------------\n")
        break
    elif guessed > num:
        print("⬇ Too high! Try a smaller number.\n")
    else:
        print("⬆ Too low! Try a bigger number.\n")
