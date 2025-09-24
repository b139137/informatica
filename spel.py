import states
import huis
import gang
import zolder
import tuin

while True :
    if states.locatie == "HUIS" :
        huis.begin()
    elif states.locatie == "GANG" :
        gang.begin()
    elif states.locatie == "ZOLDER" :
        zolder.begin()
    elif states.locatie == "TUIN" :
        zolder.begin()    
    
