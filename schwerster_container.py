import sys

def such_den_schwersten(paarliste):
    klein_container = set()
    gross_container = set()
    for paar in paarliste:
        if paar[1] in gross_container:
            gross_container.remove(paar[1])
        klein_container.add(paar[1])
        if paar[0] in klein_container:
            continue
        gross_container.add(paar[0])
    if len(gross_container) == 1:
        return list(gross_container)[0]
    else:
        return -1
    
def paarliste_aus_datei(datei):
    paarliste = []
    d = open(datei, 'r')
    for zeile in d:
        paarliste.append(zeile.strip('\n').split())
    return paarliste

def haupt_funktion(datei):
    paarliste = paarliste_aus_datei(datei)
    schwerster_container = such_den_schwersten(paarliste)
    print("Der schwerste Container ")
    if schwerster_container == -1:
        print("kann nicht bestimmt werden.")
    else:
        print("ist Container Nr." + schwerster_container)

if __name__ == '__main__':
    datei = sys.argv[1]
    haupt_funktion(datei)
