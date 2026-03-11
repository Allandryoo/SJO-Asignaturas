marcas = ["Seat", "Volkswagen", "Toyota", "Renault", "Flat", "Peugeot"]

def mostrar_marcas(marca):
    print(f"Marca: {marca}")

def main():
    print("Lista de marcas de coches:")
    print("-"*30)

    [mostrar_marcas(marca) for marca in marcas]

if __name__ == "__main__":
    main()

#El mapeo llama a la funcion de mostrar_marcas
#Cada elemento de la lista pintea marca y el elemento de la lista que corresponde