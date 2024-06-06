from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Pair(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    first_element_text = models.CharField(max_length=100, blank=True, null=True)
    first_element_image = models.ImageField(upload_to='', blank=True, null=True)
    second_element_text = models.CharField(max_length=100, blank=True, null=True)
    second_element_image = models.ImageField(upload_to='', blank=True, null=True)

class CompletedTask(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed_date = models.DateField(auto_now_add=True)
    grade = models.IntegerField(null=True, blank=True)