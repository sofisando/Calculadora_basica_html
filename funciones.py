#funciones reutilizables
def suma(a,b):
    resultado= a+b
    return resultado

def resta(a,b):
    resultado= a-b
    return resultado

def multiplicacion(a,b):
    resultado= a*b
    return resultado

def division(a,b):
    if b==0:
       print("Error. No se puede dividir por 0")
    else:
        resultado=a/b
        return resultado
    

