from django.urls import path
from .views import (
    welcome,
    translator,
    translated,
)

urlpatterns = [
    path("", welcome, name="homepage"),
    path("v1/translator/", translator, name="translator_page"),
    path("v1/translator/result", translated, name="translated"),
]
