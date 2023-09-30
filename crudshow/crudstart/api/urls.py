from django.urls import path,include
from rest_framework.routers import DefaultRouter
from crudstart.api.views import Userviewset

router=DefaultRouter()
router.register('crud',Userviewset,basename='userviewset')


urlpatterns=[
    path('',include(router.urls))
]