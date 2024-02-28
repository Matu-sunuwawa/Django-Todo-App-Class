from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ToDoApp
from .forms import ListViewForm

# Create your views here.

# def home(request):
#     return HttpResponse("hello World")

class ListView(ListView):
    model = ToDoApp
    context_object_name  = 'lists'
    template_name = 'todoapp/lists.html'

class ListCreateView(CreateView):
    model = ToDoApp
    # form_class = ListViewForm
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('lists')

class ListUpdateView(UpdateView):
    model = ToDoApp
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('lists')

class ListDeleteView(DeleteView):
    model = ToDoApp
    context_object_name = 'lists'
    success_url = reverse_lazy('lists')