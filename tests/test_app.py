import sys
import os

# Ajouter le répertoire parent au path pour importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app, calculate


@pytest.fixture
def client():
    """
    Fixture pytest pour créer un client de test Flask.

    Retourne un client de test qui peut effectuer des requêtes
    vers l'application sans la démarrer réellement.

    Yields:
        FlaskClient: Client de test Flask configuré en mode test.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestCalculateFunction:
    """Tests pour la fonction calculate."""

    def test_calculate_addition(self):
        """
        Teste le calcul d'une addition simple.

        Vérifie que "5 + 3" retourne 8.
        """
        result = calculate("5 + 3")
        assert result == 8, f"Expected 8, got {result}"

    def test_calculate_subtraction(self):
        """
        Teste le calcul d'une soustraction.

        Vérifie que "10 - 4" retourne 6.
        """
        result = calculate("10 - 4")
        assert result == 6, f"Expected 6, got {result}"

    def test_calculate_multiplication(self):
        """
        Teste le calcul d'une multiplication.

        Vérifie que "4 * 5" retourne 20.
        """
        result = calculate("4 * 5")
        assert result == 20, f"Expected 20, got {result}"

    def test_calculate_division(self):
        """
        Teste le calcul d'une division.

        Vérifie que "20 / 4" retourne 5.
        """
        result = calculate("20 / 4")
        assert result == 5, f"Expected 5, got {result}"

    def test_calculate_with_spaces(self):
        """
        Teste le calcul avec des espaces dans l'expression.

        Vérifie que les espaces sont ignorés correctement.
        """
        result = calculate("  10   +   5  ")
        assert result == 15, f"Expected 15, got {result}"

    def test_calculate_without_spaces(self):
        """
        Teste le calcul sans espaces dans l'expression.

        Vérifie que "10+5" retourne 15.
        """
        result = calculate("10+5")
        assert result == 15, f"Expected 15, got {result}"

    def test_calculate_with_decimals(self):
        """
        Teste le calcul avec des nombres décimaux.

        Vérifie que "5.5 + 2.3" fonctionne correctement.
        """
        result = calculate("5.5 + 2.3")
        expected = 7.8
        assert abs(result - expected) < 0.0001, f"Expected {expected}, got {result}"

    def test_calculate_empty_expression(self):
        """
        Teste le comportement avec une expression vide.

        Doit lever une ValueError.
        """
        with pytest.raises(ValueError, match="empty expression"):
            calculate("")

    def test_calculate_none_expression(self):
        """
        Teste le comportement avec None comme expression.

        Doit lever une ValueError.
        """
        with pytest.raises(ValueError, match="empty expression"):
            calculate(None)

    def test_calculate_multiple_operators(self):
        """
        Teste le comportement avec plusieurs opérateurs.

        Vérifie qu'une erreur est levée pour "5 + 3 - 2".
        """
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("5 + 3 - 2")

    def test_calculate_operator_at_start(self):
        """
        Teste le comportement avec un opérateur au début.

        Vérifie qu'une erreur est levée pour "+ 5".
        """
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+ 5")

    def test_calculate_operator_at_end(self):
        """
        Teste le comportement avec un opérateur à la fin.

        Vérifie qu'une erreur est levée pour "5 +".
        """
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("5 +")

    def test_calculate_no_operator(self):
        """
        Teste le comportement sans opérateur.

        Vérifie qu'une erreur est levée pour "123".
        """
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("123")

    def test_calculate_invalid_operand(self):
        """
        Teste le comportement avec un opérande invalide.

        Vérifie qu'une erreur est levée pour "abc + 5".
        """
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("abc + 5")


class TestFlaskRoutes:
    """Tests pour les routes Flask de l'application."""

    def test_homepage_get(self, client):
        """
        Teste la requête GET sur la page d'accueil.

        Vérifie que la page charge correctement avec un code 200.

        Args:
            client: Fixture du client de test Flask.
        """
        response = client.get("/")
        assert response.status_code == 200
        # Vérifie que la réponse contient du HTML
        assert b"html" in response.data.lower()

    def test_homepage_post_valid_expression(self, client):
        """
        Teste une requête POST avec une expression valide.

        Vérifie que le calcul est effectué et le résultat retourné.

        Args:
            client: Fixture du client de test Flask.
        """
        response = client.post("/", data={"display": "5 + 3"})
        assert response.status_code == 200
        # Le résultat devrait être présent dans la réponse
        assert b"8" in response.data or b"8.0" in response.data

    def test_homepage_post_invalid_expression(self, client):
        """
        Teste une requête POST avec une expression invalide.

        Vérifie qu'un message d'erreur est retourné.

        Args:
            client: Fixture du client de test Flask.
        """
        response = client.post("/", data={"display": "abc + def"})
        assert response.status_code == 200
        # Un message d'erreur devrait être présent
        assert b"Error" in response.data

    def test_homepage_post_empty_expression(self, client):
        """
        Teste une requête POST avec une expression vide.

        Vérifie qu'un message d'erreur approprié est retourné.

        Args:
            client: Fixture du client de test Flask.
        """
        response = client.post("/", data={"display": ""})
        assert response.status_code == 200
        assert b"Error" in response.data

    def test_homepage_post_division_by_zero(self, client):
        """
        Teste une requête POST avec une division par zéro.

        Vérifie qu'une erreur appropriée est gérée.

        Args:
            client: Fixture du client de test Flask.
        """
        response = client.post("/", data={"display": "10 / 0"})
        assert response.status_code == 200
        assert b"Error" in response.data
