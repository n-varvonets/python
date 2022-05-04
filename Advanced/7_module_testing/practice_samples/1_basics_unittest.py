import unittest

# протестируем функцию создав класс
def test_function(value):
    return value * 20


class UserTestCase(unittest.TestCase):

    # обязательно с префиксом test_
    def test_sum(self):
        """просто пример asssert не тестируя никакую заведумую функцию"""
        # assert 2 + 2 == 4 - могли бы в таком виде записать, но это неинформативно если бы ошибка
        self.assertEqual(2 + 2, 4)  # assertEqual() - при ошибке выдает норм инфу

    def test_multiply(self):
        """просто пример asssert не тестируя никакую заведумую функцию"""
        self.assertTrue(2 * 4 == 8)

    def test_test_function(self):
        """тестируем нашу функцию"""
        value = 100  # передаваемый парам етр в функцию
        self.assertEqual(test_function(value), value * 20)  # сравниваем на равенство test_function(100) между 100 * 20

    def test_test_function_wrong(self):
        value = 100
        self.assertEqual(test_function(value), value * 30)
