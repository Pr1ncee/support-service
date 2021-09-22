from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Вход в систему
    path('accounts/profile/', views.index, name='loggedin'),
    # Выход из системы
    path('registration/log_out', views.log_out, name='log_out'),
    # Страница добавления тикета
    path('new_ticket/', views.new_ticket, name='new_ticket'),
    # Страница успешной отправки тикета
    path('new_ticket/gratitude_words.html', views.gratitude_words, name='gratitude_words'),
    # Просмотр отправленных вопросов
    path('messages/', views.messages, name='messages'),
    path('messages/<int:message_id>/', views.messages, name='message_delete'),
    # Удаление отправленного тикета
    path('record_delete/<int:message_id>/', views.record_delete, name='record_delete'),
    # Переадресация
    path('record_delete/<int:message_id>/messages.html', views.messages),
    # Просмотр ответов саппорта
    path('accounts/profile/users/staff_page.html', views.answer, name='answers'),
    # Просмотр отправленных тикетов (на стороне саппорта)
    path('users/questions.html/', views.questions, name='questions'),
    # Изменение статуса тикета (на стороне саппорта)
    path('users/questions.html/<int:ticket_id>', views.questions, name='questions_status'),
    # Страница для отправки ответа (на стороне саппорта)
    path('feedback/questions.html', views.questions),
    # Переадресация, если ответ успешно отправлен (на стороне саппорта)
    path('feedback/<int:ticket_id>', views.feedback, name='feedback')]
