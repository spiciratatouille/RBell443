#Program 3
#Due: 03/28/2021 11:59PM
#CIS 443-75-4212
#Grading ID: P5279
import random


def roll_dice():
    
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)  # pack die face values into a tuple

def play_craps():
#roll dice and find the sum    
    roll = roll_dice()
    roll_sum = sum(roll)
    attempts = 1
    if roll_sum in (7, 11):  # win
        outcome = 'Win'
        return outcome,1,roll_sum
    elif roll_sum in (2, 3, 12):  # lose
        outcome = 'Loss'
        return outcome,1,roll_sum
    else:  # remember point        
        my_point = roll_sum
        while True:
            roll = roll_dice()
            roll_sum = sum(roll)
            attempts += 1
            if roll_sum == my_point:
                outcome = 'Win'
                return outcome,attempts,roll_sum
            elif roll_sum == 7:
                outcome = 'Loss'
                return outcome,attempts,roll_sum
            else:
                continue 

#play craps a million times and output the stats
def play_mil_times():
    rolls = [0]*25
    wins = {}
    losses = {}
    games = 1000000
#step through each roll of the dice
    for i in range(games):
        outcome, attempts,roll_sum = play_craps()
#add wins to dictionary for each roll, or add new roll
        if outcome == 'Win':
            if roll_sum in wins:
                wins[roll_sum] += 1
            else:
                wins[roll_sum] = 1
#add losses to dictionary for each roll, or add new roll        
        elif outcome == 'Loss':
            if roll_sum in losses:
                losses[roll_sum] += 1
            else:
                losses[roll_sum] = 1
        if attempts <= len(rolls):
            rolls[attempts-1] += 1
        else:
            rolls[-1] += 1

#summarize number of wins and losses
    sum_wins = sum(wins.values())
    sum_losses = sum(losses.values())
    first_header = '% Resolved'
    second_header = 'Cumulative %'
    first = 'Rolls'
    second = 'on this roll'
    third = 'of games resolved'
#print output headers
    print(f'Percentage of wins: {(sum_wins*100/(games)):.2f}%')
    print(f'Percentage of losses: {(sum_losses*100/(games)):.2f}%')
    print('Percentage of wins/losses based on total number of rolls')
    print()
    print(f' {first_header:>25} {second_header:>20} ')
    print(f' {first:<5}{second:>20} {third:>20}')
#print output data
    for i in range(len(rolls)):
        p_res = 100*(rolls[i]/games)
        c_res = 100*(sum(rolls[0:i])/games)
        num = i+1
        if i != len(rolls) - 1:
            print(f'{num:>5}{p_res:>19.2f}%{c_res:>19.2f}%')
        else:
            total_res = 100*(sum(rolls)/games)
            print(f'{num:>5}{p_res:>19.2}%{total_res:>19}%')
#initialize the program        
play_mil_times()