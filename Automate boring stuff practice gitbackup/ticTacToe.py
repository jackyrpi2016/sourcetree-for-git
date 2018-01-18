# tic tac toe game
# can I use miniMax instead of enumerating it????
'''
x 1st, o 2nd

1. board: position, 'x' or 'o'
2. print board: refresh board
3. check winner
4. no winner, must end
'''
board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('------')

def checkWinner(board):
    # enumerate all 8 winning conditions
    # row win
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ' or \
       board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ' or \
       board['low-L'] == board['low-M'] == board['low-R'] != ' ':
        return 1
    # column win
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ' or \
         board['top-M'] == board['mid-M'] == board['low-M'] != ' ' or \
         board['top-R'] == board['mid-R'] == board['low-R'] != ' ':
        return 1
    # diagonal win
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ' or \
         board['low-L'] == board['mid-M'] == board['top-R'] != ' ':
        return 1
    else:
        return 0

print('choose symbol for 1st Player: x or o')
sym = input()

for game in range(9):
    # automatic switch
    if game != 0:
        if sym == 'x':
            sym = 'o'
        else:
            sym = 'x'    
    print()
    print()     
    print('''Select a place to put your symbol: \n\t top-L, top-M, top-R \n\t mid-L, mid-M, mid-R \n\t low-L, low-M, low-R''')
    pos = input()
    print()
    print()
    board[pos] = sym
    printBoard(board)
    if game >= 4:
        if checkWinner(board):
            print('win')
            break;
    if game == 8:
        print('tie')
    
