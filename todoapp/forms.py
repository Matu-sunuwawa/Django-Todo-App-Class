from django import forms
from .models import ToDoApp


class ListViewForm(forms.Form):
    lvf = forms.CharField()