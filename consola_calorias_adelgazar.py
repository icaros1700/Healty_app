from consola_calculo_calorias_reposo import tmb

def adelgazar(tmb):

    adel1 = tmb * 0.8
    adel2 = tmb * 0.85


    return round(adel1,3), round(adel2,3)

reduccion = adelgazar(tmb)

print("Si quieres adelgazar tienes que consumir entre: ", reduccion[0], " Y ", reduccion[1])