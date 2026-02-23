# Module Tests

## Raison d'être

Ce répertoire contient tous les tests automatisés de l'application calculatrice. Les tests permettent de :

- Vérifier que chaque opérateur mathématique fonctionne correctement
- Détecter les bogues et régressions dans le code
- S'assurer que l'application web répond correctement aux requêtes
- Valider la gestion des erreurs et des cas limites

### `test_operators.py`

- **Responsabilité** : Tester individuellement chaque fonction du module `operators.py`
- **Couverture** :
  - `TestAdd` : Tests pour l'addition (nombres positifs, négatifs, zéro, décimaux)
  - `TestSubtract` : Tests pour la soustraction (divers cas incluant résultats négatifs)
  - `TestMultiply` : Tests pour la multiplication (tous les cas de signes, zéro, un)
  - `TestDivide` : Tests pour la division (nombres positifs, négatifs, division par zéro)

### `test_app.py`

- **Responsabilité** : Tester l'intégration de l'application Flask et la fonction calculate
- **Couverture** :
  - `TestCalculateFunction` : Tests de la fonction de parsing et calcul
  - `TestFlaskRoutes` : Tests des routes HTTP (GET et POST)
  - Validation des entrées et gestion des erreurs
  - Cas limites et expressions invalides

## Comment exécuter les tests

### Prérequis

Assurez-vous que pytest est installé :

```bash
pip install pytest
```

### Exécuter tous les tests

Depuis la racine du projet :

```bash
pytest tests/
```

Ou depuis le répertoire tests/ :

```bash
cd tests
pytest
```

### Exécuter un fichier de test spécifique

Pour tester uniquement les opérateurs :

```bash
pytest tests/test_operators.py
```

Pour tester uniquement l'application Flask :

```bash
pytest tests/test_app.py
```
## Dépendances

- **pytest** : Framework de tests principal
- **Flask** : Requis pour les tests d'intégration de l'application
