from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id",'username','first_name','last_name','email','password']