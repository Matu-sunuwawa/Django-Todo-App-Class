from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import ToDoApp
from .forms import ListViewForm

# Create your views here.

# def home(request):
#     return HttpResponse("hello World")


class LoginView(LoginView):
    fields = '__all__'
    template_name = 'todoapp/loginview.html'
    # success_url = reverse_lazy('lists')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lists')

class RegistrationView(FormView):
    # fields = '__all__'
    form_class = UserCreationForm
    template_name = 'todoapp/registration.html'
    success_url = reverse_lazy('lists')

    def form_valid(self, form): # "form-valid" function is always "do" after submitting the form
        user = form.save()
        if user is not None:    # this mean "if the user successfully created..." or there is nothing left null required fields!!!
            login(self.request, user)   # this login function is for "authenticated" new user!!!
        return  super(RegistrationView, self).form_valid(form)
    
    def get(self, *args, **kwargs): # This takes responsibility to "redirect" to home if user is authenticated from registration page(do not see registration page)!!! for more remover this function and see changes!!!
        if self.request.user.is_authenticated:
            return redirect('lists')
        return super(RegistrationView, self).get(*args, **kwargs)

class ListView(LoginRequiredMixin, ListView):
    model = ToDoApp
    context_object_name  = 'lists'
    template_name = 'todoapp/lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user=self.request.user)
        return context

class ListCreateView(CreateView):
    model = ToDoApp
    # form_class = ListViewForm
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreateView, self).form_valid(form)

class ListUpdateView(UpdateView):
    model = ToDoApp
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('lists')

class ListDeleteView(DeleteView):
    model = ToDoApp
    context_object_name = 'lists'
    success_url = reverse_lazy('lists')