from django.contrib import admin
from django.apps import apps
from .models import *
from django.contrib import admin
from django.apps import apps

# Получите все модели из текущего приложения
app_models = apps.get_app_config('shop').get_models()

# Зарегистрируйте все модели в административной панели
for model in app_models:
    admin.site.register(model)