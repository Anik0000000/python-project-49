import random

RULES = "What is the result of the expression?"


def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    match operator:
        case '+':
            correct_answer = str(a + b)
        case '-':
            correct_answer = str(a - b)
        case '*':
            correct_answer = str(a * b)
    
    question = f"{a} {operator} {b}"
    return question, correct_answer