from A_move.GetPieceLegalMoves import *
from C_play.PrintBoard import *

def HumanPlayer(B,player):
    #PrintBigBoard(B)
    PrintBoard(B)
    if player==10:
        print("White to Play:")
    else:
        print("Black to Play:\n")
        
    while True:
        i=int(input(">>>From: "))
        legal=GetPieceLegalMoves(B,i)
        if i<0 or i>64:
            print("ERROR: INVALID BOARD SPACE")
        elif B[i]<player or B[i]>player+5:
            print("ERROR: INVALID PIECE SELECTION")
        elif len(legal)<1:
            print("ERROR: NO LEGAL MOVES")
        else:
            print(legal)
            break
                
    while True:
        coin=False
        j=int(input(">>>To: "))
        if j<0 or j>63:
            print("ERROR: INVALID BOARD SPACE")
        else:
            for move in legal:
                if move[1]==j:
                    B[j]=B[i]
                    B[i]=0
                    coin=True
                    break
            if coin==False:
                print("ERROR: ILLEGAL MOVE")
        if coin==True:
            break
    return B
