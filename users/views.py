from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

from .forms import TicketForm, AnswerForm
from .models import Ticket, Answer


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


def messages(request):  # message_id=0
    message = Ticket.objects.filter(user_data=request.user.id).order_by('-added_date')

    context = {'messages': message}
    return render(request, 'users/messages.html', context)


def record_delete(request, message_id):
    try:
        record = Ticket.objects.get(id=message_id)
        record.delete()
    except ObjectDoesNotExist:
        pass

    return redirect('messages.html')


def answer(request):
    answer_instance = Answer.objects
    answers = []

    for ans in answer_instance.order_by('-date_added'):
        if ans.question.user_data == request.user:
            answers.append(ans)

    context = {'answers': answers}
    return render(request, 'users/answers.html', context)


def questions(request, ticket_id=0):
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
    instance = Ticket.objects
    ticket = instance.get(id=ticket_id)
    user_name = ticket.user_data
    answers = Answer.objects
    prev_ans = []

    if request.method != 'POST':
        form = AnswerForm()

    else:
        form = AnswerForm(data=request.POST)

        if form.is_valid():
            answer_ = form.save(commit=False)
            answer_.question = ticket
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
