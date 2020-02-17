def TotalMaterial(B):
    white=0
    black=0
    
    for i in B:
        if i==0:
            pass
        elif i==10:
            white+=100
        elif i==20:
            black+=100

        elif i==11:
            white+=300
        elif i==21:
            black+=300
        elif i==12:
            white+=300
        elif i==22:
            black+=300

        elif i==13:
            white+=500
        elif i==23:
            black+=500
            
        elif i==14:
            white+=900
        elif i==24:
            black+=900
        else:
            pass

    return white + black
    """
    if player==10:
        return white
    elif player==20:
        return black

    """
