#from B_analyze.GetPlayerPositions import *
from AnalyzePlayer import *
from GetPieceLegalMoves import *
from GetPlayerPositions import *

def GenerateTree(B,player,depth): #Initial_X=3, Reply_O=2, reply_X=1, reply_o=0
    """
    Current Board:
        3) Player,Max->Board_A
        2) !Player,Min->Board_B
        1) Player,Max->Board_C
        0) !Player,Min->Board_D

        Should there be a variable depth function?
            ie. if it's 5 layers, it'll do max,min,max,min,max
                elif 4 layers: it'll do max,min,max,min
            Or is that logically built in?
    """
    T=[] #T is potential moves
    move=0

    if depth==1: #Minimize score
        moves=[]
        ###>>>Switch player
        if player==10:
            for i in AllLegalMoves(B,20):
                moves+=[AnalyzePlayer(SimulateBoard(B,i),20)]
        elif player==10:

        ###Switch player<<<
            
        for i in AllLegalMoves(B,player):
            moves+=[-AnalyzePlayer(SimulateBoard(B,i),player)]
            #moves are rated in terms of the other player
        return max(moves)
        
    elif player==10:
        
        for i in AllLegalMoves(B,10): #i is [initial,final]
            T+=[[i,GenerateTree(SimulateBoard(B,i),20,depth-1)]]
        return T
        
    elif player==20:
        for i in AllLegalMoves(B,10): #i is [initial,final]
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

#########################################################

def test():
    B=[23,21,22,24,25,22,21,23, \
    20,20,20,20,20,20,20,20, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    10,10,10,10,10,10,10,10, \
    13,11,12,14,15,12,11,13]

    r=GenerateTree(B,10,3)
    
    print(r)
    print("\n\n\n\n")
    #print(len(r), len(r[0][0]))
    #,"\n\n\n\n", "Length of level 1:",len(r), len(r[0]), r[1], r[2]
    return True

test()
