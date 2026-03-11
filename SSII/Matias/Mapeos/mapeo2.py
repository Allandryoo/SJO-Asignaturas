frutas=["manzana", "platano", "kiwi", "fresa", "naranja", "pera"]

def listar_frutas(fruta):
    print(f"Me gusta la fruta: {fruta}")
    
def main():
    [listar_frutas(fruta) for fruta in frutas]

if __name__ == "__main__":
    main()

#Preguntas
#1: La funcion de listar_fruta se ejecuta 6 veces, porque cada vez que llamamos a listar le estamos dando el valor de cada elemento de la lista uno a uno

#2: Es una lista comprimida, la variable "fruta" va tomando cada elemento de la lista uno a uno y va llamando a la funcion listar_frutas con el valor de ese momento

#3: Guardar el resultado en una variable es inutil porque la lista comprimida hace ya ese trabajo

#4: Cambia el orden en el que aparece las frutas que me gustan

#5: Si se quitan los corchetes la linea habria que cambiarla a:
#for fruta in frutas:
#   listar_frutas(fruta)