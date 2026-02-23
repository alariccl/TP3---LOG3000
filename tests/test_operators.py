import sys
import os

# Ajouter le répertoire parent au path pour importer les modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from operators import add, subtract, multiply, divide


class TestAdd:
    """Tests pour la fonction d'addition."""

    def test_add_positive_numbers(self):
        """
        Teste l'addition de deux nombres positifs.

        Vérifie que 2 + 3 = 5.
        """
        result = add(2, 3)
        assert result == 5, f"Expected 5, got {result}"

    def test_add_negative_numbers(self):
        """
        Teste l'addition de deux nombres négatifs.

        Vérifie que -2 + -3 = -5.
        """
        result = add(-2, -3)
        assert result == -5, f"Expected -5, got {result}"

    def test_add_mixed_signs(self):
        """
        Teste l'addition d'un nombre positif et d'un nombre négatif.

        Vérifie que -2 + 3 = 1.
        """
        result = add(-2, 3)
        assert result == 1, f"Expected 1, got {result}"

    def test_add_zero(self):
        """
        Teste l'addition avec zéro.

        Vérifie que 5 + 0 = 5.
        """
        result = add(5, 0)
        assert result == 5, f"Expected 5, got {result}"

    def test_add_floats(self):
        """
        Teste l'addition de nombres décimaux.

        Vérifie que 2.5 + 3.7 = 6.2.
        """
        result = add(2.5, 3.7)
        assert abs(result - 6.2) < 0.0001, f"Expected 6.2, got {result}"


class TestSubtract:
    """Tests pour la fonction de soustraction."""

    def test_subtract_positive_numbers(self):
        """
        Teste la soustraction de deux nombres positifs.

        Vérifie que 5 - 3 = 2.
        """
        result = subtract(5, 3)
        assert result == 2, f"Expected 2, got {result}"

    def test_subtract_result_negative(self):
        """
        Teste la soustraction donnant un résultat négatif.

        Vérifie que 3 - 5 = -2.
        """
        result = subtract(3, 5)
        assert result == -2, f"Expected -2, got {result}"

    def test_subtract_negative_numbers(self):
        """
        Teste la soustraction avec des nombres négatifs.

        Vérifie que -5 - (-3) = -2.
        """
        result = subtract(-5, -3)
        assert result == -2, f"Expected -2, got {result}"

    def test_subtract_zero(self):
        """
        Teste la soustraction avec zéro.

        Vérifie que 10 - 0 = 10.
        """
        result = subtract(10, 0)
        assert result == 10, f"Expected 10, got {result}"

    def test_subtract_from_zero(self):
        """
        Teste la soustraction à partir de zéro.

        Vérifie que 0 - 5 = -5.
        """
        result = subtract(0, 5)
        assert result == -5, f"Expected -5, got {result}"


class TestMultiply:
    """Tests pour la fonction de multiplication."""

    def test_multiply_positive_numbers(self):
        """
        Teste la multiplication de deux nombres positifs.

        Vérifie que 4 * 5 = 20.
        """
        result = multiply(4, 5)
        assert result == 20, f"Expected 20, got {result}"

    def test_multiply_negative_numbers(self):
        """
        Teste la multiplication de deux nombres négatifs.

        Vérifie que -4 * -5 = 20.
        """
        result = multiply(-4, -5)
        assert result == 20, f"Expected 20, got {result}"

    def test_multiply_mixed_signs(self):
        """
        Teste la multiplication d'un nombre positif et d'un nombre négatif.

        Vérifie que -4 * 5 = -20.
        """
        result = multiply(-4, 5)
        assert result == -20, f"Expected -20, got {result}"

    def test_multiply_by_zero(self):
        """
        Teste la multiplication par zéro.

        Vérifie que 5 * 0 = 0.
        """
        result = multiply(5, 0)
        assert result == 0, f"Expected 0, got {result}"

    def test_multiply_by_one(self):
        """
        Teste la multiplication par un (identité).

        Vérifie que 7 * 1 = 7.
        """
        result = multiply(7, 1)
        assert result == 7, f"Expected 7, got {result}"

    def test_multiply_decimals(self):
        """
        Teste la multiplication de nombres décimaux.

        Vérifie que 2.5 * 4 = 10.
        """
        result = multiply(2.5, 4)
        assert abs(result - 10.0) < 0.0001, f"Expected 10.0, got {result}"


class TestDivide:
    """Tests pour la fonction de division."""

    def test_divide_positive_numbers(self):
        """
        Teste la division de deux nombres positifs.

        Vérifie que 20 / 4 = 5.
        """
        result = divide(20, 4)
        assert result == 5, f"Expected 5, got {result}"

    def test_divide_negative_numbers(self):
        """
        Teste la division de deux nombres négatifs.

        Vérifie que -20 / -4 = 5.
        """
        result = divide(-20, -4)
        assert result == 5, f"Expected 5, got {result}"

    def test_divide_mixed_signs(self):
        """
        Teste la division d'un nombre positif par un nombre négatif.

        Vérifie que 20 / -4 = -5.
        """
        result = divide(20, -4)
        assert result == -5, f"Expected -5, got {result}"

    def test_divide_with_remainder(self):
        """
        Teste la division avec reste.

        Vérifie que 10 / 3 = 3.333...
        """
        result = divide(10, 3)
        expected = 10 / 3
        assert abs(result - expected) < 0.0001, f"Expected {expected}, got {result}"

    def test_divide_zero_by_number(self):
        """
        Teste la division de zéro par un nombre.

        Vérifie que 0 / 5 = 0.
        """
        result = divide(0, 5)
        assert result == 0, f"Expected 0, got {result}"

    def test_divide_by_zero(self):
        """
        Teste la division par zéro (doit lever une exception).

        Vérifie que la division par zéro lève une ZeroDivisionError.
        """
        try:
            result = divide(10, 0)
            # Si on arrive ici, le test échoue car aucune exception n'a été levée
            assert False, "Expected ZeroDivisionError but no exception was raised"
        except ZeroDivisionError:
            # C'est le comportement attendu
            pass
