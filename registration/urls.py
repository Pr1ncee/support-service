from django.urls import path, include

from . import views

app_name = 'registration'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('registration/', views.register, name='register')]
