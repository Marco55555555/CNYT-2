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
    #########################################################################

def AdjM(Data1):
    res = []
    for i in range(len(Data1)):
        columna = []
        for j in range(len(Data1[i])):
            columna.append(conj(Data1[j][i]))
        res.append(columna)
    return res

def AdjV(Data1):
    res = []
    for i in range(len(Data1)):
        res.append(conj(Data1[i]))
    return res
    
def MulM(Data1,Data2):
    Matriz = []
    for i in range(len(Data1)):
        Fila = []
        for j in range(len(Data2[0])):
            Rp = 0
            Ip = 0
            for k in range(len(Data1[0])):
                Rp += pro(Data1[i][k],Data2[k][j])[0]
                Ip += pro(Data1[i][k],Data2[k][j])[1]
            Fila.append((Rp,Ip))
        Matriz.append(Fila)
    return Matriz

def AcMV(Data1,Data2):
    res=[]
    for i in range(len(Data1)):
        Rp = 0
        Ip = 0
        for k in range(len(Data2)):
            Rp += pro(Data1[i][k],Data2[k])[0]
            Ip += pro(Data1[i][k],Data2[k])[1]
        res.append((Rp,Ip))
    return res

def PriV(Data1,Data2):
    Data1 = AdjV(Data1)
    Rp = 0
    Ip = 0
    for i in range(len(Data1)):
        Rp += pro(Data1[i],Data2[i])[0]
        Ip += pro(Data1[i],Data2[i])[1]
    return (Rp,Ip)

def NorV(Data1):
    res=0
    for i in range(len(Data1)):
        res += Data1[i][0]**2+Data1[i][1]**2
    return math.sqrt(res)

def DisV(Data1,Data2):
    res = []
    for i in range(len(Data1)):
        res.append(res(Data1[i],Data2[i]))
    d = 0
    for j in range(len(res)):
        d += mod(res[j])























    
