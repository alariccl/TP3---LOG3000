# Module Static

## Raison d'être

Ce répertoire contient les fichiers statiques servant à la présentation et à l'interface utilisateur de l'application web. Ces ressources (CSS, JavaScript, images, polices, etc.) sont servies directement par Flask sans traitement dynamique.

## Fichiers et responsabilités

### `style.css`

- **Responsabilité** : Feuille de style principale de l'application
- **Contenu** : Définit le style et la mise en page de l'interface utilisateur

## Dépendances et hypothèses

- **Flask** : L'application configure automatiquement les fichiers statiques dans le répertoire `static/` via `Flask(__name__)`
- **HTTP** : Les fichiers sont servis avec les en-têtes HTTP appropriés pour le cache et la compression
- **CSS3** : La feuille de style utilise les normes CSS modernes
