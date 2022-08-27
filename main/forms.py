from django import forms
from django.forms import (fields, widgets, Textarea, NumberInput, Select, DateField)
from .models import Poll


class pollForm(forms.Form):
    question = forms.CharField(label="Question", max_length=200, required=True)
    opt1 = forms.CharField(label="Answer 1", max_length=200, required=True)
    opt2 = forms.CharField(label="Answer 2", max_length=200, required=True)
    opt3 = forms.CharField(label="Answer 3", max_length=200, required=True)
    opt4 = forms.CharField(label="Answer 4", max_length=200, required=True)
    
        
