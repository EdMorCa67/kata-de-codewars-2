def multitable(multiplicando):
    tabla_multiplicacion = ""
    for multiplicador in range(1, 11):
        resultado = multiplicando * multiplicador
        tabla_multiplicacion += f"{multiplicando} x {multiplicador} = {resultado}\n"

    return tabla_multiplicacion.strip()


print(multitable(5))