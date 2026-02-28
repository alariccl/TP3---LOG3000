# TP3 - LOG3000 : Application Calculatrice Web

**Numéro d'équipe :** 9

---

## Description du projet

Cette application est une **calculatrice web simple** développée avec Flask. Elle permet aux utilisateurs d'effectuer des opérations mathématiques de base (+, -, \*, /) via une interface web intuitive.

### Portée et objectifs

Le projet vise à :

- Démontrer la création d'une application web complète avec Flask
- Illustrer les bonnes pratiques de développement Python (documentation, tests, gestion de code)
- Maintenir une codebase bien organisée et maintenable
- Établir un flux de travail collaboratif via Git et GitHub

---

## Objectifs

Ce travail pratique poursuit trois objectifs clés :

1. **Créer et configurer un dépôt GitHub** : Mise en place d'une collaboration en équipe avec version control
2. **Documenter la base de code** : Ajouter des docstrings, commentaires et documentation au niveau des modules
3. **Tester et corriger les bogues** : Implémenter un pipeline de tests et un processus de correction documenté

---

## Guide d'installation

### Prérequis système

Avant de commencer, assurez-vous que votre système dispose de :

- **Git** installé et configuré

- **Python 3.7+** installé

- **pip** (gestionnaire de paquets Python)

- **Un compte GitHub** créé et configuré avec vos clés SSH ou token d'accès personnel

### Étapes d'installation

#### 1. Cloner le dépôt

#### 2. Ouvrir le dossier avec un IDE
---

##  Instructions d'utilisation

### Lancer l'application

Une fois les étapes d'installation complétées, lancez l'application avec :

```bash
python app.py
```

### Accéder à l'application

1. Ouvrez votre navigateur web préféré
2. Naviguez à `http://127.0.0.1:5000`
3. Vous devez voir l'interface de la calculatrice

### Utiliser la calculatrice

1. **Entrez une expression** dans le champ texte avec le format : `nombre opérateur nombre`

2. **Cliquez sur le bouton "="**

3. **Consultez le résultat** affiché sur la calculatrice

## Tests

### Exécuter les tests

Pour exécuter les tests de l'application :

```bash
python -m pytest tests/
```

Ou, si pytest n'est pas installé :

```bash
pip install pytest
python -m pytest tests/
```

---

## Flux de contribution

Ce projet utilise un flux de travail collaboratif standard basé sur Git et GitHub. Veuillez suivre ces étapes pour contribuer.

### 1. Branches Git

Le projet utilise une stratégie de branchage simple :

- **`main`** : Branche principale contenant le code stable et testé
  - Ne faire des commits que via des Pull Requests après révision
- **`dev`** : Branche de développement pour les nouvelles fonctionnalités
  - Point de départ pour les branches de fonctionnalités

- **Branches de travail** : Créez des branches courtes et descriptives pour chaque tâche
  - Format : `feature/nom-feature` ou `feature/fix nom-bug`

### 2. Processus de contribution

#### Étape 1 : Créer une branche

```bash
# Mettez à jour votre copie locale
git pull origin dev

# Créez une nouvelle branche
git checkout -b feature/votre-fonctionnalite
```

#### Étape 2 : Faire vos changements

- Écrivez du code bien documenté
- Ajoutez des docstrings et commentaires clairs
- Respectez les conventions de style Python (PEP 8)

#### Étape 3 : Tester vos changements

```bash
# Exécutez les tests localement
pytest tests/

# Testez manuellement l'application
python app.py
```

#### Étape 4 : Commiter vos changements

```bash
git add .
git commit -m "Courte description de vos changements"
```

**Conventions de messages de commit :**

- Première ligne : Résumé court (50 caractères max)
- Lignes suivantes : Explication détaillée si nécessaire

#### Étape 5 : Pousser et créer une Pull Request

```bash
git push origin feature/votre-fonctionnalite
```

1. Allez sur GitHub
2. Vous verrez une suggestion de créer une Pull Request
3. Cliquez sur **"Compare & pull request"**
4. Remplissez le modèle de PR :
   - Titre descriptif
   - Description des changements
   - Référence aux issues (si applicable)
   - Type de changement (bugfix, feature, documentation)

#### Étape 6 : Révision et fusion

- Attendez la révision d'un autre membre de l'équipe
- Répondez aux commentaires et suggestions
- Un fois approuvé, fusion dans `dev` puis dans `main`, ou directement dans `main`

### Rapport de bogues
Lorsqu’un test échoue :
1. Décrire clairement le problème observé.
2. Fournir les étapes de reproduction.
3. Créer une issue GitHub associée
   
## Suivi des corrections de bogues et validation des tests

Chaque bogue découvert est corrigé sur une branche dédiée, selon le flux Git suivant :
1. Création d’une branche `feature/fix-<nom-du-bogue>`
2. Correction du problème
3. Réexécution du test associé
4. Validation et documentation du résultat

 ### Tableau de suivi des bogues (documentation)

| Issue | Description du bogue | Fichiers concernés | Tests / Vérification | État avant | État après |
| :--- | :--- | :--- | :--- | :---: | :---: |
| #1 | **La soustraction ne marche pas** | `operators.py` | `test_calculate_subtraction`<br>`test_subtract_positive_numbers`<br>`test_subtract_result_negative`<br>`test_subtract_negative_numbers`<br>`test_subtract_zero`<br>`test_subtract_from_zero` | ❌ | ✅ |
| #2 | **La multiplication ne marche pas** | `operators.py` | `test_calculate_multiplication`<br>`test_multiply_positive_numbers`<br>`test_multiply_negative_numbers`<br>`test_multiply_mixed_signs`<br>`test_multiply_by_zero`<br>`test_multiply_decimals` | ❌ | ✅ |
| #3 | **Bogue visuel – boutons affichant des valeurs incorrectes** | `templates/index.html` | Vérification visuelle de l’interface :<br> "02" → "2", "88" → "8", libellés "*" et "/" manquants. | ❌ | ✅ |
| #4 | **La division retourne un entier au lieu d'un float** | `operators.py` | `test_divide_with_remainder` | ❌ | ✅ |

** Score de tests initiaux :** 13 tests échoués sur 41 (28 tests réussis).
** Score de tests finaux :** 0 tests échoués sur 41 (41 tests réussis).
