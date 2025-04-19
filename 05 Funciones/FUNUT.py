def imprimir_hola_mundo(x):
    x="Hola mundo"
    return print(x)

def saludar_usuario(nombre):
    x=f"Hola {nombre}"
    return print(x)

def informacion_personal(nom,ap,ed,res):
    return print(f"Soy {nom} {ap}, tengo {ed} años y vivo en {res}.")

def area_de_circulo(rad):
    import math
    area=rad*math.pi**2
    return area

def perimetro_de_circulo(rad):
    import math
    perimetro=2*math.pi*rad
    return perimetro

def seg_a_hs(seg):
    seg=float(seg)
    hs=seg/3600
    return hs

def tabla_mult(n):
    n=int(n)
    for i in range (1,10):
        y=print(f"{n}x{i}={n*i}")
    return print(f"{n}x{10}={n*10}")

def operaciones_basicas(x,y):
    print (f"{x}+{y}={x+y}")
    print(f"{x}-{y}={x-y}")
    print(f"{x}x{y}={x*y}")
    return print(f"{x}:{y}={x/y}")

def calcular_imc(p,a):
    p=float(p)
    a=float(a)
    imc=p/a**2
    return round(imc,2)

def celsius_a_faranheit(T):
    T=float(T)
    F=T*33.8
    return F

def calcular_promedio(K):
    Acum=0
    map(str,K)
    for i in range (0,len(K)):
        Acum+=float(K[i])
    prom=Acum/len(K)
    return prom

def definir_lista(mensaje,mensajeparasalir):
    parar=False
    cjto=[]
    while parar==False:
        num=(input(mensaje))
        if num==mensajeparasalir:
            parar=True
        else:
            cjto.append(num)
    return cjto