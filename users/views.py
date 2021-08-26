from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import TicketForm
from .models import Ticket


def index(request):
    if request.user.id == 1:
        return render(request, 'users/staff_page.html')

    return render(request, 'users/index.html')


def log_out(request):
    logout(request)
    return render(request, 'users/index.html')


def new_ticket(request):
    if request.method != 'POST':
        form = TicketForm()

    else:
        form = TicketForm(data=request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user_data = request.user
            ticket.save()
            return redirect('gratitude_words.html')

    context = {'form': form}
    return render(request, 'users/ticket.html', context)


def gratitude_words(request):
    return render(request, 'users/gratitude_words.html')


def messages(request):
    message = Ticket.objects.filter(user_data=request.user.id).order_by('-added_date')

    context = {'messages': message}
    return render(request, 'users/messages.html', context)


def record_delete(request, message_id):
    try:
        record = Ticket.objects.get(id=message_id)
        record.delete()
    except ObjectDoesNotExist:
        pass

    message = Ticket.objects.filter(user_data=request.user.id).order_by('-added_date')

    context = {"messages": message}
    return render(request, 'users/messages.html', context)


def answer(request, message_id=None, user_id=None):
    if request.method != 'POST':
        answer_ = []  # Рендерим страницу, если первое обращение
    else:
        answer_ = []  # Загружаем ответ пользователю в ДБ

    context = {'answers': answer_}
    return render(request, 'users/answers.html', context)


def staff_page(request):
    return render(request, 'users/staff_page.html')


def questions(request):
    tickets = Ticket.objects.order_by('-added_date')

    context = {'tickets': tickets}
    return render(request, 'users/questions.html', context)


def feedback(request, ticket_id):
    return redirect('users:index')
