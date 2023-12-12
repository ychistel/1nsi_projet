Coder le jeu en Python
======================

Une fois l'organigramme (graphe) du déroulement du jeu créé, il est temps de définir les variables, les fonctions et la structure du programme principal.

Variables
---------

-  On doit représenter la grille par un tableau de 9 valeurs. Chaque valeur peut être associée aux touches du clavier numérique.
-  Le joueur doit être identifié pour savoir la forme du pion à poser. On prend une variable de type nombre entier.
-  La fin de partie se produit dans 2 cas. Il n'y plus de case libre pour poser un pion ou un joueur a gagné la partie en alignant ses pions. Ces 2 variables sont de type booléen.

On crée les 4 variables : 

.. code:: Python

    grille = [...] # grille de type tableau
    joueur = ... # nombre entier qui identifie le joueur
    gagnant = False # booleen qui indique si un joueur a gagné
    fin = False # booléen qui indique la fin de partie

Les fonctions
-------------

Certaines étapes du jeu sont traitées par des fonctions. Voici les principales fonctions à créer:

-   La saisie d'un joueur doit être mémorisée et renvoyée au programme principal. La fonction ``saisir(j)`` attend une valeur comprise entre 1 et 9 correspondant à la case de la grille à recouvrir d'un pion. La fonction renvoie la valeur saisie. On donne la fonction ci-dessous:

    .. code:: Python

        def saisir(j):
            print(f"Joueur {j} joue")
            c = int(input("Quelle case joues-tu ? "))
            return c

-   La grille se complète avec des pions posés par les 2 joueurs. Cela revient à ajouter la valeur 'X' ou 'O' selon le joueur dans la grille du jeu. Attention la valeur doit être ajoutée au bon endroit dans le tableau. On donne la première ligne de la fonction:

    .. code:: Python

        def completer_grille(grille,j,c):
            """
            grille : tableau contenant la grille de jeu
            j : identifian du joueur
            c : case sur laquelle le pion est à poser
            """
            ...

-   Après chaque coup joué, il faut vérifier si les pions du joueur sont alignés. S'ils sont alignés, la partie est finie, sinon la partie se poursuit en changeant de joueur. La fonction ``gagner_partie`` renvoie un ``booléen``. Elle renvoie ``True`` si la grille contient un alignement de pions et ``False`` dans le cas contraire.

    .. code:: Python

        def gagner_partie(grille):
            """"
            Teste si la grille contient des pions alignés. Elle renvoie un booléen True ou False selon les cas.
            """
            ...

-   Après chaque coup joué, non gagnant, on doit vérifier si le joueur suivant peut jouer. Cela revient à vérifier que la grille peut accepter un pion. La fonction ``fin_partie`` renvoie un ``booléen``. Elle renvoie ``True`` si le joueur suivant peut jouer et ``False`` dans le cas contraire.

    .. code:: Python

        def fin_partie(grille):
            """"
            Renvoie True si on peut ajouter 'X' ou 'O' dans la grille
            Renvoie False dans le cas contraire.
        """

-   La fonction ``changer`` renvoie l'identifiant du prochain joueur qui doit jouer son pion.

    .. code:: Python

        def changer(j):
            """
            Renvoie l'identifiant qui n'est pas celui de j.
            """
            ...

Le programme principal
----------------------

Une partie se déroule tant qu'elle est jouable et tant qu'il n'y a pas de vainqueur. Le programme principal tient en une boucle ``while``.

Dans cette boucle, le même scénario se répète :

-   le joueur chosit une place dans la grille;
-   on complète la grille avec le pion 'X' ou 'O' du joueur;
-   on vérifie si le joueur a gagné
-   si le joueur n'a pas gagné, on vérifie si on peut encore jouer sur la grille;
-   si on peut encore jouer, on change de joueur et on continue la partie

On quitte la boucle de jeu lorsqu'il y a un gagnant ou si la grille n'est plus jouable.