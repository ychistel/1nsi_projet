import pyxel
from morpion import *

grille = [1,2,3,4,5,6,7,8,9]
joueur = 1
fin = False
gagnant = False


# Etats du jeu
def update():
    global joueur, grille, fin, gagnant
    case = saisir(joueur)
    print(case)
    grille = completer_grille(grille,joueur,case)
    #afficher_grille(grille)
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

# Dessin des états de jeu
def draw():
    pyxel.cls(0)
    k = 1
    for j in range(3):
        for i in range(3):
            pyxel.rectb(34+i*20,74-j*20,20,20,3)
            pyxel.text(44+i*20,84-j*20,str(k),13)
            k = k + 1

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128, title="Projet jeu")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
