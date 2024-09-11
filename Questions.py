import random
import colorama
from colorama import Fore

def check_height_condition(height):
    if height < 160:
        return "You drown."
    elif height > 180:
        return "The tiger has found you and you're dead."
    else:
        return "Safe to cross."

def check_fruit_answer(user_answer, correct_fruits):
    user_fruits = set(fruit.strip().lower() for fruit in user_answer.split(','))
    correct_fruits_set = set(fruit.strip().lower() for fruit in correct_fruits.split(','))
    return user_fruits == correct_fruits_set
random_numbers = [random.randint(1, 10) for _ in range(4)]
questions_and_answers = [
    (f"{Fore.BLUE}You went to the wild forest and met a monkey! The monkey asked you to guess the five fruits that the monkey likes.", 
     "Apple, Banana, Orange, Dragon fruit, Pear", 'fruit'),
    (f"{Fore.RED}There is a hungry tiger, and the only way out is the nearest path that requires you to cross a river. "
     "Enter your height; if you are too short, you will drown, and if you are too tall, you will be easily spotted and hunted down.", 
     "height", 'height'),
    (f"{Fore.GREEN}There is a door that requires a password to unlock; it is a series of four numbers.", 
     ''.join(map(str, random_numbers)), 'password')
]

selected_questions = random.sample(questions_and_answers, 3)
random.shuffle(selected_questions)

for i, (question, answer, qtype) in enumerate(selected_questions, 1):
    print(f"Question {i}: {question}")

    if qtype == 'height':
        try:
            user_height = int(input("Enter your height in cm: "))  
            response = check_height_condition(user_height) 
            print(f"Answer {i}: {response}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif qtype == 'password':
        user_password = input("Enter the 4-number password: ")
        if user_password == answer:
            print("Correct! The door unlocks.")
        else:
            print(f"Incorrect. The correct password was: {answer}.")
    
    elif qtype == 'fruit':
        user_answer = input("Enter your answer (comma-separated): ")
        if check_fruit_answer(user_answer, answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was: {answer}.")
#Not finished
