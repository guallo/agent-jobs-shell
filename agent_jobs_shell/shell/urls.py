from django.urls import path

from . import views

urlpatterns = [
    path('list-jobs/', views.list_jobs, name='list_jobs'),
]
