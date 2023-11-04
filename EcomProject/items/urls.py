from django.urls import path 
from items import views
app_name = 'items'

urlpatterns=[
    path('new/',views.new,name="new"),
    path('<int:pk>/',views.details,name="details")
]
