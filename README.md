# Newwws
------------------


# Table des matières

* [Contexte](#contexte)
* [Technologies](#technologies)
* [Participation](#participation)

## Contexte

**Objectif de l'application:**

Cette application permet à tout utilisateur de rechercher de manière optimale des actualités du jour ou antérieures. L’objectif de cette application est de rendre accessible au plus grand nombre l'informations de manière générale par l'intermédiaire d’une interface intelligible et simple tout en apportant quelques outils de gestion.

**STATUT**: Production

**SERVEUR**: Heroku

**Adresse**: https://newwws-gda.herokuapp.com/

**Version:**
- Version 1: 2021


## Technologies

Pour réaliser cette application, nous nous sommes basés sur les technologies suivantes:
- Python 3.8 (langage)
- Django (frameword back-end python)
- Bootstrap 4 (framework front-end)
- HTML5
- CSS3
- Pipenv (Virtual environment Python)
- Travis (CI)
- Sentry (Logs)
- Selenium / TestCase (test)
- Github

## Participation

1. Créer un répertoire sur votre ordianteur.

2. Effectuer un clône du projet présent sur Github.
```
git clone <url github repo code source>
```

4. Lancer Pipenv et installer les dépendances.
```
pipenv shell
pipenv install
```

5. Configurer une base de données en local.

6. Configuration du projet.
Configurer la variable DATABASES dans settings/__init__.py avec les informations de votre base de données.
Configurer un fichier .env à la racine du projet avec en clé "NEWS_API_KEY" et en valeur votre clé d'API à NewsApi.

7. Effectuer les migrations sur votre base de données.
```
python3 manage.py migrate
```

8. Créer une nouvelle branche de travail.
```
git checkout -b <feature branch>
```

9. Envoyer vos modifications sur github (sans oublier les tests).
```
git add .
git commit -m "New feature"
git push origin -u <feature branch>
```

10. Créer une Pull Request pour validation par les administrateurs.

Et le tour est joué !
