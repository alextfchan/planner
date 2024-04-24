from django.shortcuts import render, redirect
from django.db import models

class Timer(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=25)
    seconds = models.IntegerField(default=0)

    def __str__(self):
        return self.name