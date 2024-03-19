from django.urls import path
from Puer_app import views
from django.urls import path
from .views import home


urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form')


]








