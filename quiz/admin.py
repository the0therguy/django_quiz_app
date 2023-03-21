from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'difficulty']


admin.site.register(Question, QuestionAdmin)


class UserSubmitAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user', 'submitted_answer']


admin.site.register(UserSubmittedAnswer, UserSubmitAnswerAdmin)


class UserCategoryAttemptAdmin(admin.ModelAdmin):
    list_display = ['category', 'user', 'attempt_time']


admin.site.register(UserCategoryAttempt, UserCategoryAttemptAdmin)
