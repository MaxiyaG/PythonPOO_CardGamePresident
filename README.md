## Développeur : 
- MaxiyaG
- Site Web : https://maxiya-web.vercel.app/
 
# Jeu du Président

Ce projet est une implémentation du jeu de cartes populaire, le Président, en Python. Il a été développé par MaxiyaG.

## Description

Le jeu du Président se joue à plusieurs (de 3 à 5 joueurs). C’est un jeu de défausse en plusieurs manches, le gagnant est le premier qui n’a plus de carte en main à la fin de la manche, il devient "Président". Pour la seconde manche et pourra choisir 2 cartes à donner à un autre joueur.

## Prérequis

Pour exécuter ce projet, vous devez avoir Python 3.10 ou une version ultérieure installée sur votre machine. Vous pouvez vérifier votre version de Python en ouvrant un terminal et en exécutant la commande suivante :

```bash
python --version
```
Si vous n'avez pas Python installé ou si votre version est inférieure à 3.10, veuillez visiter le site officiel de Python pour télécharger et installer la dernière version de Python.

## Installation
1- Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :
```bash
git clone https://github.com/MaxiyaG/President.git
```
2- Naviguez jusqu'au répertoire du projet :
```bash
cd President
```

## Exécution du projet

### Windows

Ouvrez un terminal (invite de commandes) et exécutez la commande suivante :

```bash
python main.py
```

### Mac & Linux
Ouvrez un terminal et exécutez la commande suivante :
```bash
python3 main.py
```

## Structure du projet
Le projet est structuré comme suit :  

- main.py : Le point d'entrée du jeu. Il crée une instance du jeu et le démarre.
- Class/Joueur/Joueur.py : Définit la classe Joueur, qui représente un joueur dans le jeu.
- Class/Jeu/Jeu.py : Définit la classe Jeu, qui gère le déroulement du jeu.
- Class/Jeu/Tour.py : Définit la classe Tour, qui représente un tour dans le jeu.
- Class/Carte/Carte.py : Définit la classe Carte, qui représente une carte dans le jeu.
- Class/Carte/Paquet.py : Définit la classe Paquet, qui représente un paquet de cartes.

## Comment jouer
Lorsque vous exécutez le jeu, vous serez invité à entrer le nombre de joueurs et le nombre de cartes par joueur. Ensuite, le jeu commencera et chaque joueur jouera à tour de rôle.  

## Licence
Ce projet est sous licence MIT.

