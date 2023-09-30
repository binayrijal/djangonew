from django.urls import path,include
from . import views


urlpatterns=[
  path('',views.addshow,name="addshow"),
  path('delete/<int:id>',views.delete_data,name="deletedata"),
  path('<int:id>/',views.update_data,name="updatedata"),
  
 ]