#from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *
from B_analyze.AnalyzeBoard import *

def GenerateTree(B,player,depth): #Initial_X=3, Reply_O=2, reply_X=1, reply_o=0
    """
    Current Board:
        3) Player,Max->Board_A
        2) !Player,Min->Board_B
        1) Player,Max->Board_C
        0) !Player,Min->Board_D
    """
    T=[] #T is potential moves

    if depth==1: #Minimize score
        moves=[]

        for i in AllLegalMoves(B,player):
            moves+=AnalyzePlayer(SimulateBoard(B,i),player)
        return moves
        
    elif player==10:
        legal=AllLegalMoves(B,10)
        for i in legal: #i is [initial,final]
            T+=[[i,GenerateTree(SimulateBoard(B,i),20,depth-1)]]
            return T
    elif player==20:
        legal=AllLegalMoves(B,20)
        for i in legal: #i is [initial,final]
            T+=[[i,GenerateTree(SimulateBoard(B,i),10,depth-1)]]
            return T

def SimulateBoard(B,move): #[board,move]->[new_board]
    temp=list(B)
    temp[move[1]]=temp[move[0]]
    temp[move[0]]=0

    if temp[move[1]]==10 and move[1]<8:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]>55:
        temp[move[1]]=24

    return temp

############ DELETE BELOW

"""
Write the function GetPieceLegalMoves(board,position)
   which will return a list of all legal positions that the piece in
   the given position can take.
"""

def LegalHelp(B, i, offset, piece):
    #B is board, i is initial position, offset is the player (10 or 20)

    if i<0 or i>63:
        return False
    
    legal=[]

    if piece==1:
        moves=[-17,-15,-10,-6,6,10,15,17]
    elif piece==2:
        moves=[-9,-7,7,9]
    elif piece==3:
        moves=[-8,-1,1,8]
    elif piece==4 or piece==5:
        moves=[-9,-8,-7,-1,1,7,8,9]
    for A in moves: 
        j=i
        new=j+A
        while OnBoard(j,A) and (B[new]<offset or B[new]>=offset+10):
            legal+=[[i,new]]
            if B[new]!=0 or piece==5:
                break
            else:
                j=new
                new+=A
        
    return legal

def OnBoard(i,A):
    if A==-9 and i>7 and i%8!=0:
        return True
    elif A==-8 and i>7:
        return True
    elif A==-7 and i>7 and i%8!=7:
        return True
    elif A==-1 and i%8!=0:
        return True
    elif A==1 and i%8!=7:
        return True
    elif A==7 and i<56 and i%8!=0:
        return True
    elif A==8 and i<56:
        return True
    elif A==9 and i<56 and i%8!=7:
        return True
    else:
        return False

def KnightHelp(B,i,offset):
    legal=[]
    if i>15 and i%8!=0 and (B[i-17]<offset or B[i-17]>=offset+10):
        legal+=[[i,i-17]]
    if i>15 and i%8!=7 and (B[i-15]<offset or B[i-15]>=offset+10):
        legal+=[[i,i-15]]

    if i%8>1 and i>7 and (B[i-10]<offset or B[i-10]>=offset+10):
        legal+=[[i,i-10]]
    if i%8>1 and i<56 and (B[i+6]<offset or B[i+6]>=offset+10):
        legal+=[[i,i+6]]

    if i%8<6 and i>7 and (B[i-6]<offset or B[i-6]>=offset+10):
        legal+=[[i,i-6]]
    if i%8<6 and i<56 and (B[i+10]<offset or B[i+10]>=offset+10):
        legal+=[[i,i+10]]

    if i<48 and i%8!=0 and (B[i+15]<offset or B[i+15]>=offset+10):
        legal+=[[i,i+15]]
    if i<48 and i%8!=7  and (B[i+17]<offset or B[i+17]>=offset+10):
        legal+=[[i,i+17]]

    return legal

def GetPieceLegalMoves(B,i):
  #B is board, i is position
  legal=[]

  if B[i]==0:
    pass
##########          ##########          ##########  PAWN
  elif B[i]==10:
    if i>7:
        if B[i-8]==0:
          legal+=[[i,i-8]]
        if i%8!=0 and B[i-9]>19:
          legal+=[[i,i-9]]
        if i%8!=7 and B[i-7]>19:
          legal+=[[i,i-7]]
      
  elif B[i]==20:
    if i<56:
        if B[i+8]==0:
          legal+=[[i,i+8]]
        if i%8!=0 and B[i+7]>9 and B[i+7]<19:
          legal+=[[i,i+7]]
        if i%8!=7 and B[i+9]>9 and B[i+9]<19:
          legal+=[[i,i+9]]
##########          ##########          ##########  KNIGHT
  elif B[i]==11:
    legal=KnightHelp(B,i,10)
  elif B[i]==21:
    legal=KnightHelp(B,i,20)
##########          ##########          ##########  BISHOP
  else:
    mod=B[i]%10
    legal=LegalHelp(B,i,B[i]-mod,mod)
  return legal

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


############ DELETE ABOVE

"""
def test():
    B=[23,21,22,24,25,22,21,23, \
    20,20,20,20,20,20,20,20, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    10,10,10,10,10,10,10,10, \
    13,11,12,14,15,12,11,13]
    
    print(GenerateTree(B,10,3))
    return True

test()
"""
