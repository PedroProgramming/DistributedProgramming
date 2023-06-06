from django.urls import path
from . import views


urlpatterns = [
    path('incricao/', views.incricao, name="incricao"),
    path('test/', views.test, name="test"),
]
