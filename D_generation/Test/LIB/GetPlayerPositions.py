from LIB.GetPieceLegalMoves import *

"""
Write the function GetPlayerPositions(board,player)
   where board is the list data struct that represents the chess board
   (described above) and player is 10 (for white) and 20 (for black).
   It should return a list of all positions that the player occupies.
"""

def GetPlayerPositions(B,player):
    #B is board and player is player
    loci=[] #position
    for i in range(0,64,1):
        if B[i]>=player and B[i]<player+6:
            loci+=[[B[i],i]]
    return loci

def AllLegalMoves(B,player):
    loci=GetPlayerPositions(B,player)
    legal=[]
    for locus in loci:
        legal+=GetPieceLegalMoves(B,locus[1])
    return legal
