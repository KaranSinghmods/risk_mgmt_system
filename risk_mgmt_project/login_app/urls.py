
# store urls for this application
# also need to add urls to project
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]