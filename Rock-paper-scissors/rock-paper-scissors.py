#score
computer_score = 0
player_score = 0
again_question = 'yes'

# define computer move
options = ['rock', 'paper', 'scissors']
import random

def play_function(computer_score, player_score):
    computer_move = random.sample(options, 1).pop()
    
    #ask for player move and validate it
    player_move = input('Enter your move (rock, paper or scissors): ')
    while not player_move in options:
        player_move = input('Sorry, didn\'t get that. Please enter your move and check the spelling (rock, paper or scissors): ')
    
    # play = [computer_move, player_move]
    play = []
    play.append(computer_move)
    play.append(player_move.lower())

    #define winner move. if tie, define final statement too
    if play[0] == play[1]:
        winner_move = 'tie'
        winner = 'tie'
        winner_statement = 'You and the computer went with {computer_move}. It\'s a tie!\nScore is computer {computer_score} x {player_score} you.'
    if play[0] != play[1]:
        if ('rock' in play) and ('scissors' in play):
            winner_move = 'rock'
        if ('paper' in play) and ('scissors' in play):
            winner_move = 'scissors'
        if ('rock' in play) and ('paper' in play):
            winner_move = 'paper'

    #define winner and final statement
    if winner_move != 'tie':
        if play.index(winner_move) == 0:
            winner = 'computer'
            computer_score += 1
            winner_statement = 'You went with {player_move} and the computer went with {computer_move}. Computer wins!\nScore is computer {computer_score} x {player_score} you.'
        if play.index(winner_move) == 1:
            winner = 'player'
            player_score += 1
            winner_statement = 'You went with {player_move} and the computer went with {computer_move}. You win!\nScore is computer {computer_score} x {player_score} you.'
    print(winner_statement.format(player_move=player_move, computer_move=computer_move, computer_score=computer_score, player_score=player_score))
    
    #ask if the player wants to play again
    again_question = input('Play again? (yes or no): ')
    while again_question != 'yes' and again_question != 'no':
        again_question = input('Sorry, didn\'t get that. Please enter yes or no. Play again? ')
    if again_question.lower() == 'yes':
        play_function(computer_score, player_score)
    if again_question.lower() == 'no':
        print('Alrighty, later!')
        exit()
        
print('This is \'Rock, Paper, Scissors game!\' Players are you and the computer. Let\'s start!')
play_function(computer_score, player_score)