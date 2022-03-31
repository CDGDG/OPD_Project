from django.urls import path
from . import views

app_name = 'Project'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
]
