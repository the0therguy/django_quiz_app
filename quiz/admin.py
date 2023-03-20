from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'difficulty']


admin.site.register(Question, QuestionAdmin)
