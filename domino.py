cont=0
def crearFichas(n):
    fichas=[]
    for x in range(n+1):
        for y in range(x,n+1):
            fichas.append([x,y])
    return fichas

def invertir(ficha):
    return [ficha[1],ficha[0]]

def esta(ficha,solucion):
    return ficha in solucion or invertir(ficha) in solucion

def coincide(ficha1,ficha2):
    return ficha1[1]==ficha2[0]

def igual(ficha):
    return ficha[0]==ficha[1]
    
def organizar(fichas,solucion):
    global cont
    if len(solucion)==len(fichas):
        print("Una solucion :",solucion)
        #input()
        cont+=1
    else:
        for ficha in fichas:
            if not solucion:
                solucion.append(ficha)
                organizar(fichas,solucion)
                solucion.pop()
                if not igual(ficha):
                    solucion.append(invertir(ficha))
                    organizar(fichas,solucion)
                    solucion.pop()
            else:
                if not esta(ficha,solucion):
                    if coincide(solucion[-1],ficha):
                        solucion.append(ficha)
                        organizar(fichas,solucion)
                        solucion.pop()
                    elif coincide(solucion[-1],invertir(ficha)) and not igual(ficha):
                        solucion.append(invertir(ficha))
                        organizar(fichas,solucion)
                        solucion.pop()
                
n=int(input("Valor de n : "))
domino=crearFichas(n)
print(domino)
solucion=[]
organizar(domino,solucion)
print("Total de soluciones es : ",cont)
