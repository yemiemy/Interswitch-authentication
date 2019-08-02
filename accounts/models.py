import random
import hashlib
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
# Create your models here.
User = get_user_model()

class EmailConfirmed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    activation_key = models.CharField(max_length=200, null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.confirmed)

    def activate_user_email(self):
        #send email
        activation_url = '{}/{}'.format(settings.SITE_URL, reverse('activation_view', args=[self.activation_key]))
        context = {
            'activation_key': self.activation_key,
            'activation_url': activation_url,
            'user': self.user.username,
        }
        message= render_to_string('accounts/activation_message.txt', context)
        subject = 'Activation Message'
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email = None, *kwargs):
        send_mail(subject, message, from_email, [self.user.email], *kwargs)

def user_created(sender, instance, created, *args, **kwargs):
    user = instance
    #print(user.emailconfirmed.email_user())
    if created:
        email_confirmed, email_is_created = EmailConfirmed.objects.get_or_create(user=user)
        if email_is_created:
            #create has
            short_hash =hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            #username = user.username
            base, domain = str(user.email).split("@")
            activation_key = hashlib.sha1((short_hash+base).encode('utf-8')).hexdigest()
            email_confirmed.activation_key = activation_key
            email_confirmed.save()
            email_confirmed.activate_user_email()

post_save.connect(user_created, sender=User)




# Create your models here.


class Role(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
