from django.contrib import admin
from .models import User,Teacher

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','email','password','checkbox']
