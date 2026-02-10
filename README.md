# little-games

Mini projet Python contenant **Magic Jars**, un jeu de hasard textuel orienté apprentissage.

## 🎮 Présentation de Magic Jars

Dans un ancien temple, 5 jarres sont posées devant toi à chaque manche :
- certaines contiennent une **clé magique** (`K`) ;
- d'autres cachent un **serpent** (`S`).

Ton objectif est de récupérer assez de clés pour devenir le roi du temple.

## 📜 Règles du jeu

1. Tu choisis une difficulté :
   - `1` = facile (1 serpent, 4 clés)
   - `2` = moyen (2 serpents, 3 clés)
   - `3` = difficile (3 serpents, 2 clés)
2. À chaque manche, les 5 jarres sont mélangées aléatoirement.
3. Tu sélectionnes une jarre entre `1` et `5`.
4. Si tu tombes sur une clé :
   - tu gagnes **+1 clé**.
5. Si tu tombes sur un serpent :
   - tu perds **1 cœur**.
6. Tu gagnes la partie si tu atteins **3 clés** avant de perdre tes **3 cœurs**.

### ✨ Règle bonus ajoutée
- Si tu enchaînes **2 victoires consécutives**, tu obtiens une **clé bonus**.

## 🧠 Conception technique

Le jeu a été restructuré pour être plus propre et plus robuste :

- `ask_level()` : valide la saisie du niveau (1/2/3 uniquement).
- `ask_jar_choice()` : valide le choix de jarre (1 à 5).
- `build_jars(level)` : génère les jarres selon la difficulté puis mélange avec `random.shuffle`.
- `play_game()` : boucle principale de partie (clés, cœurs, combo, victoire/défaite).

### Améliorations apportées

- ✅ Validation des entrées utilisateur (évite les plantages `ValueError`).
- ✅ Ajout d'un système de cœurs (`3 vies`) pour créer une vraie condition de défaite.
- ✅ Ajout d'un bonus combo pour rendre le jeu plus dynamique.
- ✅ Messages de statut plus lisibles à chaque manche.
- ✅ Code découpé en fonctions pour faciliter maintenance et évolutions.

## ▶️ Lancer le jeu

Depuis la racine du projet :

```bash
python3 "the magic jars"
```

## 🚀 Idées d'amélioration futures

- Ajouter un mode "hardcore" avec 4 serpents.
- Masquer/révéler le contenu des jarres avec animation terminale.
- Sauvegarder les scores (nombre de manches, temps, séries de victoire).
- Ajouter une IA simple qui conseille une stratégie (juste pour le fun).

## 🔗 À propos de GitHub

Je peux préparer et structurer le code pour être prêt à pousser sur GitHub (README, commits propres, historique clair).  
En revanche, la connexion directe à ton compte GitHub dépend de ton environnement local (clé SSH/token déjà configuré). Une fois ton remote configuré, un simple `git push` suffira.
