import random
def nim_game():
    print("\n=== NIM GAME ===")
    print("Take 1-3 sticks per turn. Taking the last stick wins!")
    # Set up game
    sticks = random.randint(10, 15)
    current_player = random.choice(["player", "computer"])
    print(f"Starting with {sticks} sticks. {'You' if current_player == 'player' else 'Computer'} go first.")
    # Game loop
    while sticks > 0:
        print(f"\nSticks left: {sticks}")
        if current_player == "computer":
            # Simple optimal strategy
            remainder = sticks % 4
            move = remainder if remainder in [1, 2, 3] else 1
            print(f"Computer takes {move} stick(s)")
            sticks -= move
            if sticks == 0:
                print("\nComputer wins!")
                return False
            current_player = "player"
        else:
            # Player's move
            try:
                move = int(input("Your turn! Take 1, 2, or 3 sticks: "))
                if move < 1 or move > 3 or move > sticks:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue
            sticks -= move
            if sticks == 0:
                print("\nYou win!")
                return True
            current_player = "computer"
# Start the game
if __name__ == "__main__":
    while True:
        nim_game()
        if input("Play again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")