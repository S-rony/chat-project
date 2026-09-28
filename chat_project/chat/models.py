from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.Charfiels(max_length = 100, unique = True)
    description = models.Textfield(blanck = True, null = True)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)