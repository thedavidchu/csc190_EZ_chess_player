"""
Write the function GetPieceLegalMoves(board,position)
   which will return a list of all legal positions that the piece in
   the given position can take.
"""

def LegalHelp(B, i, player, piece):
    #B is board, i is initial position, player is the player (10 or 20)

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
        while OnBoard(j,A) and (B[new]<player or B[new]>player+9):
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

def KnightHelp(B,i,player):
    legal=[]
    if i>15 and i%8!=0 and (B[i-17]<player or B[i-17]>player+9):
        legal+=[[i,i-17]]
    if i>15 and i%8!=7 and (B[i-15]<player or B[i-15]>player+9):
        legal+=[[i,i-15]]

    if i%8>1 and i>7 and (B[i-10]<player or B[i-10]>player+9):
        legal+=[[i,i-10]]
    if i%8>1 and i<56 and (B[i+6]<player or B[i+6]>player+9):
        legal+=[[i,i+6]]

    if i%8<6 and i>7 and (B[i-6]<player or B[i-6]>player+9):
        legal+=[[i,i-6]]
    if i%8<6 and i<56 and (B[i+10]<player or B[i+10]>player+9):
        legal+=[[i,i+10]]

    if i<48 and i%8!=0 and (B[i+15]<player or B[i+15]>player+9):
        legal+=[[i,i+15]]
    if i<48 and i%8!=7  and (B[i+17]<player or B[i+17]>player+9):
        legal+=[[i,i+17]]

    return legal

def GetPieceLegalMoves(B,i):
  #B is board, i is position
    legal=[]
    if B[i]==0:
        pass

    #Pawn:
    elif B[i]==10:
        if i<56:
            if B[i+8]==0:
                legal+=[[i,i+8]]
            if i%8!=0 and B[i+7]>19:
                legal+=[[i,i+7]]
            if i%8!=7 and B[i+9]>19:
                legal+=[[i,i+9]]
      
    elif B[i]==20:
        if i>7:
            if B[i-8]==0:
                legal+=[[i,i-8]]
            if i%8!=0 and B[i-9]>9 and B[i-9]<19:
                legal+=[[i,i-9]]
            if i%8!=7 and B[i-7]>9 and B[i-7]<19:
                legal+=[[i,i-7]]

    #Knight:
    elif B[i]==11:
        legal=KnightHelp(B,i,10)
    elif B[i]==21:
        legal=KnightHelp(B,i,20)

    #Linear Pieces:
    else:
        mod=B[i]%10
        legal=LegalHelp(B,i,B[i]-mod,mod)
    return legal


