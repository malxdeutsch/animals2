from django.db import models
from django.forms import ModelForm

# Create your models here.

class Animal (models.Model):
    legs = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    height = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)
    family = models.ForeignKey('Family', on_delete=models.CASCADE)

class Family(models.Model):
    name = models.CharField(max_length=200)

class ArticleForm(ModelForm):
    class Meta:
        model = Animal
        fields ='__all__'


