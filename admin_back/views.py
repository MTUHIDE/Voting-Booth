from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages, auth
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from functools import wraps

import urllib
import json
import csv
import datetime
import requests
from django.urls import reverse

from .forms import QuestionForm, SurveyForm, UserCreationForm, CreateUserForm, EditProfileForm
from .models import Question, Survey

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

def registration(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('admin_back:home')

    context = {'form': form}
    return render(request, 'admin_back/user_registration.html', context)


def edit_user(request):
    form = EditProfileForm()

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin_back:dashboard')

    context = {'form': form}
    return render(request, 'admin_back/update_profile.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('admin_back:dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'admin_back/change_password.html', context)


'''
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = Newusers()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.emailId = form.cleaned_data['emailId']
            user.password = form.cleaned_data['password']
            user.save()']

    context = {}
    return render(request, 'admin_back/user_registration.html', context)

'''


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('redirect to a new page')


@login_required
def dashboard(request):
    context = {}
    return render(request, 'admin_back/dashboard.html', context)


def loginauth(request):
    context = {}
    return render(request, 'admin_back/loginauth.html', context)


'''
def forgotpass(request):
    context = {}
    return render(request, 'admin_back/password_reset.html', context)

def password_sent(request):
    context = {}
    return render(request, 'admin_back/password_reset_done', context)

def password_done(request):
    context = {}
    return render(request, 'admin_back/password_reset_confirm', context)
'''


@login_required
def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)

        if form.is_valid():
            survey = Survey()
            survey.title = form.cleaned_data['survey_name']
            for each in Survey.objects.all():
                each.state = 0
                each.save()
            survey.state = 1
            survey.save()

            return redirect('admin_back:create_question', survey_id=survey.id)

    context = {}
    return render(request, 'admin_back/create_survey.html', context)


