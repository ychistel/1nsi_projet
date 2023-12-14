import pyxel
from morpion import *

grille = [1,2,3,4,5,6,7,8,9]
joueur = 1
fin = False
gagnant = False
choix = 0

def saisie_clavier():
    global joueur
    if pyxel.btn(pyxel.KEY_KP_1):
        return 1
    elif pyxel.btn(pyxel.KEY_KP_2):
        return 2
    elif pyxel.btn(pyxel.KEY_KP_3):
        return 3
    elif pyxel.btn(pyxel.KEY_KP_4):
        return 4
    elif pyxel.btn(pyxel.KEY_KP_5):
        return 5
    elif pyxel.btn(pyxel.KEY_KP_6):
        return 6
    elif pyxel.btn(pyxel.KEY_KP_7):
        return 7
    elif pyxel.btn(pyxel.KEY_KP_8):
        return 8
    elif pyxel.btn(pyxel.KEY_KP_9):
        return 9
    else:
        return 0
        
# Etats du jeu
def update():
    global joueur, grille, fin, gagnant
    choix = saisie_clavier()
    if choix in grille and not(gagnant) and not(fin):
        grille = completer_grille(grille,joueur,choix)
        gagnant = gagner_partie(grille)
        fin = fin_partie(grille)
        if not(gagnant):
            joueur = changer(joueur)
        print(choix,joueur,grille)

# Dessin des états de jeu
def draw():
    global grille
    pyxel.cls(7)
    k = 1
    for j in range(3):
        for i in range(3):
            pyxel.rectb(34+i*20,74-j*20,20,20,1)
            if grille[k-1] == 'X':
                pyxel.blt(36+i*20,76-j*20,0,0,0,16,16)
            elif grille[k-1] == 'O':
                pyxel.blt(36+i*20,76-j*20,0,16,0,16,16)
            else:
                pyxel.text(44+i*20,84-j*20,str(grille[k-1]),2)
            k = k + 1
    if joueur == 1:
        couleur = 8
    else:
        couleur = 5
    if gagnant:
        pyxel.text(20,20,f"Le joueur {joueur} gagne !",couleur)
    elif fin:
        pyxel.text(8,20,f"Fin de partie, pas de gagnant !",couleur)
    else:
        pyxel.text(20,20,f"Le joueur {joueur} joue",couleur)
        

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128, title="Projet jeu")

# chargement des images
pyxel.load("morpion.pyxres")

# Lancement de la boucle de jeu
pyxel.run(update,draw)
