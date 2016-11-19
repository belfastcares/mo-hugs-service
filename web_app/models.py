from datetime import datetime, timedelta

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    name = models.CharField('name', max_length=30, unique=True)
    address = models.CharField('address', max_length=100)
    active = models.BooleanField('is_active', default=False)
    date_started = models.DateTimeField('date_started')
    completion_time = models.DateTimeField('completion_time')
    active_users = models.IntegerField('active_users')

    def __str__(self):
        return self.name

    def start_event(self):
        self.active = True
        self.date_started = datetime.now()
        self.completion_time = self.date_started + timedelta(minutes = 30)
        self.save()

    def is_active(self):
        return self.active

    def handle_timeout(self):
        if self.completion_time <= datetime.now():
            self.active = False
            self.active_users = 0
            self.save()

    def add_user(self):
        self.active_users += 1
        self.save()

    def remove_user(self):
        self.active_users -=1
        self.save()

@python_2_unicode_compatible
class Posts(models.Model):
    location = models.ForeignKey(Location)
    username = models.CharField('username', max_length=50)
    date_posted = models.DateTimeField(auto_now=True)
    message = models.TextField('message')

    def __str__(self):
        return str(self.id) + " " + self.username


