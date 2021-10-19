from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Note(models.Model):

    class NoteStatus(models.TextChoices):
        published = 'published', _('Published')
        draft = 'draft', _('Draft')
        deleted = 'deleted', _('Deleted')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=NoteStatus.choices,
        default=NoteStatus.published,
        )
    is_public = models.BooleanField(default=False)
    created_date = models.DateTimeField( editable=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title