@login_required
def manage_question(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    info = Question.objects.all()
    # print(survey_id)

    context = {'detail': info,
               'survey_id': survey_id,
               'survey_name': survey_name,
               # 'choices': choices
               }

    if request.method == 'POST':
        if 'add question' in request.POST:
            template = loader.get_template('admin_back/create_question.html')
            # return HttpResponse(template.render(context, request))
            return redirect('admin_back:create_question', survey_id=survey.id)
            # return redirect('admin_back:manage_question', survey_id=survey.id)
        elif 'edit' in request.POST:
            data = request.POST
            id = data.get("qid", "0")
            before = data.get("replace", "0")
            holder = Question.objects.get(id=id)
            holder.text = data.get("replace", "0")
            after = holder.text
            holder.save()
            # print(before)
            # print(after)
            # print(holder.id)

        elif 'delete' in request.POST:
            data = request.POST
            id = data.get("qid", "0")
            holder = Question.objects.get(id=id)
            holder.delete()
            # print(id)

            return render(request, 'admin_back/manageQuestions.html', context)

    return render(request, 'admin_back/manageQuestions.html', context)


@login_required
def manage_survey(request):
    info = Survey.objects.all()
    context = {"surveys": info}

    if request.method == "POST":

        answer = request.POST

        if "rfid-input" in answer:

            if len(request.POST.get('rfid-input')) == 13:
                messages.success(request, "Yes")
            else:
                messages.error(request, "No")
        else:
            id = request.POST.get("sid", "0")
            survey = Survey.objects.get(id=id)
            if "edit" in request.POST:
                request.method = None
                return redirect('admin_back:manage_question', survey_id=id)
            elif "active" in request.POST:
                for each in Survey.objects.all():
                    each.state = 0
                    each.save()
                survey.state = 1
                survey.save()
                return redirect('admin_back:manage_survey')
            elif "delete" in request.POST:
                survey.delete()
            elif "launch" in request.POST:
                request.method = None
                return redirect('admin_back:take_survey', survey_id=id)

    return render(request, 'admin_back/manage_survey.html', context)


@login_required
def create_question(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            # submit question data to database
            question = Question()
            question.survey = survey
            question.text = form.cleaned_data['questiontext']

            question.save()

            # redirect to manage questions page
            return redirect('admin_back:manage_question', survey_id=survey.id)

    context = {'survey_name': survey_name}
    template = loader.get_template('admin_back/create_question.html')
    return HttpResponse(template.render(context, request))


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_back:dashboard')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'admin_back/home.html')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return render(request, 'admin_back/home.html')
    context = {}
    return render(request, 'admin_back/home.html', context)


@login_required
def logout_User(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('admin_back:home')


@login_required
def form_test(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            # data is processed here
            return HttpResponseRedirect('/')

    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'admin_back/form_test.html', context)


def redirect_to_home(request):
    return HttpResponseRedirect('admin')


'''
def results(request):
   obj = Choice.objects.get(id=1)
   context = {
            'survey': obj.survey,
            'question': obj.question,
            'text': obj.text,
            'votes': obj.votes,
          }
   
   return render(request, 'admin_back/results.html', context)
'''


@login_required
def results(request):
    info = Question.objects.all()
    survey = Survey.objects.all()
    if request.method == 'POST':
        if not survey:
            display = ''
        else:
            data = request.POST
            if 'export' in data:
                display = data.get("surveys")
                current_datetime = datetime.datetime.now()
                response = HttpResponse(content_type='text/csv')
                response['Content-Desposition'] = 'attachment; filename = "results.csv"'

                writer = csv.writer(response)
                writer.writerow(['Date of results download: ' + current_datetime.strftime('%Y-%m-%d %H:%M')])
                writer.writerow(['Survey Title', 'Survey Question', 'Yes', 'No', 'Total'])
                for s in info:
                    if s.survey == display or s.survey.title == display:
                        writer.writerow([s.survey, s.text, s.yes, s.no, s.votes])

                return response
            else:
                display = data.get("surveys")
    elif request.method == 'GET':
        if not survey:
            display = ''
        else:
            for x in range(0, len(survey)):
                if survey[x].state == 1:
                    display = survey[x]
        # print(display)
    else:
        if not survey:
            display = ''

    resultdata = {'survey': survey,
                  'detail': info,
                  'display': display}
    # print(resultdata)
    # print(request)
    return render(request, 'admin_back/results.html', resultdata)


@login_required
def take_survey(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    info = Question.objects.all()
    # print(info)
    questionid_list = []
    for each in Question.objects.all():
        if each.survey_id == survey_id:
            questionid_list.append(each.id)
            # print(each.id)

    question_id = questionid_list[0]
    questionid_list.pop(0)

    # numofquestions = 0
    # for _ in info:
    #     numofquestions = numofquestions + 1

    context = {'detail': info,
               'survey_id': survey_id,
               'survey_name': survey_name,
               'question_id': question_id,
               'questionid_list': questionid_list
               }

    request.session['questionid_list'] = questionid_list
    return redirect('admin_back:display_question', survey_id, question_id)
    # return render(request, 'admin_back/display_question.html', context)


@login_required
def display_question(request, survey_id, question_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    info = Question.objects.all()

    context = {'detail': info,
               'survey_id': survey_id,
               'survey_name': survey_name,
               'question_id': question_id,
               'questionid_list': request.session['questionid_list']
               }

    if request.method == 'POST':

        answer = request.POST

        # Process RFID reader input
        if 'rfid-btn' in answer:
            if len(request.POST.get('rfid-input')) == 13:
                answer = 'yes'
            else:
                answer = 'no'
        if 'no' in answer:
            data = request.POST
            id = data.get("qid", "0")
            question = Question.objects.get(id=id)
            question.no += 1
            question.votes += 1
            # print("no")
        elif 'yes' in answer:
            data = request.POST
            id = data.get("qid", "0")
            question = Question.objects.get(id=id)
            question.yes += 1
            question.votes += 1
            # print("yes")

        question.save()
        questionid_list = request.session['questionid_list']
        if not questionid_list:
            return redirect('admin_back:end_survey', survey_id)
        else:
            question_id = questionid_list[0]
        questionid_list.pop(0)
        request.session['questionid_list'] = questionid_list
        return redirect('admin_back:display_question', survey_id, question_id)

    return render(request, 'admin_back/display_question.html', context)


@login_required
def end_survey(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    survey_name = survey.title
    info = Question.objects.all()

    context = {'detail': info,
               'survey_id': survey_id,
               'survey_name': survey_name,
               }

    if 'start' in request.POST:
        return redirect('admin_back:take_survey', survey_id=survey_id)

    return render(request, 'admin_back/end_survey.html', context)

