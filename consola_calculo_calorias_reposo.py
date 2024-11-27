from Datos import Edad, Genero, Peso, Altura

def tasa_metabolica_basal (Edad, Genero, Peso, Altura):

    if Genero == "MASCULINO":
        Gen = 5
    else:
        Gen = -161

    TMB = (10 * Peso) + (6.25 * Altura) - (5 * Edad) + Gen
    return round(TMB,3)

tmb = tasa_metabolica_basal(Edad, Genero, Peso, Altura)

print("Tu calorias en reposo son: ", tmb)