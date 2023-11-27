def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def getBoardCopy(board):
    return board[:]

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getComputerMove(board):
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if copy[i] == ' ':
            copy[i] = 'O'
            if isWinner(copy, 'O'):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if copy[i] == ' ':
            copy[i] = 'X'
            if isWinner(copy, 'X'):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if board[5] == ' ':
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter

def playGame(board):
    turn = 'player'
    while True:
        drawBoard(theBoard)
        move = getComputerMove(theBoard) if turn == 'computer' else getPlayerMove(theBoard)
        makeMove(theBoard, 'X' if turn == 'player' else 'O', move)
        if isWinner(theBoard, 'X'):
            drawBoard(theBoard)
            print('Hooray! The computer has won the game!')
            break
        elif isWinner(theBoard, 'O'):
            drawBoard(theBoard)
            print('Hooray! You have won the game!')
            break
        elif ' ' not in theBoard:
            drawBoard(theBoard)
            print('The game is a tie!')
            break
        turn = 'computer' if turn == 'player' else 'player'

theBoard = [' '] * 10
playGame(theBoard)