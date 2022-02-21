from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

"""
    Creating a question requires an existing survey, to add one to your database do the following:
    In your terminal run 'python manage.py shell'
    
    >>> from admin_back.models import Survey, Question, Choice
    >>> survey = Survey(title="testSurvey")
    >>> survey.save()
"""

"""
    IMPORTANT
    Variable names in forms must match the names given in the HTML code, i.e.
    questiontext is the same variable name as the <input> tag in the HTML code has in its name element
"""


class SurveyForm(forms.Form):
    survey_name = forms.CharField(label='Survey name', max_length=300)


class QuestionForm(forms.Form):
    questiontext = forms.CharField(label='Question text', max_length=200)

    choice1text = forms.CharField(label='Choice 1', max_length=100)
    choice2text = forms.CharField(label='Choice 2', max_length=100)

    # TYPE_CHOICES = [('radio', 'Radio'), ('checkbox', 'Checkbox')]
    # answertype = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)

    """

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    emailId = forms.CharField(label='Email ID', max_length=200)
    password = forms.CharField(label='Password', max_length=200)
    confirm_password = forms.CharField(label='confirm_password', max_length=200)
"""


class CreateUserForm(UserCreationForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@mtu.edu" not in data:  # any check you need
            raise forms.ValidationError("Must be a MTU email address")
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@mtu.edu" not in data and data != "":  # any check you need
            raise forms.ValidationError("Must be a MTU email address")
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    # UsernameField = forms.CharField(required=False)


class EditPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
