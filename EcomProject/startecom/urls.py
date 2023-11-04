from django.urls import path
from startecom import views

app_name='startecom'


urlpatterns=[
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
]