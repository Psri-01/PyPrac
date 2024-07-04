#print('Project - Trading game simulation / pseudo code')
# replace 2 marbles 1 green with a black 10x winner marble, 1 red with a 5x white loser marble
import random
bag = ('green','green','green','green','green','black','red','red','red','white')
# green marble win same amount you bet, red marble lose the amount you bet
# marbles replaced into bag after each round
#starting amount of money
purse_gold = 1000
#current money amount
purse = purse_gold
#result of last round
result = 0
#how many rounds
rounds = 3
# game over if you lose half of your money
#last marble
marble = 'none'
#create a bag with 10 marbles

#welcome user to game
print(f'You are starting out with {purse_gold} gold.')
#loop drawing marbles
for draw in range(1, rounds+1):
    #how much was bet
    bet = int(input(f'Current purse: {purse}, Last draw: {marble} \nRound: {draw} - How much will you bet?'))
    #draw marble
    marble = random.choice(bag)
    #win or loss
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10*bet
    elif marble == 'white':
        result = -5*bet
    else:
        result = -bet
    #calc win or loss/ result and new amount/purse
    purse += result
    #lose game if lose half of money
    if purse < (purse_gold)*0.5:
        print('Game over!')
        break
    #print results
    print(f'Purse: {purse}, Last result: {marble}:{result}')
#print final results
print(f'Starting and ending gold: {purse_gold}/{purse}')
print('Gain/Loss: ', ((purse-purse_gold)/purse_gold *100),'%')
