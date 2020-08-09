from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *

class TicketForm(forms.Form):
    GENDER_CHOICES = (
        ('MALE','Male'),
        ('FEMALE','Female'),
    )
    BERTH_CHOICES = (
        ('UPPER','Upper'),
        ('LOWER','Lower'),
        ('FEMALE','Middle '),
        ('SIDE','Side portion'),
    )

    #GENDER_CHOICES

    name = forms.CharField(max_length=60)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    berth_preference = forms.ChoiceField(choices=BERTH_CHOICES)

# class  DemoForm(forms.Form):
#     COLOR = (
#         ('R', _('RED')),
#         ('O', _('ORANGE')),
#         ('W', _('WHITE')),
#     )
#     MALE = 'M'
#     FEMALE = 'F'

#     GENDER = (
#         (MALE,'Male'),
#         (FEMALE,'Female'),
#     )
#     name = forms.CharField()
#     title = forms.CharField()
#     created_on = forms.DateField(widget= forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),))   
#     color = forms.ChoiceField(choices=COLOR, widget= forms.Select)
#     gender = forms.ChoiceField(choices=GENDER, widget= forms.Select, initial= 'F') # Or iInitial= FEMALE

