from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='d_profile.png', null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
