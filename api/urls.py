from django.urls import path
from .views import health, hello

urlpatterns = [
    path("health/", health),
    path("hello/", hello),
]
