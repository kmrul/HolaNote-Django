from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .note_enums import NoteStatusChoice

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=255,
        choices = NoteStatusChoice.choices(),
        )
    is_public = models.BooleanField(default=False)
    created_date = models.DateTimeField( editable=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title