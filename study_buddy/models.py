from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Pair(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    first_element_text = models.CharField(max_length=100, blank=True, null=True)
    first_element_image = models.ImageField(upload_to='', blank=True, null=True)
    second_element_text = models.CharField(max_length=100, blank=True, null=True)
    second_element_image = models.ImageField(upload_to='', blank=True, null=True)