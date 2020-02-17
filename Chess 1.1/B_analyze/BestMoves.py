from B_analyze.AnalyzePlayer import *

def BestMove_Single(B,moves,player): #moves = [ [[initial,final],score,[tree]], [], [],... ]
    if len(moves)>0:
        best=moves[0]
    else:
        return []
    for i in moves:
        if i[1]>best[1]:
            best=i
        elif i[1]==best[1]:
            if AnalyzePlayer(SimulateBoard(B,i[0]),player)>AnalyzePlayer(SimulateBoard(B,best[0]),player):
                best=i
    return best

def SimulateBoard(B,move): #[board,move]->[new_board]
    temp=list(B)
    temp[move[1]]=temp[move[0]]
    temp[move[0]]=0

    if temp[move[1]]==10 and move[1]>55:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]<8:
        temp[move[1]]=24

    return temp
