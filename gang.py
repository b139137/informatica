import states

def begin() :
    print("Je staat in een GANG met een TRAP.")
    print("Kies je voor de TRAP of ga je TERUG ")
    antwoord = input("> ")
    if antwoord == "TRAP" :
        states.locaties = "ZOLDER"
    elif antwoord == "TERUG" :
        states.locaties = "TUIN"
        
        