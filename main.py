print('Welcome to this amazing quiz game!')
points = 0

while True:
    want_to_play = input('Are you ready to play? ').lower()

    if want_to_play == 'yes':
        print("Great! Let's get started.")
        break
    elif want_to_play == 'no':
        print("Okay, maybe next time!")
        quit()
    else:
        print("I did not understand.")

# Question 1
question_one_answer = input('What is the capital city of France? ').capitalize()

if question_one_answer == 'Paris':
    print('Correct 👏')
    points += 1
else:
    print('Incorrect 🤡')

# Question 2
question_two_answer = input('What is the largest planet in our solar system? ').capitalize()

if question_two_answer == 'Jupiter':
    print('Correct 👏')
    points += 1
else:
    print('Incorrect 🤡')

# Question 3
question_three_answer = input('In what year did the Titanic sink? ').capitalize()

if question_three_answer == '1912':
    print('Correct 👏')
    points += 1
else:
    print('Incorrect 🤡')

# Question 4
question_four_answer = input('Who painted the Mona Lisa? ').capitalize()

if question_four_answer == 'Leonardo da Vinci':
    print('Correct 👏')
    points += 1
else:
    print('Incorrect 🤡')

# Question 5
question_five_answer = input('Who discovered penicillin? ').capitalize()

if question_five_answer == 'Alexander Fleming':
    print('Correct 👏')
    points += 1
else:
    print('Incorrect 🤡')


print(f'Total points: {points} / 5 ⭐')
