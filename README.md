# WebTesterX - La révolution du tester

Bienvenue dans le README du projet WebTesterX ! Vous trouverez ici toutes les informations essentielles pour comprendre et utiliser notre application révolutionnaire de tests de connectivité des serveurs web.

# Présentation du projet

WebTesterX a pour objectif de simplifier les tests de connectivité d'un ou plusieurs serveurs web. Il s'agit d'un projet gratuit et open-source, développé par Hoag et Eagle_ en Python.

# Structure

Le projet est divisé en deux applications différentes. Une application GUI (Graphical User Interface) développée par Amaury et une application CLI (Command Line Interface) développée par Maël.

Puis-ce que les deux applications fonctionnent de la meme maniere, pour eviter les doublons, toutes les fonctions sont reunis dans un seul fichier, pour que les applications puissent les appeler.

Pour faciliter l'utilisation, nous avons créé un fichier "requirements.txt". L'utilisateur aura juste à exécuter la commande suivante pour installer les dépendances nécessaires :

```shell
pip install -r PATH/TO/REQUIREMENTS.txt
```
Le ficher sert à installer toutes les librairies necesssaires en une seule commande. Soit :
| Nom de la librairie | Commande d'installation | Utilisation |
|----------------------|----------------------|----------------------|
| Requests | pip install requests | Pouvoir atteindre un serveur via la methode Requests |
| TermColor | pip install thermcolor | Pouvoir metrre des couleurs dans le terminal |
| argparse | pip install argparse | Pouvoir faciliter le traitement de d'arguments en ligne de commande |
| ping3 | pip install ping3 | Pouvoir atteindre un serveur via la methode Ping |

------------------
Chaque evenement est enregistrer dans un fichier .log afin de pouvoir debug si besoin.
```file
webtesterx.log
```

---------
Nous avons creer 2 methods, la premiere ```Ping``` , interroger le serveur via des pings pour verifier qu'il est accessible, et la deuxieme, ```Requests``` essaye juste d'atteindre le serveur.

- Pour la methode Ping, nous utilisons la librairie ```Subprocess``` pour executer la commande "ping" un certain nombre de fois en tache de fond.

- Pour la methode Requests, nos utilisons la librairie ```Requests``` de python. Cette librairie cherche simplement à atteindre le server en tant que robot.

# GUI 
Pour faire cette interface graphique, nous avons utilisé Tkinter, Tkinter est une bibliothèque Python qui permet de créer des interfaces utilisateur graphiques faciles à utiliser et esthétiques. Une interface White Mode, simple d'utilisation. A gauche, un champ de saisie, et des boutons radio pour choisir la methode (Ping/Requests). A droite, une zone de texte, la zone ou sera affiché tout les resultats des requetes.

![image](https://i.imgur.com/Qoc5HhL.png)


# CLI
Pour notre Application CLI, nous avons utilisé le modele d'une commande avec des arguments

Pour ajouter l'URL, il sufit d'utiliser l'argument ```--url```.

```
python3 CLI.py --url https://example.com/
```

Pour choisir la methode, il sufit d'utiliser l'argument ```-p``` pour utiliser la methode PING, et ```-r``` our la methode Requests.

Exemple :
```
python3 CLI.py --url https://example.com/ -r
```
## OU ##
```
python3 CLI.py --url https://example.com/ -p 4
```
----
Par rapport à l'application GUI, il y a plus de possibilités.
Il y a déjà la possibilité d'importer une liste de serveurs à tester qui ressemble à quelque chose comme ca :
```
example.com
double-t.fr
https://prod.double-t.fr/
https://chat.openai.com/
monsitesupercool.net
```
La liste peut etre appellé via cette commande :
```
python3 CLI.py --list PATH/TO/LIST.txt
```

## Recapitulatif des commandes :

| Argument | Utilisation                                           |
|----------|-------------------------------------------------------|
| --help   | Affiche documentation                                 |
| --url    | Entrer lien du serveur à tester.                      |
| --list   | Entrer une liste de l'utilisateur                     |
| -p       | Atteindre le serveur via la methode Ping              |
| -r       | Tester avec la methode requests                       |
| -t       | Preciser un timeout si on utilise la methode Requests | 

![image](https://i.imgur.com/mb6viQl.png)
