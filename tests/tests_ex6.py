"""
Tests para la función fun_total_goals del ejercicio 6.
"""
import os
import sys
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from exercises.ex6 import fun_total_goals


class TestFunTotalGoals(unittest.TestCase):
    """Tests unitarios para la función fun_total_goals."""

    @classmethod
    def setUpClass(cls):
        """Carga el dataset una sola vez para todos los tests."""
        data_path = os.path.join(
            os.path.dirname(__file__), "..", "src", "data", "LaLiga_Matches.csv"
        )
        data = pd.read_csv(data_path)
        cls.data = data.drop(columns=["HTHG", "HTAG", "HTR"])

    def test_returns_tuple_of_three(self):
        """Verifica que la función devuelve una tupla de tres elementos."""
        result = fun_total_goals(self.data)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_returns_integers(self):
        """Verifica que los tres valores devueltos son enteros."""
        home_goals, away_goals, total_goals = fun_total_goals(self.data)
        self.assertIsInstance(home_goals, int)
        self.assertIsInstance(away_goals, int)
        self.assertIsInstance(total_goals, int)

    def test_total_equals_sum(self):
        """Verifica que total_goals es la suma de home_goals y away_goals."""
        home_goals, away_goals, total_goals = fun_total_goals(self.data)
        self.assertEqual(total_goals, home_goals + away_goals)

    def test_home_goals_value(self):
        """Verifica el valor exacto de los goles locales."""
        home_goals, _, _ = fun_total_goals(self.data)
        self.assertEqual(home_goals, 18040)

    def test_away_goals_value(self):
        """Verifica el valor exacto de los goles visitantes."""
        _, away_goals, _ = fun_total_goals(self.data)
        self.assertEqual(away_goals, 13053)

    def test_total_goals_value(self):
        """Verifica el valor exacto del total de goles."""
        _, _, total_goals = fun_total_goals(self.data)
        self.assertEqual(total_goals, 31093)

    def test_home_goals_greater_than_away(self):
        """Verifica que los locales marcan más goles que los visitantes."""
        home_goals, away_goals, _ = fun_total_goals(self.data)
        self.assertGreater(home_goals, away_goals)


if __name__ == "__main__":
    unittest.main()
