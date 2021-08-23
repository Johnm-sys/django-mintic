from django.db import models
from datetime import date



class Tennis_court_1(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    client =  models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    date_init =  models.CharField(max_length=70, blank=False, default='')
    date_end =  models.CharField(max_length=70, blank=False, default='')
    referee = models.BooleanField(default=False)
    instructor = models.BooleanField(default=False)
    

class Tennis_court_2(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    client =  models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    date_init =  models.CharField(max_length=70, blank=False, default='')
    date_end =  models.CharField(max_length=70, blank=False, default='')
    referee = models.BooleanField(default=False)
    instructor = models.BooleanField(default=False)
    

class Tennis_court_3(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    client =  models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    date_init =  models.CharField(max_length=70, blank=False, default='')
    date_end =  models.CharField(max_length=70, blank=False, default='')
    referee = models.BooleanField(default=False)
    instructor = models.BooleanField(default=False)
    