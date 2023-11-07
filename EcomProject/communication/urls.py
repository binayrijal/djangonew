from django.urls import path
from communication.views import new_communication

app_name='communication'

urlpatterns=[
    path('new/<int:item_pk>/',new_communication,name="newcommunication")
]