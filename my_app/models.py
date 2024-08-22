from django.db import models as m
from rest_framework.generics import ListAPIView


# Create your models here.



class Note(m.Model):
    title = m.CharField('Title', max_length=50)
    description = m.CharField('Description', max_length=50)
    created_at = m.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return self.title



