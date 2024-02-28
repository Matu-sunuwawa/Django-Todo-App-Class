from django.urls import path
# from . import views
from .views import ListView,ListCreateView,ListUpdateView,ListDeleteView

urlpatterns = [
    path('', ListView.as_view(), name='lists'),
    path('create_list/', ListCreateView.as_view(), name='create_list'),
    path('update-list/<str:pk>/', ListUpdateView.as_view(),name='update-list'),
    path('delete-list<str:pk>/', ListDeleteView.as_view(),name='delete-list'),
]
