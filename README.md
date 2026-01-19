# Analyseur Syntaxique LL(1) – Mini langage C (Python)

## 🚀 Présentation du projet

Ce projet est un **analyseur syntaxique LL(1)** pour un mini-langage inspiré du langage C, développé en **Python** avec une **interface graphique en Tkinter**.  
Il prend en entrée une chaîne représentant un programme, vérifie sa validité syntaxique et génère **l’arbre syntaxique associé**.

Au-delà de l’analyse syntaxique, ce projet met en avant :
- la mise en œuvre d’algorithmes
- l’utilisation de structures de données
- la visualisation de structures complexes
- la conception d’une application complète et interactive

---

## 🧠 Fonctionnalités principales

- Analyseur descendant prédictif **LL(1)**
- Vérification de la grammaire à l’aide des ensembles **PREMIER et SUIVANT**
- Implémentation de la table d’analyse syntaxique
- Application pas à pas des règles de grammaire
- **Génération et affichage de l’arbre syntaxique**
- Gestion du zoom et du déplacement pour les arbres complexes
- Détection et gestion des erreurs syntaxiques

---

🧠 Fondements Théoriques:
Le moteur de l'analyse repose sur une grammaire rigoureusement validée :
Analyse LL(1) : La grammaire a été vérifiée manuellement pour garantir l'absence de conflits, permettant une analyse déterministe
Ensembles PREMIER et SUIVANT : Le calcul de ces ensembles a permis de construire une table d'analyse précise
Les PREMIER identifient les terminaux par lesquels commence un non-terminal.
Les SUIVANT déterminent quels symboles peuvent apparaître après un non-terminal, gérant ainsi les règles vides ($\epsilon$)
6.Table d'Analyse :
Une structure de 16 règles numérotées guide l'algorithme pour associer chaque couple (non-terminal, terminal) à la production adéquate

---
## 🧩 Spécification du langage

Le langage pris en charge permet :
- la déclaration de variables (`int`, `float`)
- l’affectation de valeurs
- les structures conditionnelles (`if / else`)

Extrait simplifié de la grammaire :

Programme → main() { Déclarations Instructions }   <br>
Déclarations → Déclaration Déclarations | ε        <br>
Déclaration → Type id                        <br>
Instructions → Instruction Instructions | ε    <br>
Instruction → Affectation | Test              <br>
Affectation → id = nombre ;                  <br>
Test → if Condition Instruction else Instruction    <br>
Condition → id Opérateur nombre                 <br>
Opérateur → < | > | ==                    <br>
<br>

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

## 🛠️ Technologies utilisées

- **Python 3**
- **Tkinter**
- Structures de données (pile, arbre, dictionnaires)
- Théorie de la compilation (LL(1), PREMIER / SUIVANT)

---

## ▶️ Apperçu
# ![Fatimatou](https://github.com/Fatimatou-DIALLO-87/Analyseur_syntaxiqye/blob/master/analyseur.gif)

