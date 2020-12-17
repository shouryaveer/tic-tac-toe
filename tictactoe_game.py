from tictactoe_player import HumanPlayer, ComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def printboard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def printboard_nums():
        # To give numbering to refer to each boxes in the board
        num_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all ([spot == letter for spot in row]):
            return True

        col_index = square % 3
        col = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals i.e. squares (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.printboard_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                game.printboard()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(1)
        
    if print_game:
        print("It's a tie!")

print("*********Welcome to Tic-Tac-Toe Game*********")
print("Who do wanna play with: ")
print("1. Random Computer(Easy)\n2. Genius Computer\n3. Human Player")
x = int(input("Choose your option(1-2-3): "))

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    if x == 1:
        o_player = ComputerPlayer('O')
    elif x == 2:
        o_player = GeniusComputerPlayer('O')
    else:
        o_player = HumanPlayer('O')
    play(TicTacToe(),x_player,o_player)
