from rest_framework.serializers import ModelSerializer
from users.models import profiles
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model =User
        # fields = '__all__'
        exclude = ['is_superuser','password']

class profileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = profiles
        fields = '__all__'

