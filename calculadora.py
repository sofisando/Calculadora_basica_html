import cgi
#Headers
print ("Content.Type: text/html")  
print() 
print ("""<html>
<head>
    <title>Calculadora básica HTML</title>
</head>
<body>
    <form method="get" action="respuesta.py">
        Primer número: <input name="num1" type="number" /><br />
        Segundo número: <input name="num2" type="number" /><br />

        <p>Ingrese la operación que desea realizar</p>
        <input type="radio" id="suma" name="operacion" value="Suma">
        <label for="suma">Suma</label><br>
        <input type="radio" id="resta" name="operacion" value="Resta">
        <label for="resta">Restar</label><br>
        <input type="radio" id="multiplicacion" name="operacion" value="Multiplicacion">
        <label for="multiplicacion">Multiplicar</label><br>
        <input type="radio" id="division" name="operacion" value="Division">
        <label for="division">Dividir</label><br>

        <button type="submit">Enviar</button>
    </form>
</body>
</html>""")

#post o get o put o delete
#diferencia entre post y get
#post añade los datos a la base de datos y el get utiliza un url (creo)