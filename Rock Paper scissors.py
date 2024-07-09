import random 
import math

def play():
    user = input("What's your choice? 'r' is for rock, 's' is for scissors, 'p' is for paper/n ")
    user = user.lower()

    list1=['r', 's', 'p']
    b=random.randint(0,2)
    computer = list1[b]

     #b > c, a > b, c > a
    if user == list1[b]:
        return (0, user,list1[b])

     #b > c, a > b, c > a
    if is_win(user, list1[b]):
        return (1, user, list1[b])

    return (-1, user, list1[b])
        
def is_win(player, opponent):
    # return true player beats opponent
    # winning conditions: b > c, a > b, c > a
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):#
    # plays against computer until somebody wins best of n the game
    # to win you must win ceil(n/2) games i.e (2/3, 3/5, 4/7)
    player_wins = 0 
    computer_wins = 0
    wins_necessary = math.ceil(n/2)    
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        #tie
        if result == 0:
            print('its a tie. You and the computer have both chosen {}. /n'.format(user))
        # you win
        elif result == 1:
            player_wins +=1
            print("You chose {} and computer has chose {}. Congrats You Won!/n".format(user, computer))
        else:
            computer_wins +=1
            print("You chose {} and the computer chose {}. Sorry You Lost!:/n".format(computer, user))
        print('/n')

    if player_wins > computer_wins:
        print('You have Won best of {} games! What a Champ :)'.format(n))
    else:
        print('Unfortunatly, the computer has Won best out of {} games! Better Luck Next time'.format(n))


if __name__ == '__main__':
   play_best_of(3) #2
   play_best_of(9) #5