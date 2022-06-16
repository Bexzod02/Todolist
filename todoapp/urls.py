from django.urls import path
from .views import index,  single, search, delete, create

urlpatterns = [
    path('', index, name='index'),
    path('edit/<int:pk>/', single, name='single'),
    path('search/', search, name='search'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create/', create, name='create'),
]
