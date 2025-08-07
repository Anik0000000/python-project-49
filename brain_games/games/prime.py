import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct_answer