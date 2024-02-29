from django.urls import path
# from . import views
from .views import ListView,ListCreateView,ListUpdateView,ListDeleteView, LoginView, RegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('', ListView.as_view(), name='lists'),
    path('create_list/', ListCreateView.as_view(), name='create_list'),
    path('update-list/<str:pk>/', ListUpdateView.as_view(),name='update-list'),
    path('delete-list<str:pk>/', ListDeleteView.as_view(),name='delete-list'),
]
