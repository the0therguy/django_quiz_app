from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register', register, name='register'),
    path('all-categories', all_categories, name='all_categories'),
    path('questions/<int:category_id>', category_questions, name='category_question'),
    path('submit-answer/<int:category_id>/<int:question_id>', submit_answer, name='submit-answer'),
    path('add-category', add_category, name='add-category'),
    path('change_password/', PasswordsChangeView.as_view(template_name='change_password.html'),
         name='change_password'),
    path('password_success/', password_success, name='password_success'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('add-question', add_question, name='add-question'),
    path('delete-category/<int:category_id>', delete_category, name='delete-category'),
    path('question-categorywise/<int:category_id>', question_categorywise, name='question-categorywise'),
    path('delete-question/<int:category_id>/<int:question_id>', delete_question, name='delete-question'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
