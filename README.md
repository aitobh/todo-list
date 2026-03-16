<div align="center">

```
    ___    ______________      __________  ____  ____ 
   /   |  /  _/_  __/ __ \    /_  __/ __ \/ __ \/ __ \
  / /| |  / /  / / / / / /_____/ / / / / / / / / / / /
 / ___ |_/ /  / / / /_/ /_____/ / / /_/ / /_/ / /_/ / 
/_/  |_/___/ /_/  \____/     /_/  \____/_____/\____/  
```

**L'organisation à portée de vous**

---

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)
![Storage](https://img.shields.io/badge/Storage-JSON-f59e0b?style=flat-square)

</div>

---

## 📋 À propos

**AITO-TODO** est un gestionnaire de tâches en ligne de commande, simple et efficace.  
Chaque tâche dispose de sa propre **barre de progression** visuelle, pour un suivi clair directement dans le terminal.

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| ➕ **Créer** | Ajouter une nouvelle tâche instantanément |
| 📋 **Lister** | Afficher toutes les tâches avec leur progression |
| ✏️ **Modifier** | Renommer ou mettre à jour la progression d'une tâche |
| 🗑️ **Supprimer** | Retirer une tâche terminée ou annulée |
| 💾 **Persistance** | Sauvegarde automatique dans un fichier JSON |

---

## 🖥️ Aperçu

<img width="1133" height="644" alt="image" src="https://github.com/user-attachments/assets/28707b37-434a-4084-89c8-26ec569eb01b" />


---

## 🚀 Installation & Lancement

**Aucune dépendance externe requise.** Python standard uniquement.

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/aito-todo.git
cd aito-todo

# 2. Lancer le script
python todo.py
```

> ✅ Compatible **Windows**, **macOS** et **Linux**

---

## 📁 Structure du projet

```
aito-todo/
├── todo.py        ← Script principal
├── tasks.json     ← Données (créé automatiquement)
└── README.md
```

---

## 💾 Format des données

Les tâches sont stockées localement dans `tasks.json` :

```json
[
    {
        "name": "Rédiger le rapport",
        "progress": 50
    },
    {
        "name": "Préparer la présentation",
        "progress": 30
    }
]
```

---

## 🔧 Utilisation

### Ajouter une tâche
```
> 2
Nom de la tâche: Mon projet Python
Tâche ajoutée.
```

### Mettre à jour la progression
```
> 3
[affichage des tâches...]
Numéro de la tâche: 1

1. Modifier le nom
2. Modifier la progression

> 2
Progression (0-100): 75
```

### Supprimer une tâche
```
> 4
[affichage des tâches...]
Numéro à supprimer: 2
Tâche supprimée.
```

---

## 🗺️ Roadmap

- [ ] Ajout de **dates d'échéance**
- [ ] **Catégories** / étiquettes par tâche
- [ ] **Priorités** (haute, moyenne, basse)
- [ ] **Export** en CSV ou TXT
- [ ] Mode **couleurs ANSI** dans le terminal

---

## 📄 Licence

Distribué sous licence **MIT**. Voir `LICENSE` pour plus d'informations.

---

<div align="center">

Fait avec ❤️ et Python 🐍

</div>
