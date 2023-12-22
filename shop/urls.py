from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import CategoryApiView

router = routers.DefaultRouter()
router.register(r'api/cat', CategoryApiView)
urlpatterns = [
    path('', include(router.urls))

]
