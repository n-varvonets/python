import unittest
import datetime


class UserTestCase(unittest.TestCase):
    """
    В классе 2 тестовых метода (префикс test_)
    """

    def setUp(self):
        """
        setUp будет вызываться каждый раз ПЕРЕД выполнением какого-то теста.
        Т.е. в setUp мы можем реализовать логику создания тест-данных для каждого теста.
        """
        print('setUp')
        self.current = datetime.datetime.now()

    @classmethod
    def setUpClass(cls):
        """
        setUpClass вызывается единожды при инициализации нашего класса, что бы правильно настроить окр
        """
        cls.current_cls = datetime.datetime.now()
        print('setUpClass')

    def tearDown(self):
        """tearDown будет вызываться каждый раз ПОСЛЕ выполнением какого-то теста"""
        print('tearDown')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def test_example1(self):
        print(self.current)
        print(self.current_cls)

    def test_example2(self):
        print(self.current)  # время должно ОТЛИЧАТЬСЯ, т.к. setUp вызывается при каждом новом вызове метода
        print(self.current_cls)  # время должно ОДИНКАОВЫМ, т.к. setUpClass вызывается единожды в рамках класса
