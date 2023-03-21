from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import *
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'home.html')


def register(request):
    form = RegisterUserForm
    message = ''
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Registration Successfully'
            form = RegisterUserForm
    return render(request, 'registration/register.html', {'form': form, 'msg': message})


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


@login_required
def category_questions(request, category_id):
    category = Category.objects.get(id=category_id)
    question = Question.objects.filter(**{'category__id': category_id}).order_by('id').first()
    return render(request, 'category_questions.html', {'question': question, 'category': category})


@login_required
def submit_answer(request, category_id, question_id):
    category = Category.objects.get(id=category_id)
    question = Question.objects.filter(**{'category__id': category_id, 'id__gt': question_id}).exclude(
        id=question_id).order_by('id').first()
    q = Question.objects.get(id=question_id)
    user = request.user
    if request.method == 'POST':
        if 'skip' in request.POST:
            answer = 'Not submitted'
            UserSubmittedAnswer.objects.create(user=user, question=q, submitted_answer=answer)
            if question:
                return render(request, 'category_questions.html', {'question': question, 'category': category})
            else:
                result = UserSubmittedAnswer.objects.filter(user=user)
                skipped = UserSubmittedAnswer.objects.filter(user=user, submitted_answer='Not submitted').count()
                attempted = UserSubmittedAnswer.objects.filter(user=user).exclude(
                    submitted_answer='Not submitted').count()
                right_ans_count = 0
                for r in result:
                    if r.question.answer == r.submitted_answer:
                        right_ans_count += 1
                return render(request, 'result.html',
                              {'results': result, 'skipped': skipped, 'attempted': attempted,
                               'right_ans': right_ans_count})

        else:
            answer = request.POST['answer']
            UserSubmittedAnswer.objects.create(user=user, question=q, submitted_answer=answer)
        if question:
            return render(request, 'category_questions.html', {'question': question, 'category': category})
        else:
            result = UserSubmittedAnswer.objects.filter(user=user)
            skipped = UserSubmittedAnswer.objects.filter(user=user, submitted_answer='Not submitted').count()
            attempted = UserSubmittedAnswer.objects.filter(user=user).exclude(submitted_answer='Not submitted').count()
            right_ans_count = 0
            for r in result:
                if r.question.answer == r.submitted_answer:
                    right_ans_count += 1
            return render(request, 'result.html',
                          {'results': result, 'skipped': skipped, 'attempted': attempted, 'right_ans': right_ans_count})
    else:
        return HttpResponse('Method not allowed')


@login_required
def add_category(request):
    form = AddCategoryForm
    message = ''
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Category add Successfully'
            form = AddCategoryForm
    return render(request, 'add-category.html', {'form': form, 'msg': message})


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'shop/password_success.html')
