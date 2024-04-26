from django.contrib import admin

from django.contrib import admin
from .models import Task, Pair

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    list_display = ('task', 'first_element_text', 'first_element_image', 'second_element_text', 'second_element_image')
