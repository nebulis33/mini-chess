##prog67.py
##Colton Juliano
##3/16/17
##
def move_maker(board,mycolor):
    '''Takes a board in the form of a list of lists and number representing a color
and returns the possible moves that color can make from the original board'''
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
    '''Takes a list of possible boards and a color and returns the best move for
that color as a board in the form of a list of lists'''
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

