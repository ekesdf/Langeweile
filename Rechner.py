

# Grundaustellung vor jedem Spiel

Feld = [
    ["Tw ", "Pw ", "Lww", "Kw ", "Dw ", "Lwb", "Pw ", "Tw "],
    ["Bw ", "Bw ", "Bw ", "Bw ", "Bw ", "Bw ", "Bw ", "Bw "],
    ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    ["Bb ", "Bb ", "Bb ", "Bb ", "Bb ", "Bb ", "Bb ", "Bb "],
    ["Tb ", "Pb ", "Lbb", "Kb ", "Db ", "Lbw", "Pb ", "Tb "],
]

Teamschwarz = ["Bb ", "Tb ", "Pb ", "Lbb", "Kb ", "Db ", "Lbw"]
Teamweiß = ["Bw ", "Tw ", "Pw ", "Lww", "Kw ", "Dw ", "Lwb"]
Figuren_kekickt = []



def Position(Reihe,Spalte):

    index = Spalte+((Reihe-1)*8)

    return index

def leere_Liste_Feld_anfang():

    Liste_Feld = []

    for Reihe in range(8):

        for Spalte in range(8):

            Liste_Feld.append(("   ",Reihe+1,Spalte+1))

    return Liste_Feld

print(leere_Liste_Feld_anfang())
















