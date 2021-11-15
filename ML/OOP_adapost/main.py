from Adapost import Adapost
from Catel import Catel
from Pisica import Pisica

if __name__ == '__main__':
    adapost_local = Adapost()
    while True:
        line = input('Introduceti o noua comanda: ')
        cmd = line.split()
        if cmd[0] == 'exit':
            print('Aplicatia se va inchide...')
            break
        elif cmd[0] == 'afiseaza':
            if len(cmd) == 1:
                adapost_local.afisare_animale()
            else:
                tip_animal = cmd[1]
                adapost_local.afisare_specifica(tip_animal)
        elif cmd[0] == 'adauga_catel':
            varsta = int(cmd[1])
            rasa = cmd[2]
            vaccinat = cmd[3]
            c = Catel(varsta, rasa, vaccinat)
            adapost_local.adauga_animal(c)
        elif cmd[0] == 'adauga_pisica':
            varsta = int(cmd[1])
            rasa = cmd[2]
            vaccinat = cmd[3]
            sterilizat = cmd[4]
            p = Pisica(varsta, rasa, vaccinat, sterilizat)
            adapost_local.adauga_anmimal(c)
        elif cmd[0] == 'adopta_animal':
            id_adoptat = int(cmd[1])
            adapost_local.adoptie_animal(id_adoptat)