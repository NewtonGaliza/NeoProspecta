from django.db import models
from django.urls import reverse
import uuid

class Entry(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for Entry model')
    access_id = models.CharField(max_length=20, unique=True, help_text='unique access_id')
    kingdom = models.ForeignKey('Kingdom', on_delete=models.SET_NULL, null=True, help_text='can store a Null value, and if the recorded is deleted the Null value is stored')
    specie = models.ForeignKey('Specie', on_delete=models.SET_NULL, null=True, help_text='can store a Null value, and if the recorded is deleted the Null is stored')
    sequence = models.CharField(max_length=258)

    def __str__(self): #string for representing the Entry object
        return self.access_id

class Kingdom(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for Kingdom model')
    label = models.CharField(max_length=258, help_text='Kingdom label')

    def __str__(self):
        return self.label

    def get_basolute_url(self): #returns the url to access a detail record
        return reverse('kingdom-detail', args=[str(self.label)])

class Specie(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id for Specie model')
    label = models.CharField(max_length=258, help_text='Specie label')

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('specie-detail', args=[str(self.label)])
