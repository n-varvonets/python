import datetime
import unittest
import unittest.mock


def sum_two_values(a, b):
    return a + b


def power(x, n):
    return x ** n


def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if x == 0:
        raise ValueError('`x` should not be equeal 0')
    return y / x


class User:
    def test_method(self):
        raise NotImplementedError


class UserTestCase(unittest.TestCase):

    @unittest.mock.patch('5_mock.sum_two_values')  # unittest передаст path к функции '5_mock.sum_two_values' которую хотим пропатчить
    def test_sum_two_values_uncalled(self, mocked_sum):
        """проверяем что бы наша функция не звывалась"""
        # функция нами не вызывалась, а значит called будет False
        self.assertFalse(mocked_sum.called)  # проверяет вызывалась ли наша функция и если нет, то assertFalse будет true и тест пройдет

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_sum_two_values_called(self, mocked_sum):
        sum_two_values(10, 20)  # что бы проверить вызывалась ли функция, то нужно вызывать настоящию фунцию sum_two_values, а не пропатченную mocked_sum
        # функция нами вызывалась, а значит called будет True
        # но тело функции не выполнялось, так как мы сделали `mock.patch`.
        self.assertTrue(mocked_sum.called)

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_sum_two_values_called_with(self, mocked_sum):
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)  # вызывалась ли она вообще? ДОПУСТИМ В ТЕСТАХ НЕ НУЖНО ОТПРАЛЯТЬ СМС НА ПОЧТУ, А НУЖНО ПРОВРЕТЬИ ЛИШЬ ФАКТ
        self.assertEqual(mocked_sum.call_count, 1)  # тело функции выполнялось один раз(выше строка), проверим это
        mocked_sum.assert_called_with(10, 20)  # проверим с какими аргументами вызывалась функция

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_reset_mock(self, mocked_sum):
        sum_two_values(10, 20)
        sum_two_values(10, 20)
        self.assertTrue(mocked_sum.called)
        self.assertEqual(mocked_sum.call_count, 2)
        # проверим вызывалась ли функция используя другой способ
        mocked_sum.assert_called()
        mocked_sum.assert_called_with(10, 20)

        # сбросим счетчик вызовов, после чего функция будет обнулена и
        # все предыдущие вызовы как бы забыты
        mocked_sum.reset_mock()

        self.assertEqual(mocked_sum.call_count, 0)
        self.assertFalse(mocked_sum.called)
        mocked_sum.assert_not_called()

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_mock_call(self, mocked_sum):
        sum_two_values(10, 40)
        sum_two_values(20, 50)
        sum_two_values(30, 60)
        # был ли хотя бы один вызов функции с такими аргументами
        mocked_sum.assert_any_call(10, 40)

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_mock_call_with(self, mocked_sum):
        sum_two_values(10, 40)
        mocked_sum.assert_called_with(10, 40)

        sum_two_values(20, 50)
        mocked_sum.assert_called_with(20, 50)

        sum_two_values(30, 60)
        mocked_sum.assert_any_call(30, 60)

    # подменим возвращаемое значение на число 20.
    @unittest.mock.patch('5_mock.sum_two_values', return_value=20)
    def test_mock_return_value_in_dec(self, mocked_sum):
        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)  # т.е. вызов функции sum_two_values всегда возращало 20ть, что бы мы ему не передали
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)  # здесь в этом можно убедиться, потому что вернет true
        self.assertEqual(result3, 20)

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_mock_return_value_in_body(self, mocked_sum):
        # подменим возвращаемое значение на число 20 используя еще один способ
        mocked_sum.return_value = 20

        result1 = sum_two_values(10, 40)
        result2 = sum_two_values(110, 140)
        result3 = sum_two_values(1110, 1140)
        self.assertEqual(result1, 20)
        self.assertEqual(result2, 20)
        self.assertEqual(result3, 20)

    @unittest.mock.patch('5_mock.sum_two_values')
    def test_mock_side_effect(self, mocked_sum):
        """переопределим тело функции своим собственным функционалом"""
        result = 0  # всегда будет результат выполнения нашей функции 0, но без return_value, а...

        def res_func(x, y):
            """т.е. можем менять здесь функцию, примая те же значения что и обычная, а потом проверять резлуьтат"""
            return result

        # по вызову нашей функции мы хотим выполнить сторонний код,
        # который опишем в тесте. Как правило это называется side effect
        mocked_sum.side_effect = res_func

        self.assertEqual(sum_two_values(110, 140), result)  # при вызове sum_two_values будет вызываться наша res_func
        self.assertEqual(sum_two_values(10, 0), result)
        self.assertEqual(sum_two_values(300, 400), result)

        # мы также можем присвоить экземпляр исключение, чтобы оно было
        # выбрашено в момент вызова
        raise_text = 'Test exception'
        mocked_sum.side_effect = ValueError(raise_text)
        with self.assertRaises(ValueError):  # будет тру, потому что мы переопределили результат вызова функции строчкой выше
            sum_two_values(10, 30)

        # более того, список исключений для последовательного вызова
        mocked_sum.side_effect = ValueError, RuntimeError, ZeroDivisionError

        with self.assertRaises(ValueError):  # последовательно первый вызов ошибки
            sum_two_values(10, 30)
        with self.assertRaises(RuntimeError):
            sum_two_values(10, 30)
        with self.assertRaises(ZeroDivisionError):
            sum_two_values(10, 30)

        # если мы хотим добавить side effect вместе с возвращаемым значением,
        # которое также хотим задать, используем `return mock.DEFAULT`
        def res_func2(x, y):
            print('Hey')
            return unittest.mock.DEFAULT  # default позво ляет использовать return_value но использовать side_effect, т.е. исползовать def res_func2()

        mocked_sum.return_value = 300
        mocked_sum.side_effect = res_func2
        self.assertEqual(sum_two_values(1, 2), 300)  # вызвана res_func2 и распечатет 'Hey' и дефолтно даст ответ return_value, т.е. DEFAULT

    def test_mock_return_value_in_body_with(self):
        # использование патчинга в связке с оператором with

        with unittest.mock.patch('5_mock.sum_two_values') as mocked_sum:
            """то же самое что и в прошлом примере, только у нас внутри метода это патчиться,
             а в предедущих у нас патчилось до вызова метода"""
            mocked_sum.return_value = 20
            result1 = sum_two_values(10, 40)
            result2 = sum_two_values(110, 140)
            result3 = sum_two_values(1110, 1140)
            self.assertEqual(result1, 20)
            self.assertEqual(result2, 20)
            self.assertEqual(result3, 20)

    def test_mock_builtin(self):
        """случай, когда нам нужно пропатчить builtin модули"""
        with unittest.mock.patch('datetime.datetime') as mocked_datetime:
            actual_date = datetime.datetime(2019, 1, 1, 23, 8, 6)

            mocked_datetime.now.return_value = actual_date  # патчим метод now и теперь она будет возвращать наш actual_date
            result1 = datetime.datetime.now()
            self.assertEqual(result1, actual_date)

    # мы можем патчить даже методы у классов, используя `mock.patch..object`
    @unittest.mock.patch.object(User, 'test_method')
    def test_user(self, mock_method):
        mock_method.return_value = 10
        user = User()
        # вызываем метод и проверяем наш mock
        user.test_method()
        self.assertTrue(mock_method.called)
        mock_method.assert_called_once()
