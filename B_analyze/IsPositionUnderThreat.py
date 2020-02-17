from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *

"""
Write the function IsPositionUnderThreat(board,position,player)
   which will return True if the position is under threat by the opponent
   of the given player
"""

def IsPositionUnderThreat(B,i,offset):
    #B is board, i is position, offset is player
    enemy_loci=[]
    enemy_attack=[]
    if offset==10:
        enemy_loci=GetPlayerPositions(B,20) #Returns [type,position]
    elif offset==20:
        enemy_loci=GetPlayerPositions(B,10)
    for locus in enemy_loci: #locus [type,position]
        enemy_attack=GetPieceLegalMoves(B,locus)
        for target in enemy_attack: #target [initial, final]
            if target[1]==i:
                return True
    return False
        
def Check(B):
    whiteCheck=False
    blackCheck=False
    
    for i in range(0,64,1):
        if B[i]==15:
            whiteCheck=IsPositionUnderThreat(B,i,10)
        if B[i]==25:
            blackCheck=IsPositionUnderThreat(B,i,20)
    return [whiteCheck, blackCheck]
    
def Checkmate(B,check):
    whiteMate=False
    blackMate=False
    
    if check[0]==True:
        whiteMate=True
        for i in AllLegalMoves(B,10): #i is [initial, final]
            tempBoard=list(B)
            tempBoard[i[1]]=tempBoard[i[0]]
            tempBoard[i[0]]=0
            #print(Check(tempBoard))
            if Check(tempBoard)[0]==False:
                whiteMate=False
                break
        #print(whiteMate)
            
    if check[0]==True:
        blackMate=True
        for i in AllLegalMoves(B,20):
            tempBoard=list(B)
            tempBoard[i[1]]=tempBoard[i[0]]
            tempBoard[i[0]]=0
            if Check(tempBoard)[1]==False:
                blackMate=False
                break

    return [whiteMate,blackMate]
