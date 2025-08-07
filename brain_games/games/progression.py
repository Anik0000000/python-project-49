import random

RULES = 'What number is missing in the progression?'

def generate_progression(start, step, length):
    return [str(start + i * step) for i in range(length)]

def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)
    
    progression = generate_progression(start, step, length)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer