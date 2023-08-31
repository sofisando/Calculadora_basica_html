import cgi
from funciones import suma,resta,multiplicacion,division  #se importan las funciones de la ptra pestaña

# Headers
print ("Content-Type: text/html")
print()
print("<html>")
form_input = cgi.FieldStorage()

if "num1" not in form_input or "num2" not in form_input:
    print("Debe ingresar dos numeros para hacer la operación")
    #despues poner que si no elijió una opcion debe elejirla
else:
    # Obtener los valores de num1, num2 y operacion
    num1 = int(form_input["num1"].value)
    num2 = int(form_input["num2"].value)
    operacion = form_input["operacion"].value

    a=num1
    b=num2

    # Realizar operaciones de cálculo
    resultado = None
    if operacion == "Suma":
        resultado= suma(a,b)
    elif operacion == "Resta":
        resultado= resta(a,b)
    elif operacion == "Multiplicacion":
        resultado= multiplicacion(a,b)
    elif operacion == "Division":
        if num2==0:
            print("Error: División por cero") 
        else:
            resultado= division(a,b)

    # Generar la respuesta HTML
    print("<head><title>Resultado</title></head>")
    print("<body>")
    print("<h1>Resultado de la operación:</h1>")
    print(f"<p>{num1} {operacion} {num2} = {resultado}</p>")

    #print("<a href="calculadora.py">Volver atrás</a>")

    print("</body>")
    print("</html>")
