"""Почему PyCharm показывает, что
Во-первых, модуль pytest не установлен, хотя он установлен;
Во-вторых, команда модуль pytest не используется в коде и все тесты запускаются, даже когда я удаляю команду импорта

И в чем преимущество использования статических методов, которое мне навязывает PyCharm?"""

import pytest

from calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(7, 4) == 11

    def test_multiply_success(self):
        assert self.calc.multiply(5, 8) == 40

    def test_division_success(self):
        assert self.calc.division(24, 8) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(7, 2) == 5

    def teardown(self):
        print(' Выполнение метода Teardown')
