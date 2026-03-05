texto=input("Escibe una cadena de texto:\n")

opciones=["Numero de palabras","Convertir a MAYUSCULAS"]
for indice,valor in enumerate(opciones):
  print(f"Pulsa {indice} para: {valor}")

opcion=int(input("Indica que opcion quieres: "))

match opcion:
    case 0:
      separador=texto.split()
      numpalabras=len(separador)
      print(f"El texto que has escrito tiene {numpalabras} palabras.")
    case 1:
      may=texto.upper()
      print(may)