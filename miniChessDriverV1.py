## miniChessDriver.py
## version 0.1
## March 1, 2017

## Here's the crude, unpolished first version of a user
## interface for your miniChess function

## It doesn't really know much about who wins the game
## or when...although it does know that if it can't make
## a move, the human player wins.

## It does not validate the coordinates for the move
## that is entered by the user.  You can move any pawn
## on either side to any square.  So be careful.

## your definitions for move_maker and
## move_chooser go up here in this space

##prog67.py
##Colton Juliano
##3/16/17
##
def move_maker(board,mycolor):
    import copy
    full_list=[]
    for row in range(len(board)):
        for col in range(len(board[row])):
            newlist=copy.deepcopy(board)
            if mycolor==2:
                if board[row][col]==1:
                    try:
                        if board[row+1][col-1]==2:
                            if col-1>=0:
                                full_list=takepawn_up_right(board,row,col,full_list)
                                pass
                    except IndexError:
                        pass
                    try:
                        if board[row+1][col+1]==2:
                            full_list=takepawn_up_left(board,row,col,full_list)
                            continue
                    except:
                        continue
                if newlist[row][col]==0:
                    try:
                        if board[row+1][col]==2:
                            full_list=moveup_forward(board,row,col,full_list)
                        continue
                    except:
                        continue
            if mycolor==1:
                if board[row][col]==2:
                    try:
                        if board[row-1][col-1]==1:
                            if col-1>=0:
                                full_list=takepawn_down_right(board,row,col,full_list)
                                pass
                    except IndexError:
                        pass
                    try:
                        if board[row-1][col+1]==1:
                           full_list=takepawn_down_left(board,row,col,full_list)
                        continue
                    except:
                        continue
                if board[row][col]==0:
                    try:
                        if board[row-1][col]==1:
                            full_list=movedown_forward(board,row,col,full_list)
                        continue
                    except:
                        continue
    return(full_list)

def takepawn_up_right(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=2
    newlist[row+1][col-1]=0
    full_list.append(newlist)
    return full_list
    
def takepawn_up_left(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=2
    newlist[row+1][col+1]=0
    full_list.append(newlist)
    return full_list

def moveup_forward(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=2
    newlist[row+1][col]=0
    full_list.append(newlist)
    return full_list

def takepawn_down_right(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=1
    newlist[row-1][col-1]=0
    full_list.append(newlist)
    return full_list

def takepawn_down_left(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=1
    newlist[row-1][col+1]=0
    full_list.append(newlist)
    return full_list

def movedown_forward(board,row,col,full_list):
    newlist=creategameboard(board)
    newlist[row][col]=1
    newlist[row-1][col]=0
    full_list.append(newlist)
    return full_list

def creategameboard(board):
    import copy
    newlist=copy.deepcopy(board)
    return newlist

def move_chooser(possiblemoves,mycolor):
    mymove=[]
    boardvalue=len(possiblemoves[0])*-1
    index=0
    badmoves=[]
    if mycolor==1:
        for move in possiblemoves:
            for pawn in move[len(move)-1]:
                if pawn==1:
                    return move##no point value because this is an autowin, and thus can be chosen w/o further investigation
            for pawn in move[0]:
                if pawn==2:
                    badmoves.append(move)##put losing moves in list badmoves
    if mycolor==2:
        for move in possiblemoves:
            for pawn in move[0]:
                if pawn==2:
                    return move##no point value because this is an autowin, and thus can be chosen w/o further investigation
            for pawn in move[len(move)-1]:
                if pawn==1:
                    badmoves.append(move)##put losing moves in list badmoves
    try:
        for bad in badmoves:
            possiblemoves.remove(bad)##try to remove losing moves from possible moves before continuing
    except:
        pass##if there are no losing moves to remove, pass
    for move in possiblemoves:
            boardpoints=0
            for row in move:
                rowpoints=0
                point=0
                lostpoint=0
                for pawn in row:
                    if pawn==mycolor:
                        point=point+1
                    if pawn==0:
                        pass
                    if pawn!=mycolor and pawn!=0:
                        lostpoint=lostpoint+1
                rowpoints=point-lostpoint
                boardpoints=boardpoints+rowpoints
            if boardpoints>=boardvalue:
                boardvalue=boardpoints
                mymove[:]=move
    return mymove



## below is what we supply ======================================


## print a board
## 0 prints as '-', 1 prints as 'w', 2 prints as 'b'

def printBoard(board):
    print("   ", end = "")
    for i in range(0, len(board[0])):
        print(str(i)+" ", end = "")

    print("\n")
    row = 0
    for r in board:
        print(row, " ", end = "")
        for c in r:
            if c == 1:
                print("w ", end = "")
            elif c == 2:
                print("b ", end = "")
            else:
                print("- ", end = "")
        print()
        row = row + 1
    print()

def makeInitBoard(dim):
    board = []
    for i in range(0,dim):
        row = []
        for j in range(0,dim):
            row.append(0)
        board.append(row)

    for i in range(0,dim):
        board[0][i] = 1
        board[dim - 1][i] = 2
        
    return board

def miniChess():
    from random import randint
    print("Welcome to miniChess")
    dim = int(input("What size board would you like? \n(enter an integer greater than 2): "))
    bheight = dim
    bwidth = dim
    b = makeInitBoard(dim)    
    print("\nHere's the initial board...\n")    
    printBoard(b)

    ## ask user to select color of pawns
    ## if user selects white, then the program's color is 2 (i.e., black)
    ## if user selects black, then the program's color is 1 (i.e., white)

    while True:
        answer = input("Choose the white pawns or black pawns (enter 'w' or 'b' or 'quit'): ")
        if answer == "w":
            mycolor = 2
            break
        if answer == "b":
            mycolor = 1
            break
        if answer == "quit":
            print("Ending the game")
            return

    ## if program has white pawns, generate program's first move

    if mycolor == 1:
        print("Here's my opening move...\n")
        column = randint(0, bwidth - 1)
        b[1][column] = b[0][column]
        b[0][column] = 0
        printBoard(b)

    ## game loop

    while True:
        
        ## ask for user's move
        ## coordinates are not validated at this time
        
        print("\nEnter the coordinates of the pawn you wish to move:")
        fromrow = int(input("   row: "))
        fromcol = int(input("   col: "))
        print("Enter the coordinates of the destination square: ")
        torow = int(input("   row: "))
        tocol = int(input("   col: ")) # oops
        b[torow][tocol] = b[fromrow][fromcol]
        b[fromrow][fromcol] = 0
        print("This is your move...\n")
        printBoard(b)

        ## here is where the program uses the functions created by the student
        
        possiblemoves = move_maker(b, mycolor)  # don't change this function call
        if possiblemoves == []:
            print("I can't move\nCongratulations! You win!")
            return
        b = move_chooser(possiblemoves, mycolor) # don't change this function call


        print("Here's my response...\n")
        printBoard(b)




