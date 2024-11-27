import inquirer

Edad = int(input("Ingresa tu edad: "))
Genero=input("Ingresa tu Genero: ")
Peso = float(input("Ingresa tu peso en Kg: "))
Altura = float(input("Ingresa tu altuna en mts: "))
def actividad_fisica():
    opciones = ['Poco o ninguno', '1-3 dias', '3-5 dias', '6-7 dias', 'Mañana y tarde']
    selecciones = []

    print("Selecciona tu actividad fisica:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

    seleccion = input("Ingresa el numero de la opcion: ")
    indices_seleccionados = seleccion.split(',')

    for indice in indices_seleccionados:
        try:
            idx = int(indice.strip()) - 1
            if 0 <= idx < len(opciones):
                selecciones.append(opciones[idx])
        except ValueError:
            print(f"'{indice}' no es un número válido. Se omitirá.")

    return selecciones

# Ejemplo de uso
selecciones = actividad_fisica()
print('Has seleccionado:', selecciones)
