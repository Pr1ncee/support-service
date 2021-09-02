from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    """Сообщение, которое отправится в саппорт"""

    message = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, default='unsolved')

    def __str__(self):
        return self.message


class Answer(models.Model):
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
