import requests

def newDeck():
    urlDeck = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

    responseDeck = requests.get(urlDeck)
    if responseDeck.status_code == 200:
        deckID = responseDeck.json()
        return deckID["deck_id"]
    else:
        print("No se ha podido conseguir una baraja: " + responseDeck.status_code)

def newCard(url):
    shuffleUrl = f"https://www.deckofcardsapi.com/api/deck/{url}/shuffle/"
    requests.get(shuffleUrl)

    urlCard = f"https://www.deckofcardsapi.com/api/deck/{url}/draw/?count=1"

    responseCard = requests.get(urlCard)

    if responseCard.status_code == 200:
        carta = responseCard.json()
        value = carta["cards"][0]["value"]
        if value == "JACK":
            value = 11
        elif value == "QUEEN":
            value = 12
        elif value == "KING":
            value = 13
        elif value == "ACE":
            value = 14
        return int(value)
    else:
        print("No se ha podido sacar una carta: " + responseCard.status_code)

def upperLower(newCard, actualCard, opcion):
    print(f"\nCarta nueva: {newCard} - Carta anterior: {actualCard}")

    if newCard > actualCard and opcion == "g":
        print("Acertaste :)")
        return True
    elif newCard < actualCard and opcion == "g":
        print("Fallaste :(")
        return False
    elif newCard == actualCard:
        print("Son iguales :(")
        return False
    elif newCard > actualCard and opcion == "p":
        print("Fallaste :(")
        return False
    elif newCard < actualCard and opcion == "p":
        print("Acertaste :)")
        return True
    else:
        print("Opción no válida :(")
        return False

deck = newDeck()

vidas = 5

actualCard = newCard(deck)

while vidas > 0:
    print(f"\nVidas: {vidas}")
    print(f"Carta actual: {actualCard}")

    opcion = input("La siguiente carta será mayor(G) o menor(P)?\n").lower()

    siguienteCard = newCard(deck)

    acertado = upperLower(siguienteCard, actualCard, opcion)
    
    if not acertado:
        vidas -= 1
        
    actualCard = siguienteCard

print("\n¡Juego terminado!")