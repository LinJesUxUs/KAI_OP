def getUIntWithMsg(msg: str = "Enter uint value.\n",error: str = "Error!"):
    buf = 0
    while(True):
        try: buf = abs(int(input(msg)))
        except: print(error)
        else: break
    return buf

def getBoolVal():
    v = input()
    try:
        v = int(v)
        if (v==0): return False
        else: return True
    except: pass
    try:
        v = float(v)
        if (v==0.0): return False
        else: return True
    except: pass
    if (v.lower()=="y"): pass
    elif (v.lower()=="yes"): pass
    elif (v.lower()=="да"): pass
    elif (v.lower()=="д"): pass
    elif (v.lower()=="true"): pass
    elif (v.lower()=="верно"): pass
    else: return False
    return True
