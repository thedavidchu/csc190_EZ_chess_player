def InitBoard():
    return [13,11,12,15,14,12,11,13, \
    10,10,10,10,10,10,10,10, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    0,0,0,0,0,0,0,0, \
    20,20,20,20,20,20,20,20, \
    23,21,22,25,24,22,21,23]

def PrintBoard(B):
    #B is board
    blank="#_#_#_#_\
_#_#_#_#\
#_#_#_#_\
_#_#_#_#\
#_#_#_#_\
_#_#_#_#\
#_#_#_#_\
_#_#_#_#"
    board=""
    
    for i in range(0,64,1):
        if B[i]==0:
            board=blank[i]+board
        elif B[i]==10:
            board="P"+board
        elif B[i]==20:
            board="p"+board
        elif B[i]==11:
            board="N"+board
        elif B[i]==21:
            board="n"+board
        elif B[i]==12:
            board="B"+board
        elif B[i]==22:
            board="b"+board
        elif B[i]==13:
            board="R"+board
        elif B[i]==23:
            board="r"+board
        elif B[i]==14:
            board="Q"+board
        elif B[i]==24:
            board="q"+board
        elif B[i]==15:
            board="K"+board
        elif B[i]==25:
            board="k"+board

    print(board[0:8])
    print(board[8:16])
    print(board[16:24])
    print(board[24:32])
    print(board[32:40])
    print(board[40:48])
    print(board[48:56])
    print(board[56:64]+"\n")
      
    return True
"""
def main():
    PrintBoard(InitBoard())
main()
"""

