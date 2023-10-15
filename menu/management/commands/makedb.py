from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

from pytils.translit import slugify

from menu.models import Menu, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        call_command('makemigrations', verbosity=0, interactive=False)
        self.stdout.write(self.style.SUCCESS('SUCCESS makemigrations'))

        call_command('migrate', verbosity=0, interactive=False)
        self.stdout.write(self.style.SUCCESS('SUCCESS migrate'))

        call_command('collectstatic', verbosity=0, interactive=False)
        self.stdout.write(self.style.SUCCESS('SUCCESS collectstatic'))

        User.objects.create_superuser('admin', None, 'admin')
        self.stdout.write(self.style.SUCCESS('SUCCESS create_superuser [username=admin, password=admin]'))

        for i in range(1, 4):
            title = f'Меню{i}'
            menu = Menu.objects.create(title=title, slug=slugify(title))

            cats1 = []
            for j in range(1, 7):
                title = f'a-Категория{i}-{j}'
                cat = Category.objects.create(title=title, slug=slugify(title), menu=menu)
                cats1.append(cat)

            cats2 = []
            for k in range(1, 4):
                title = f'ab-Категория{i}-{k}'
                cat = Category.objects.create(title=title, slug=slugify(title), menu=menu, parent=cats1[i-1])
                cats2.append(cat)

            for g in range(1, 3):
                title = f'abc-Категория{i}-{g}'
                Category.objects.create(title=title, slug=slugify(title), menu=menu, parent=cats1[-i-1])

            for h in range(1, i+2):
                title = f'abcd-Категория{i}-{h}'
                Category.objects.create(title=title, slug=slugify(title), menu=menu, parent=cats2[i-2])

        self.stdout.write(self.style.SUCCESS('SUCCESS creation MOCK database'))
