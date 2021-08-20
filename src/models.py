from django.db import models
from datetime import date


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)


class Reservation(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    client =  models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    data_init =  models.CharField(max_length=70, blank=False, default='')
    data_end =  models.CharField(max_length=70, blank=False, default='')
    published = models.BooleanField(default=False)


class Tennis_court(models.Model):
    client =  models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=70, blank=False, default='')
    umpire = models.BooleanField(default=False)
    teacher =  models.BooleanField(default=False)