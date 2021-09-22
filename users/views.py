from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

from .forms import TicketForm, AnswerForm
from .models import Ticket, Answer

#TODO Сделать правильную авторизацию персонала.


def index(request):
    """
    Временное решение авторизации персонала - проверка по id
    """
    if request.user.id == 1:
        return render(request, 'users/staff_page.html')

    return render(request, 'users/index.html')


def log_out(request):
    logout(request)
    return render(request, 'users/index.html')


def new_ticket(request):
    """
    Если метод GET, просто рендерит страницу с формой.
    Если метод POST, проверяет валидность данных, сохраняет их и перенаправляет пользователя.
    """
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


def messages(request, message_id=0):
    """
    Выводит список тикетов, отправленных пользователем.
    """
    message = Ticket.objects.filter(user_data=request.user.id).order_by('-added_date')

    context = {'messages': message}
    return render(request, 'users/messages.html', context)


def record_delete(request, message_id):
    """
    Удаляет тикет по решению пользователя.
    """
    try:
        record = Ticket.objects.get(id=message_id)
        record.delete()
    except ObjectDoesNotExist:
        pass

    return redirect('messages.html')


def answer(request):
    """
    Загружает ответы и тикеты, на которые ответил саппорт.
    """
    answer_instance = Answer.objects
    answers = []

    for ans in answer_instance.order_by('-date_added'):
        if ans.question.user_data == request.user:
            answers.append(ans)

    context = {'answers': answers}
    return render(request, 'users/answers.html', context)


def questions(request, ticket_id=0):
    """
    Если метод POST, меняет статус тикета (решенный, нерешенный, замороженный).
    Выводит тикеты пользователей.
    """
    if request.method == 'POST':
        try:
            choice = request.POST['choice']

            ticket = Ticket.objects.get(id=ticket_id)
            ticket.status = choice
            ticket.save()
        except MultiValueDictKeyError:
            pass

    tickets = Ticket.objects.order_by('-added_date')

    context = {'tickets': tickets}
    return render(request, 'users/questions.html', context)


def feedback(request, ticket_id):
    """
    Если метод GET, рендерит страницу с формой, иначе проверяет валидность данных и записывает в БД.
    """
    tickets = Ticket.objects
    answers = Answer.objects

    ticket = tickets.get(id=ticket_id)
    user_name = ticket.user_data

    prev_ans = []  # Список с ответами, если саппорт ранее обрабатывал тикет.

    if request.method != 'POST':
        form = AnswerForm()

    else:
        form = AnswerForm(data=request.POST)

        if form.is_valid():
            answer_ = form.save(commit=False)
            answer_.question = ticket  # Привязывает ответ к соответствующему тикету.
            answer_.save()
            return redirect('questions.html')

    for reply in answers.order_by('-date_added'):
        if reply.question.id == ticket_id:
            prev_ans.append(reply)

    context = {'form': form,
               'ticket': ticket,
               'user_name': user_name,
               'prev_ans': prev_ans}
    return render(request, 'users/reply.html', context)
