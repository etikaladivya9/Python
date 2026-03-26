import random

num = random.randint(1, 20)
score = 20

for i in range(1,5):
    if score>0:
        guess = int(input("Enter a number between 1-20: "))
        if guess == num:
            print("Correct Guess!")
            print("Score:", score)
            break
        else:
            score -= 5
            print('try again!..')
else:
    print(f'You lost the game the num is {num} ')        
        