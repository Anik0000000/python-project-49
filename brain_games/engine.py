def run_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)

    for _ in range(3):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            error_msg = (
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
            )
            print(error_msg)
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")