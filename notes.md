# Notes pour le projet de dé

## Todo
- [ ] Afficher plusieurs dés en fonction de l'écran
- [ ] Bouton pour relancer les dés
- [ ] Faire une toute petite animation
- [ ] Modifier la forme des dés



### Afficher plusieurs dés en fonction de la taille de l'écran
> Pour cela, je prévois de découper l'écran en plusieurs case de la taille d'un dé  
> Et ensuite de récupérer la position de tous ces centres de case

- On divise donc la taille de l'écran par la taille du dé plus sa bordure (100 + 5)
- On divise la taille de l'écran par 2 pour connaitre les points positifs et les points négatis
> Ex: 1080/2 -> [540; -540], on voit que le bord haut à gauche de l'écran est 540