# Ecommerce Project
# 🛒 Django E-commerce Project - IABD 4A

Ce projet est une application de commerce électronique développée avec Django 5.1+. 

## 🚀 Fonctionnalités Actuelles
- **Gestion des Produits** : Affichage d'une liste complète et de détails spécifiques par produit.
- **Système de Catégories** : Organisation des produits par catégories avec navigation dynamique.
- **Interface Admin** : Gestion complète du catalogue (CRUD) via l'espace d'administration Django.
- **Gestion des Médias** : Support pour l'upload et l'affichage des images produits.

## 🛠️ Stack Technique
- **Framework** : Django (Python)
- **Base de données** : SQLite (Développement)
- **Frontend** : HTML5 / Django Template Language (DTL)
- **Environnement** : macOS (M1) / Virtualenv

## 📂 Structure du Projet
```text
.
├── ecommerce/          # Configuration globale du projet
├── products/           # Application principale (Modèles, Vues, Templates)
│   ├── migrations/     # Historique des évolutions de la base de données
│   ├── templates/      # Fichiers HTML (Listes, Détails, Catégories)
│   └── models.py       # Définition des classes Product et Category
├── media/              # Stockage des images téléchargées
└── manage.py           # Point d'entrée des commandes Django

On a créé une relation Many-to-One (Plusieurs-à-Un) entre les produits et les catégories.

Modèle Category : Pour organiser le catalogue.

Modèle Product : Enrichi d'une ForeignKey vers les catégories.

Migrations : Nous avons synchronisé la base de données SQLite pour inclure ces nouvelles colonnes sans perdre tes données existantes.

On a mis en place le "Routing" pour permettre à l'utilisateur de naviguer naturellement :

Listes : Une vue pour tous les produits et une pour toutes les catégories.

Détails : Des vues spécifiques utilisant l'ID (ou PK) pour afficher une page unique par objet (ex: product/2/).

Filtrage : La capacité d'afficher uniquement les produits appartenant à une catégorie précise.

