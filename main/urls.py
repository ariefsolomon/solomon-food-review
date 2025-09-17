from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('<uuid:pk>/', views.food_detail, name='food_detail'),
    path('add/', views.add_food, name='add_food'),
]