from django.urls import path
from . import views

urlpatterns=[
  path('',views.addshow,name="addshow"),
  path('delete/<int:id>',views.delete_data,name="deletedata")
 ]