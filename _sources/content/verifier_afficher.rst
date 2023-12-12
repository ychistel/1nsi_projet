Vérifier et afficher
====================

En l'état, le jeu est jouable mais il n'y a aucun contrôle de la partie. Il faut effectuer des vérifications pour éviter un certain nombre d'erreurs:

-   vérifier que la case choisie par le joueur est un nombre entre 1 et 9;
-   vérifier que le joueur ne pose pas de pion sur une case déjà occupée;

Vérifier la saisie
------------------

#.  Dans la fonction de saisie, il faut ajouter un test qui vérifie que la valeur saisie par le joueur est un nombre compris entre 1 et 9. Plusieurs actions sont possibles:

    -   si le joueur saisit une mauvaise valeur, on lui redemande une nouvelle valeur.
    -   si le joueur se trompe, il passe son tour.

    Quelle que soit le choix, il faut traiter cette situation.

#.  Un joueur a posé son pion sur la case 9. L'autre joueur décide de poser son pion sur la case 9. En l'état, c'est tout à fait possible.

    Il faut donc au moment de la saisie ou juste après la saisie vérifier que la case choisie par le joueur n'est pas déjà occupée.

    Si la case est occupée, il faut proposer une alternative! Faire rejouer le joueur ou alors passer son tour.

Afficher la grille
------------------

Le jeu se déroule en console. On peut proposer un affichage de la grille dans la console. Cela se fait avec une succession de ``print``.

.. figure:: ../img/affiche_console.png
    :align: center
    :width: 320px

-   Dessiner une grille en utilisant les caractères ``-``, ``+`` et ``|`` en insérant des espaces!
-   Modifier votre code pour y ajouter les pions 'X' et 'O' des joueurs.
-   Insérer ces lignes d'affichage dans une fonction ``afficher(grille)`` et insérer cette fonction dans lle programme principal.

