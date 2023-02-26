# 异序词检测

def anagramSolution1(S1,S2): 
    alist = list(S2) 
    pos1 = 0 
    stillOK = True 

    while pos1 < len(S1) and stillOK: 
        pos2 = 0 
        found = False 
        while pos2 < len(alist) and not found: 
            if S1[pos1] == alist[pos2]: 
                found = True 
            else: 
                pos2 = pos2 + 1 
        if found: 
            alist[pos2] = None 
        else: 
            stillOK = False 
        pos1 = pos1 + 1 
    return stillOK  

anagramSolution1("heart","earth") 