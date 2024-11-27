
from Datos import Edad, Genero, Peso, Altura
from consola_calculo_imc import imc


def calculo_grasa(Edad, Genero, Peso, Altura):

    if Genero == "MASCULINO":
        Gen = 10.8
    else:
        Gen = 0
    
    GC = (1.2 * imc) + (0.23 * Edad) - 5 - Gen

    return round(GC,3)

gr = calculo_grasa(Edad, Genero, Peso, Altura)

print("Tu porcentaje de grasa es: ", str(gr) + " %")

