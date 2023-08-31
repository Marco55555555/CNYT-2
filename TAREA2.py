import math
def sum(NUM1,NUM2):
    res = (NUM1[0]+NUM2[0],NUM1[1]+NUM2[1])
    return res

def res(NUM1,NUM2):
    res = (NUM1[0]-NUM2[0],NUM1[1]-NUM2[1])
    return res

def pro(NUM1,NUM2):
    res = (NUM1[0]*NUM2[0]-NUM1[1]*NUM2[1],NUM1[0]*NUM2[1]+NUM2[0]*NUM1[1])
    return res

def div(NUM1,NUM2):
    res = ((((NUM1[0]*NUM2[0])+(NUM1[1]*NUM2[1]))/(NUM2[0]**2+NUM2[1]**2)),(((NUM2[0]*NUM1[1])-(NUM1[0]*NUM2[1]))/(NUM2[0]**2+NUM2[1]**2)))
    return res

def mod(NUM1):
    res = math.sqrt(NUM1[0]**2+NUM1[1]**2)
    return res

def conj(NUM1):
    res = (NUM1[0],(-1)*NUM1[1])
    return res

def ctop(NUM1):
    res = (round(math.sqrt(NUM1[0]**2+NUM1[1]**2),2),round(math.atan(NUM1[1]/NUM1[0])*180/math.pi,2))
    return res

def fase(NUM1):
    res = round(math.atan(NUM1[1]/NUM1[0])*180/math.pi,2)
    return "{}°".format(res)

def SumV(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2):
        for i in range(len(Data1)):
            res.append(sum(Data1[i],Data2[i]))
        return res
    else: return res

def InvV(Data1):
    res=[]
    for i in range(len(Data1)):
        res.append(pro(Data1[i],(-1,0)))
    return res

def eVec(Escalar,Data1):
    res=[]
    for i in range(len(Data1)):
        res.append(pro(Data1[i],Escalar))
    return res

def SumM(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2) and len(Data1[0])==len(Data2[0]):
        for i in range(len(Data1)):
            columna=[]
            for j in range(len(Data1[i])):
                columna.append(sum(Data1[i][j],Data2[i][j]))
            res.append(columna)
        return res
    else: return res

def ResM(Data1,Data2):
    res=[]
    if len(Data1)==len(Data2) and len(Data1[0])==len(Data2[0]):
        for i in range(len(Data1)):
            columna=[]
            for j in range(len(Data1[i])):
                columna.append(res(Data1[i][j],Data2[i][j]))
            res.append(columna)
        return res
    else: return res

def InvM(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(pro(Data1[i][j],(-1,0)))
        res.append(columna)
    return res

def eMat(Escalar,Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(pro(Data1[i][j],Escalar))
        res.append(columna)
    return res

def Tra(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(Data1[j][i])
        res.append(columna)
    return res

def ConjM(Data1):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data1[i])):
            columna.append(conj(Data1[i][j]))
        res.append(columna)
    return res
