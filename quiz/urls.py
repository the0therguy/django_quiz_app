from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register', register, name='register'),
    path('all-categories', all_categories, name='all_categories'),
    path('questions/<int:category_id>', category_questions, name='category_question'),
    path('submit-answer/<int:category_id>/<int:question_id>', submit_answer, name='submit-answer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
