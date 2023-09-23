
from django.contrib import admin
from django.urls import path
from crudstart import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name="viewshow")
]
