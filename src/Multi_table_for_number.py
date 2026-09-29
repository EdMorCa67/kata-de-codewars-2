
def multiTable(n):
    resultado = ""
    multiplo = 1
    while multiplo <= 10:
        
        resultado += f"{multiplo} * {n} = {multiplo * n}"

        if multiplo < 10:
            resultado += "\n"


        multiplo += 1
    return resultado


print(multiTable(2))

