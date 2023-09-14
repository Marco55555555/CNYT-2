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
############################################33
def Unit(Data1):
    res = AdjM(Data1)
    Un = []
    for i in range(len(Data1)):
        col1 = []
        for j in range (len(Data1[i])):
            if i == j:
                col1.append((1,0))
            else: 
                col1.append((0,0))
        Un.append(col1)
    res = MulM(res,Data1)
    if res == Un:return True
    else:return False

def Herm(Data1):
    res = AdjM(Data1)
    if(res==Data1):return True
    else:return False
    
def productoTensorV(c,d):
    resultado=[]
    for i in range (len(c)):
        for j in range(len(d)):
            r=c[i]*d[j]
            resultado.append(r)
    print(resultado)
    return resultado

def productoTensorM(a,b):  
    n=len(b)
    n2=len(b[0])
    m=len(a)
    m2=len(a[0])
    t=n*m
    t2=n2*m2
    r=[[0 for i in range (t)]for j in range (t2)]
    for i in range(t2):
        for j in range(t):
            r[i][j]=a[j//n][j//n2]*b[j%n][j%n2]
    print(r)
    return r



















    
