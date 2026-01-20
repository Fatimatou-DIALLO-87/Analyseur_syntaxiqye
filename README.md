# Analyseur Syntaxique LL(1) – Mini-langage C (Python)

## 🚀 Présentation du projet
Ce projet consiste à développer un **analyseur syntaxique descendant prédictif LL(1)** pour un mini-langage inspiré du C.  
Réalisé dans le cadre d’un projet de compilation à l’Université de Limoges, il permet de :  
- Vérifier la **validité syntaxique** d’un code source  
- Générer un **arbre syntaxique interactif** via une interface graphique en Python (Tkinter)

Au-delà de l’analyse syntaxique, ce projet met en avant :  
- La mise en œuvre d’**algorithmes**  
- L’utilisation de **structures de données**  
- La **visualisation de structures complexes**  
- La conception d’une **application complète et interactive**  

---

## 🧠 Fonctionnalités principales
- Analyseur descendant prédictif **LL(1)**  
- Vérification de la grammaire avec les ensembles **PREMIER et SUIVANT**  
- Construction de la **table d’analyse syntaxique**  
- Analyse pas à pas des règles de grammaire  
- **Génération et affichage de l’arbre syntaxique**  
- Zoom et déplacement pour gérer les arbres complexes  
- Détection et gestion des **erreurs syntaxiques**  

---

## 📚 Fondements théoriques
L’analyse repose sur une **grammaire validée LL(1)** :  
- **Analyse LL(1)** : grammaire sans conflits, analyse déterministe  
- **Ensembles PREMIER et SUIVANT** :  
  - `PREMIER` identifie les terminaux par lesquels commence un non-terminal  
  - `SUIVANT` détermine quels symboles peuvent apparaître après un non-terminal, y compris les règles vides (ε)  
- **Table d’analyse syntaxique** : associe chaque couple `(non-terminal, terminal)` à la production adéquate (16 règles)  

---

## 🧩 Spécification du langage
Le langage supporte :  
- Déclaration de variables (`int`, `float`)  
- Affectation de valeurs  
- Structures conditionnelles (`if / else`)  

**Extrait simplifié de la grammaire :**

```bnf

Programme          → main(){ Liste_declarations Liste_instructions }
Liste_declarations → Une_declaration Liste_declarations | vide
Une_declaration    → Type id
Liste_instructions → Une_instruction Liste_instructions | vide
Une_instruction    → Affectation | Test
Type               → int | float
Affectation        → id = nombre ;
Test               → if Condition Une_instruction else Une_instruction ;
Condition          → id Operation nombre
Operation          → < | > | ==


```
La grammaire a été validée comme étant **LL(1)**, garantissant une analyse déterministe sans ambiguïté.

---

## 🏗️ Structure du projet

### `Analyseur.py`
- Implémentation de la table d’analyse LL(1)
- Algorithme d’analyse syntaxique descendant
- Utilisation d’une pile pour l’analyse
- Découpage lexical simple de la chaîne d’entrée

### `Arbre.py`
- Construction de l’arbre syntaxique
- Modélisation des nœuds de l’arbre
- Calcul automatique de la disposition des nœuds
- Affichage graphique avec Tkinter (Canvas)
- Gestion du zoom et de la navigation

### `fenetre.py`
- Point d’entrée de l’application
- Gestion de l’interface graphique
- Validation des entrées utilisateur
- Affichage des règles appliquées et de l’arbre

---

## 🧪 Utilisation et tests

L’application permet de :
- détecter une syntaxe incorrecte ou incomplète
- valider une chaîne conforme à la grammaire
- afficher les règles utilisées pendant l’analyse
- visualiser un arbre syntaxique interactif

Exemples de Test
Chaîne Valide : main(){ int id; id=nombre; } (Acceptée par l'analyseur).
Chaîne Invalide : main(){ int id = nombre (Rejetée pour cause de symboles manquants ou mal formés).
Ce projet peut servir à la fois d’**outil pédagogique** et de **démonstration technique**.


---

## ▶️ Apperçu

<p align="center">
  <img src="https://github.com/Fatimatou-DIALLO-87/Analyseur_syntaxiqye/blob/master/analyseur.gif" width="500">
</p>

## 🛠️ Technologies utilisées

- **Python 3**
- **Tkinter**
- Structures de données (pile, arbre, dictionnaires)
- Théorie de la compilation (LL(1), PREMIER / SUIVANT)
