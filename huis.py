import states

def begin() :
    print("Je staat in een TUIN met een HUIS.")
    print("Kies je voor de DEUR of ga je de TUIN in?")
    antwoord = input("> ")
    if antwoord == "DEUR" :
        states.locaties = "GANG"
    elif antwoord == "TUIN" :
        states.locaties = "TUIN"