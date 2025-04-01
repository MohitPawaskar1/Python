from random import randint

computer = randint(1, 100)  # Random number between 1-100

n = -1
guesses = 0

while n != computer:
    try:
        n = int(input("Enter a number: "))
        guesses += 1  # Increase attempt count
        
        if n > computer:
            print("Enter a smaller number")
        elif n < computer:
            print("Enter a bigger number")
        else:
            print(f"🎉 You guessed it in {guesses} attempts!")
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")
