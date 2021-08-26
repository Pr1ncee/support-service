from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """Сообщение, которое отправится в саппорт"""

    message = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
