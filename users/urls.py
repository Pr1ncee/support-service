from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    path('messages/', views.messages, name='messages'),
    path('record_delete/<int:message_id>/messages.html', views.messages),
    path('accounts/profile/users/staff_page.html', views.answer, name='answers'),
    path('users/questions.html/', views.questions, name='questions'),
    path('record_delete/<int:message_id>/', views.record_delete, name='record_delete'),
    path('new_ticket/gratitude_words.html', views.gratitude_words, name='gratitude_words'),
    path('accounts/profile/', views.index, name='loggedin'),
    path('registration/log_out', views.log_out, name='log_out'),
    path('feedback/<int:ticket_id>', views.feedback, name='feedback'),
    path('feedback/questions.html', views.questions),
    path('users/questions.html/<int:ticket_id>', views.questions, name='questions_1')]
