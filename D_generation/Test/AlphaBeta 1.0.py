from LIB.AnalyzePlayer import *
from LIB.GetPieceLegalMoves import *
from LIB.GetPlayerPositions import *

def BestMoves(moves): #moves = [ [[initial,final],score], [], [],... ]
    best=[moves[0]]
    for i in moves:
        if i[1]>best[0][1]:
            best=[i]
        elif i[1]==best[0][1]:
            best+=[i]
    return best


def BestNum(moves):
    best=moves[0][1]
    for i in moves:
        if i[1]>best:
            best=i[1]
    return best

def SimulateBoard(B,move): #[board,move]->[new_board]
    temp=list(B)
    temp[move[1]]=temp[move[0]]
    temp[move[0]]=0

    if temp[move[1]]==10 and move[1]<8:
        temp[move[1]]=14
    elif temp[move[1]]==20 and move[1]>55:
        temp[move[1]]=24

    return temp

def alphaBeta_general(B,player,max_depth,depth,alpha,beta):
    T=[] #T is potential moves
    moves=[]
    
    if depth==0:
        for i in AllLegalMoves(B,player):
            moves+=[AnalyzePlayer(SimulateBoard(B,i),player)]
        return max(moves)#BestMoves(moves)

    elif player==10:
        value=-20000
        for i in AllLegalMoves(B,10): #i is [initial,final]

            r=alphaBeta_general(SimulateBoard(B,i),20,max_depth,depth-1,beta,alpha)
            T+=[[i,r]]

            value=max(value,r)
            alpha=max(value,alpha)
            if alpha >= beta:
                break
            
        if depth==max_depth:
            return BestMoves(T)
        else:
            return BestNum(T)
        
    elif player==20:
        value=-20000
        for i in AllLegalMoves(B,20): #i is [initial,final]

            r=alphaBeta_general(SimulateBoard(B,i),10,max_depth,depth-1,beta,alpha)
            T+=[[i,r]]

            value=max(value,r)
            alpha=max(value,alpha)
            if alpha >= beta:
                break
            
        if depth==max_depth:
            return BestMoves(T)
        else:
            return BestNum(T)




def main():
    B=[13,11,12,15,14,12,11,13, \
    10,10,10,10,10,10,10,10, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    20,20,20,20,20,20,20,20, \
    23,21,22,25,24,22,21,23]
    
    moves = alphaBeta_general(B,10,3,3,-20000,20000)
    print(moves)
    return True

main()
