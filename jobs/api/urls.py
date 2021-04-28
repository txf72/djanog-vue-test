from django.urls import path
from jobs.api import views

urlpatterns = [
    path("jobs/", views.ListView.as_view(), name="list"),


]