from django.urls import path
from .views import form_show,delete_data,addshow,update_data


urlpatterns=[
  path('view/',addshow,name="addshow"),
  path('delete/<int:id>',delete_data,name="deletedata"),
  path('<int:id>/',update_data,name="updatedata"),
  path('',form_show,name="viewshow")
 
 ]