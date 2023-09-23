from django.urls import path
from . import views

urlpatterns=[
  path('',views.add_show,name='add_show'),
  path('new/',views.addshow,name="addshow"),
 ]