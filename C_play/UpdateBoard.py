from B_analyze.IsPositionUnderThreat import *
from B_analyze.AnalyzePlayer import *

def UpdateBoard(B,player,move):
    B[move[1]]=B[move[0]]
    B[move[0]]=0

    analysis=AnalyzePlayer(B,player)

    #Pawn Promotion
    if B[move[1]]==10 and move[1]>55:
        B[move[1]]=14
    elif B[move[1]]==20 and move[1]<8:
        B[move[1]]=24

    #Check and Checkmate
    check=Check(B)
    if check[0]==True:
        print("WARNING: WHITE is in Check")
        if Checkmate(B,check)[0]==True:
            print("Checkmate!")
            return 2#[B,2]
        
    if check[1]==True:
        print("WARNING: BLACK is in Check")
        if Checkmate(B,check)[1]==True:
            return 1#[B,1]

    if analysis>6000:
        print("King Captured!")
        return int(player/10)

    return 0#[B,0]
