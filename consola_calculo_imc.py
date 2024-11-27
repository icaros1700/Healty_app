from Datos import Edad, Peso, Altura



def calculo_imc (Peso, Altura):
    IMC = Peso/(Altura**2)
    return round(IMC,2)

imc=calculo_imc(Peso, Altura)

print("Tu IMC es de: ", imc )