import keyword

nombre = 'Joel'
telefono = 940236290
promedio = 18.43
licencia_conducir = False
parametros = None

# str -> string
"""
str -> string       -> cadena de texto
int -> integer      -> entero
float -> float      -> numero de coma flotante
bool  -> booleanos  -> verdadero o falso
None -> null
"""

# print(parametros)
# print(type(parametros))

nombre, apellidos, edad = "Joel", "Menacho", 30

lenguaje = "PYTHON"

# print(lenguaje[3])

abecedario = "abcdefghij"

# efg
# print(abecedario[4:7])
# print(abecedario[7])
# print(abecedario[5:])
# print(abecedario[:7])


institucion = "Hm System"

# print(institucion.lower())


# print(keyword.kwlist)

estatura = input('¿Cuál es tu estatura en metros?: ')

print(type(estatura))

try:
    imc = float(estatura) * 1.5
    print(round(imc, 3))
except:
    print('Hubo un problema al realizar el cálculo, contactar a sistemas')

print("Esta linea si se ejecutar")