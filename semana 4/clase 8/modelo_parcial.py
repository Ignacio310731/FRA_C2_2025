MAX = 10
lista_nombres = [""] * MAX
lista_puntaje = [0] * MAX
lista_comentario = [""] * MAX

while True:
    nombres = input("Ingrese un nombre: ")
    if nombres == "" or nombres == " ":
        print("Error, ingrese de vuelta")
    else:
        break
print(nombres)