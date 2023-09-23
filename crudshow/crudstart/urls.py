from django.urls import path
from . import views

urlpatterns=[
  path('',views.addshow,name="addshow"),
 ]