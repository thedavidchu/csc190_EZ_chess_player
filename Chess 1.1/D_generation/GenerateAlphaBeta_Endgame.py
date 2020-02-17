from A_move.GetPieceLegalMoves import *
from B_analyze.AnalyzePlayer import *
from B_analyze.GetPlayerPositions import *

def BestNum(moves):
    if len(moves)>0:
        best=moves[0][1]
    else:
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

def AnalyzePlayer_Endgame(B,player):
    white=0
    black=0

    #Black:

    pawn=[  0,  0,  0,  0,  0,  0,  0,  0,\
 45, 45, 45, 45, 45, 45, 45, 45,\
 30, 30, 30, 30, 30, 30, 30, 30,\
 15, 15, 15, 15, 15, 15, 15, 15,\
  0,  0,  0,  0,  0,  0,  0,  0,\
  5, -5,-10,  0,  0,-10, -5,  5,\
  5, 10, 10,-20,-20, 10, 10,  5,\
  0,  0,  0,  0,  0,  0,  0,  0]

    #White

    Pawn=[  0,  0,  0,  0,  0,  0,  0,  0,\
  5, 10, 10,-20,-20, 10, 10,  5,\
  5, -5,-10,  0,  0,-10, -5,  5,\
  0,  0,  0,  0,  0,  0,  0,  0,\
 15, 15, 15, 15, 15, 15, 15, 15,\
 30, 30, 30, 30, 30, 30, 30, 30,\
 45, 45, 45, 45, 45, 45, 45, 45,\
  0,  0,  0,  0,  0,  0,  0,  0]

    for i in range(0,64,1):
        if B[i]==0:
            pass
        
        elif B[i]==10:
            white+= 100 + Pawn[i]
        elif B[i]==20:
            black+= 100 + pawn[i]
            
        elif B[i]==11:
            white+= 300
        elif B[i]==21:
            black+= 300

        elif B[i]==12:
            white+= 300
        elif B[i]==22:
            black+= 300

        elif B[i]==13:
            white+= 500
        elif B[i]==23:
            black+= 500

        elif B[i]==14:
            white+= 900
        elif B[i]==24:
            black+= 900

        elif B[i]==15:
            white+= 9000
        elif B[i]==25:
            black+= 9000

        else:
            pass

    if player==10:
        return white-black
    elif player==20:
        return black-white


def alphaBeta_Endgame(B,player,max_depth,depth,alpha,beta): #Look ahead more
    T=[] #T is potential moves
    moves=[]
    
    if depth==0:
        for i in AllLegalMoves(B,player):
            moves+=[AnalyzePlayer_Endgame(SimulateBoard(B,i),player)]
        return max(moves)#BestMoves(moves)

    elif player==10:
        value=-20000
        for i in AllLegalMoves(B,10): #i is [initial,final]
            S=SimulateBoard(B,i)
            q=AnalyzePlayer_Endgame(S,10)
            if q>-6000 and q<6000:
                r=-alphaBeta_Endgame(S,20,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""alpha,beta
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
            q=AnalyzePlayer_Endgame(S,10)
            if q>-6000 and q<6000:
                r=-alphaBeta_Endgame(S,10,max_depth,depth-1,-beta,-alpha) #Negative?"""beta,alpha"""
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



