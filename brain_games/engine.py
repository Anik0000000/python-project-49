def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)

    for _ in range(3):
        question, correct_answer = game.generate_round()
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()  
        if game.__name__ == 'brain_games.games.calc':
            if not user_answer.lstrip('-').isdigit():
                print("❌ Please enter a number! Try again.")
                    continue
                break
                
        elif game.__name__ == 'brain_games.games.even':
            if user_answer.lower() not in ('yes', 'no'):
                print("❌ Please answer 'yes' or 'no'! Try again.")
                    continue
                break

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")  
            return

    print(f"Congratulations, {name}!")