
from django.contrib import admin
from django.urls import path,include
from crudstart import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('crudstart.urls'),name="viewshow")
]
