from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patricia/', views.patricia, name='patricia'),
    path('mechaila/', views.mechaila, name='mechaila'),
]
