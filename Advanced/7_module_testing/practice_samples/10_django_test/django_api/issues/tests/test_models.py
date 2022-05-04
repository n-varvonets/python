from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.test import TestCase, override_settings, tag
from django.utils import timezone

from issues.models import Issue


class IssueTestCase(TestCase):

    def setUp(self):
        self.issue = Issue.objects.create(
            name='test name',
            description='test desc',
            due_date=timezone.now().date() + timezone.timedelta(days=2),
        )

    # маркируем метод как `user`, что позволит потом запускать
    # только `user` тесты
    @tag('user')
    def test_str_method(self):
        self.assertEqual(str(self.issue), self.issue.name)

    @tag('user')  #  tag - это как маркировка... т.е. при запуске тестов терминале - можем указать какие тэги выполнять и будут выполненны только они
    def test_set_due_date(self):
        old_value = self.issue.due_date
        new_value = timezone.now().date()

        self.assertEqual(self.issue.due_date, old_value)

        self.issue.set_due_date(new_value)

        self.assertEqual(self.issue.due_date, new_value)
        self.issue.refresh_from_db()  # сбрасывает данные и подгружаем обратно с базы, что бы...
        self.assertEqual(self.issue.due_date, old_value)   # ...убедиться что не сохраняет в базу это значение

    @override_settings(DEBUG=True)  # жно в лайв режиме переопределить настройки
    def test_foo_prod_decorator(self):
        self.assertEqual(self.issue.foo(), self.issue.name)

    @override_settings(DEBUG=False)
    def test_foo_debug_decorator(self):
        self.assertEqual(self.issue.foo(), 'stub')

    def test_foo_prod_with(self):
        with self.settings(DEBUG=True): # синтаксический сахар, делает все  же самое что и сверху, но без декоратора
            self.assertEqual(self.issue.foo(), self.issue.name)

    def test_foo_debug_with(self):
        # переопределяем настройки проекта в рамках метода и тестируем метод
        with self.settings(DEBUG=False):
            self.assertEqual(self.issue.foo(), 'stub')

    def test_modify_settings(self):
        self.assertEqual(self.issue.bar(), self.issue.name)

        modify_rules = {'remove': settings.ADMINS_NAME}  #  или appendс ули хотим добавить настройку
        with self.modify_settings(CUSTOM_LIST=modify_rules):  # можем переопределить настройки и прокинуть в функцию
            self.assertEqual(self.issue.bar(), 'stub')

    def test_templates(self):
        with self.assertTemplateUsed('test_template.html'):
            render_to_string('test_template.html')  # можно так же проверить вызывался ли рендер шаблона при его вызове
        with self.assertTemplateNotUsed('test_template.html'):
            render_to_string('login.html')

    @tag('user')
    def test_queryset(self):
        """функция считает количество запросов"""
        User.objects.create(username='t')  # создаем пользователя
        total = User.objects.all().count()  # считаем первоначальное их общее кол-во

        def get_users_with_groups():
            """lfktt j,"""
            results = []
            total = User.objects.all().count()
            for user in User.objects.all():
                results.append({
                    'user': user,
                    'groups': list(user.groups.all())
                })  # + два запроса в БД
            return total, results

        # подсчитываем количество SQL запросов.
        self.assertNumQueries(2 + total, get_users_with_groups)  # сравниваем до(1  +2) и вызванную функцию(которая по идее делает 2 запроса)
