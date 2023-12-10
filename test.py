from django.apps import apps
from django.core.management import execute_from_command_line

# Загружаем Django
execute_from_command_line(["manage.py", "shell"])

# Получаем все модели из всех приложений
all_models = apps.get_models()

# Выводим имена моделей в консоль
for model in all_models:
    print(model.__name__)