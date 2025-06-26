import random
import time
import os

def clear_screen():
    # Works on Windows and Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def dice_animation():
    animation = ['Rolling.', 'Rolling..', 'Rolling...']
    for frame in animation:
        clear_screen()
        print(frame)
        time.sleep(0.4)

def roll_die():
    return random.randint(1, 6)

def main():
    while True:
        user_input=input("Press Enter to roll the die (or type 'q' and press Enter to quit): ")
        if 'q' in user_input:
            break
        dice_animation()
        result = roll_die()
        print(f"\n🎲 You rolled a {result}!\n")
        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
