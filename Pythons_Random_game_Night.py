import random

game = ['basketball', 'baseball', 'football', 'soccer', 'tennis', 'cricket']

while True:
    my_choice = input(game)
    computer = random.choice(game)
    print('computer chose:', computer)
    win = input('did you select the correct sport? yes or no ')
    if win == 'yes':
        print('wow you actually won! :o')
        print(my_choice, 'equals', computer)



