# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

destino = input("¿A que destino desea viajar? (Bariloche, MDQ, Cataratas)")
estacion = input("¿En que estacion desea viajar? (invierno, verano, otoño, primavera)")

match estacion:
    case "invierno":
        if destino == "Bariloche":
            print("Viaja")
        else:
            print("No viaja...")
    case "verano":
        if destino == "MDQ" or "Cataratas":
            print("Viaja")
        else:
            print("No viaja...")
    case "otoño":
            print("Viaja")
    case "primavera":
        if destino == "MDQ" or "Cataratas":
            print("Viaja")
        else:
            print("No viaja...")



