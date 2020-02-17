from B_analyze.AnalyzePlayer import *
from A_move.GetPieceLegalMoves import *
from B_analyze.GetPlayerPositions import *

def BestNum(moves):
    if len(moves)>0:
        best=moves[0][1]
    else:
        print("\n\n\n\n>>>USEFULL<<<\n\n\n\n")
        best=-20000
    
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
            S=SimulateBoard(B,i)
            q=AnalyzePlayer(S,10)
            if q>-6000 and q<6000:
                r=-alphaBeta_general(S,20,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""alpha,beta
                T+=[[i,r]]
                
                value=max(value,r)
                alpha=max(value,alpha)
                if alpha >= beta:
                    break
                
        if depth==max_depth:
            return T #BestMoves(T)
        else:
            return BestNum(T)
        
    elif player==20:
        value=-20000
        for i in AllLegalMoves(B,20): #i is [initial,final]
            S=SimulateBoard(B,i)
            q=AnalyzePlayer(S,20)
            if q>-6000 and q<6000:
                r=-alphaBeta_general(S,10,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""
                T+=[[i,r]]
                #"""
                value=max(value,r)
                alpha=max(value,alpha)
                if alpha >= beta:
                    break
                #"""
        if depth==max_depth:
            return T#BestMoves(T)
        else:
            return BestNum(T)



