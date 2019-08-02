from django.db import models
from accounts.models import Role
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    total_points = models.IntegerField(default=0, null=True, blank=False)
    pending_points = models.IntegerField(default=0, null=True, blank=False)
    members = models.ManyToManyField(User, verbose_name='members')
    program_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams', null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', null=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, null=True)
    is_line_manager = models.BooleanField(default=False,null=False)
    is_program_manager = models.BooleanField(default=False,null=False)

    def __str__(self):
        return self.user.username