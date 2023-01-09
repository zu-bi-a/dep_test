from dataclasses import field
from rest_framework import serializers
from .models import UserModell
from .models import Word



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModell
        fields = '__all__'
    
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(UserSerializer, self).__init__(*args, **kwargs)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModell
        fields = ('userId', 'username', 'firstName', 'lastName','password', 'phone', 'email', 'userImg', 'desc', 'rating')

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

        
    # For Partial Updating
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(WordSerializer, self).__init__(*args, **kwargs)

    