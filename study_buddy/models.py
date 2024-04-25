from django.db import models
# реализация найди пару
from django.contrib.auth.models import User

class FindPairTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PairElement(models.Model):
    task = models.ForeignKey(FindPairTask, related_name='pairs', on_delete=models.CASCADE)
    first_element = models.CharField(max_length=200)
    second_element = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_element} - {self.second_element}'
