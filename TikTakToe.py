#Tik tak toe


board = {"Top-L":" ","Top-M":" ","Top-R":" ",
         "Mid-L":" ","Mid-M":" ","Mid-R":" ",
         "Low-L":" ","Low-M":" ","Low-R":" ",
         }

def printboard(ttt):
    print(ttt['Top-L'] +  " |" + ttt["Top-M"] + " |" + ttt["Top-R"])
    print("--+--+--")
    print(ttt["Mid-L"] + " |" + ttt["Mid-M"] + " |" + ttt["Mid-R"])
    print("--+--+--")
    print(ttt["Low-L"] + " |" + ttt["Low-M"] + " |" + ttt["Low-R"])

turn = 'X'

for i in range(9):
    printboard(board)
    move = input('Turn for ' + turn + '. Move on which space?: ')
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printboard(board)