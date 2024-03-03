from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_api_view.as_view()),
]