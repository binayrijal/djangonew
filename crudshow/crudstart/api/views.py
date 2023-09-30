from crudstart.models import User
from rest_framework import viewsets
from crudstart.api.serializers import UserSerializer


class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer