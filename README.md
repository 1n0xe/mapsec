# MAPSEC

MAPSEC est un programme Python conçu pour simplifier et guider les tests de pénétration en fournissant un cadre organisé pour mener des évaluations de sécurité informatique de manière méthodique. Il offre des étapes claires pour chaque phase du pentest, des suggestions d'outils et la possibilité de personnaliser les résultats.

## Table des matières

- [Introduction](#introduction)
- [Utilisation](#utilisation)
  - [Installation](#installation)
  - [Structure](#structure)
  - [Exécution](#exécution)
- [Détails Techniques](#détails-techniques)
  - [Fichiers Principaux](#fichiers-principaux)
  - [Fonctions Clés](#fonctions-clés)
  - [Utilisation de Bibliothèques Python](#utilisation-de-bibliothèques-python)
  - [Personnalisation](#personnalisation)
- [Pour Aller Plus Loin](#pour-aller-plus-loin)
  - [Création d'une Version Plus Complète](#création-dune-version-plus-complète)
  - [Fonctionnalités Supplémentaires](#fonctionnalités-supplémentaires)
  - [Marketing](#marketing)
  - [Version Payante](#version-payante)

## Introduction

Cet outil vise à simplifier le processus de test de pénétration en guidant les utilisateurs à travers les différentes étapes d'une évaluation de sécurité. Il offre une approche structurée qui permet aux pentesters de mener des tests de manière méthodique et organisée. Cet outil a été conçu pour les professionnels de la cybersécurité et les chercheurs en sécurité informatique, ainsi que pour toute personne souhaitant améliorer la sécurité de ses systèmes.

Pour en savoir plus sur l'objectif et les fonctionnalités de l'outil, consultez la [page d'introduction](documentation/introduction.md).

## Utilisation

### Installation

Pour utiliser MAPSEC, vous devez disposer d'un environnement Python fonctionnel sur votre système. Suivez ces étapes pour l'installation :

1. Téléchargez le code source de l'outil à partir du référentiel GitHub.
```
git clone https://github.com/1n0xe/mapsec
```
2. Assurez-vous que Python est installé sur votre système.
3. Ouvrez un terminal dans le répertoire contenant le code source.
4. Exécutez le programme en entrant la commande `python main.py`.

### Structure

L'outil est organisé en plusieurs fichiers, chacun correspondant à une phase spécifique du test de pénétration. Voici la structure du répertoire :

- `main.py` : Point d'entrée de l'application, guide les utilisateurs à travers les différentes étapes.
- `enumeration.py` : Phase d'énumération, collecte des informations sur la cible.
- `identification.py` : Phase d'identification, identifie les services et les ports ouverts.
- `detection.py` : Phase de détection, recherche de vulnérabilités potentielles.
- `exploitation.py` : Phase d'exploitation, analyse les possibilités d'exploitation.
- `post_exploitation.py` : Phase de post-exploitation, présente les options de persistance et d'élévation de privilèges.

### Exécution

Lorsque vous exécutez `main.py`, l'outil affiche un menu interactif qui permet à l'utilisateur de choisir l'étape à partir de laquelle il souhaite commencer le test de pénétration. Chaque étape est guidée par des instructions claires, des suggestions d'outils et la possibilité de personnaliser les résultats.

Pour plus de détails sur l'utilisation de l'outil, consultez la [page d'utilisation](documentation/utilisation.md).

## Détails Techniques

### Fichiers Principaux

1. `main.py` : Point d'entrée du programme. Il guide l'utilisateur à travers les différentes étapes du test de pénétration.
2. `enumeration.py` : Contient les fonctions pour la collecte d'informations sur la cible.
3. `identification.py` : Contient les fonctions pour identifier les services et les ports ouverts.
4. `detection.py` : Contient les fonctions pour détecter les vulnérabilités potentielles.
5. `exploitation.py` : Contient les fonctions pour explorer les options d'exploitation.
6. `post_exploitation.py` : Contient les fonctions pour présenter les options de post-exploitation.

### Fonctions Clés

- `run_enumeration()` (enumeration.py) : Gère la phase d'énumération, collecte des informations sur la cible.
- `run_identification()` (identification.py) : Gère la phase d'identification, identifie les services et les ports ouverts.
- `run_detection()` (detection.py) : Gère la phase de détection, recherche de vulnérabilités potentielles.
- `run_exploitation()` (exploitation.py) : Gère la phase d'exploitation, analyse les possibilités d'exploitation.
- `run_post_exploitation()` (post_exploitation.py) : Gère la phase de post-exploitation, présente les options de persistance et d'élévation de privilèges.

### Utilisation de Bibliothèques Python

L'outil utilise principalement les fonctionnalités de base de Python pour interagir avec l'utilisateur et gérer les étapes du test de pénétration. Les fonctions `input()` et `print()` sont utilisées pour l'interaction en ligne de commande. Les listes et les dictionnaires sont employés pour stocker les données.

### Personnalisation

Les fichiers `detection.py` et `exploitation.py` sont conçus pour être personnalisables en fonction des besoins de l'utilisateur. Vous pouvez modifier les outils de détection et d'exploitation, ajouter de nouvelles options et personnaliser les descriptions.

Pour des détails complets sur les détails techniques de l'outil, consultez la [page des détails techniques](documentation/details_techniques.md).

---

**MAPSEC** est un projet en évolution constante. Votre contribution, vos idées et vos commentaires sont les bienvenus pour améliorer l'outil et en faire une ressource précieuse pour les professionnels de la sécurité informatique.

Pour des détails complets sur l'outil, veuillez consulter la documentation détaillée dans le répertoire [documentation](documentation/).

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

