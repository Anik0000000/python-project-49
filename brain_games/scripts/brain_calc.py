from brain_games.engine import run_game
from brain_games.games import calc

def main():
    run_game(calc)

if __name__ == '__main__':
    main()

try:
    user_answer = int(input("Your answer: "))
except ValueError:
    print("Please enter a number!")
    continue