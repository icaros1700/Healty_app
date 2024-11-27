from consola_calculo_calorias_reposo import tmb
from Datos import selecciones

def tmb_actividad_fisica(tmb):

    if selecciones == "Poco o ninguno":
        tmb_a = 1.2
    elif selecciones == "1-3 dias":
        tmb_a = 1.375
    elif selecciones == "3-5 dias":
        tmb_a = 1.55
    elif selecciones == "6-7 dias":
        tmb_a = 1.72
    else:
        tmb_a = 1.9
    
    TMB_AC = tmb * tmb_a
    return round(TMB_AC,3)

actividad = tmb_actividad_fisica(tmb)

print("Tu TMB x Actividad fisica es: ", actividad )