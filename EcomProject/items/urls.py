from django.urls import path 
from items import views
app_name = 'items'

urlpatterns=[
    path('<int:pk>/',views.details,name="details")
]