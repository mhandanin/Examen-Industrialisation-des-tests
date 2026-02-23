# Tests Automatisés Selenium - Exercices 1 & 2

##  Description

Ce projet contient des tests automatisés en Python avec Selenium pour deux exercices :

- **Exercice 1** : Tests de login/authentification
- **Exercice 2** : Tests d'extraction d'informations d'un site e-commerce

##  Installation

### Prérequis
- Python 3.10+
- Git

### 1. Cloner le repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

##  Exécuter les Tests Localement

### Exécuter tous les tests
```bash
pytest
```

### Exécuter les tests de l'exercice 1
```bash
pytest test_exercice1.py -v
```

### Exécuter les tests de l'exercice 2
```bash
pytest test_exercice2.py -v
```

### Exécuter un test spécifique
```bash
pytest test_exercice1.py::TestExercice1::test_login_success -v
```

### Afficher la couverture des tests
```bash
pip install pytest-cov
pytest --cov=.
```

##  Tests Disponibles

### Exercice 1 - Login Tests (3 tests)
- `test_login_success` : Teste la connexion avec les bonnes identifiants
- `test_login_invalid_username` : Teste la réaction à un mauvais username
- `test_login_invalid_password` : Teste la réaction à un mauvais password

### Exercice 2 - Web Scraping Tests (5 tests)
- `test_books_page_loads` : Vérifie que la page se charge
- `test_books_list_found` : Vérifie la présence d'une liste de livres
- `test_books_extraction_first_20` : Vérifie l'extraction de 20 livres
- `test_books_contain_required_info` : Vérifie que toutes les infos sont extraites
- `test_first_book_details` : Teste les détails du premier livre

##  Exécution avec GitHub Actions

Les tests s'exécutent automatiquement sur chaque push ou pull request.

### Résultats
Les résultats des tests sont disponibles dans l'onglet **Actions** du repository GitHub.

### Configuration
Le workflow est défini dans `.github/workflows/tests.yml`

##  Dépendances

- **selenium** : Automatisation web
- **webdriver-manager** : Gestion automatique des drivers Chrome
- **pytest** : Framework de test
- **pytest-timeout** : Limitation du temps d'exécution

##  Configuration

Les paramètres pytest sont définis dans `pytest.ini`.

##  Dépannage

### Chrome driver non trouvé
Si vous rencontrez une erreur avec ChromeDriver, webdriver-manager le téléchargera automatiquement.

### Tests trop lents
Augmentez le timeout dans `pytest.ini` si nécessaire.

### Erreurs de connexion
Vérifiez votre connexion Internet pour accéder aux sites de test.

##  Notes

- Les tests utilisent des sites de test publiques (the-internet.herokuapp.com, books.toscrape.com)
- Aucune modification de données réelles n'est effectuée
- Les tests sont conçus pour être exécutés en local ou en CI/CD

##  Statut des Tests

- **Exercice 1** :  3/3 tests passants
- **Exercice 2** :  5/5 tests passants

---

**Total** : **8 tests** - **100% passants**
