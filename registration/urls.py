from django.urls import path, include

from . import views

app_name = 'registration'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.register, name='register')]
    #path('registration/login/', views.my_view, name='my_view')]
