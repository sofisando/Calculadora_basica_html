import cgi
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

    # Realizar operaciones de cálculo
    resultado = None
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2==0:
            resultado = "Error: División por cero"
        else:
            resultado = num1 / num2

# Generar la respuesta HTML
print("<head><title>Resultado</title></head>")
print("<body>")
print("<h1>Resultado de la operación:</h1>")
print(f"<p>{num1} {operacion} {num2} = {resultado}</p>")

#print("<a href="calculadora.py">Volver atrás</a>")

print("</body>")
print("</html>")
