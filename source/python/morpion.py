# --------------------------------------
# Fonctions
# --------------------------------------

def saisir(j):
    print(f"Joueur {j} joue")
    c = int(input("Quelle case joues-tu ? "))
    return c

def completer_grille(grille,j,c):
    if j == 1:
        grille[c-1] = 'X'
    else:
        grille[c-1] = 'O'
    return grille
        
def gagner_partie(grille):
    if (grille[0] == grille[1] == grille[2]) or\
       (grille[3] == grille[4] == grille[5]) or\
       (grille[6] == grille[7] == grille[8]) or\
       (grille[0] == grille[3] == grille[6]) or\
       (grille[1] == grille[4] == grille[7]) or\
       (grille[2] == grille[5] == grille[8]) or\
       (grille[0] == grille[4] == grille[8]) or\
       (grille[2] == grille[4] == grille[6]):
        return True
    else:
        return False
    
def fin_partie(grille):
    coups_a_jouer = 0
    for i in range(len(grille)):
        if grille[i] != 'X' and grille[i] != 'O':
            coups_a_jouer = coups_a_jouer + 1
    if coups_a_jouer < 2:
        return True
    else:
        return False

def changer(j):
    if j == 1:
        return 2
    else:
        return 1
    
def afficher_grille(grille):
    print("+---+---+---+")
    if grille[6] == 'X' or grille[6] == 'O':
        print(f"| {grille[6]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[7] == 'X' or grille[7] == 'O':
        print(f"| {grille[7]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[8] == 'X' or grille[8] == 'O':
        print(f"| {grille[8]} |")
    else:
        print(f"|   |")
    print("+---+---+---+")
    if grille[3] == 'X' or grille[3] == 'O':
        print(f"| {grille[3]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[4] == 'X' or grille[4] == 'O':
        print(f"| {grille[4]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[5] == 'X' or grille[5] == 'O':
        print(f"| {grille[5]} |")
    else:
        print(f"|   |")
    print("+---+---+---+")
    if grille[0] == 'X' or grille[0] == 'O':
        print(f"| {grille[0]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[1] == 'X' or grille[1] == 'O':
        print(f"| {grille[1]} ",end='')
    else:
        print(f"|   ",end='')
    if grille[2] == 'X' or grille[2] == 'O':
        print(f"| {grille[2]} |")
    else:
        print(f"|   |")
    print("+---+---+---+\n")

if __name__ == '__main__':
# --------------------------------------
# Variables
# --------------------------------------

    grille = [1,2,3,4,5,6,7,8,9]
    joueur = 1
    fin = False
    gagnant = False


# --------------------------------------
# Programme principal
# --------------------------------------

    print("Début de partie")
    afficher_grille(grille)

    while not(fin) and not(gagnant):
        case = saisir(joueur)
        grille = completer_grille(grille,joueur,case)
        afficher_grille(grille)
        gagnant = gagner_partie(grille)
        fin = fin_partie(grille)
        if gagnant:
            print(f"Le joueur {joueur} a gagné.")
            fin = True
        elif fin:
            print("Fin de partie, pas de gagnant")
            gagnant = True
        else:
            joueur = changer(joueur)
    
    