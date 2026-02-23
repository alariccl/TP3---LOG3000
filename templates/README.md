# Module Templates

## Raison d'être

Ce répertoire contient les fichiers de modèles HTML utilisés par l'application Flask. Ces templates définissent l'interface utilisateur de l'application web et permettent le rendu dynamique du contenu côté serveur.

## Fichiers et responsabilités

### `index.html`

- **Responsabilité** : Fichier de modèle principal de l'application
- **Contenu** : Page HTML qui présente l'interface de la calculatrice avec un formulaire permettant à l'utilisateur d'entrer une expression mathématique
- **Variables dynamiques** :
  - `result` : Le résultat du calcul (si disponible) à afficher à l'utilisateur

## Dépendances et hypothèses

- **Flask** : L'application utilise `render_template` de Flask pour rendre ces fichiers
- **CSS** : Les fichiers fait référence à la feuille de style `style.css` du répertoire `static/`
