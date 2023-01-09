from operator import mod
from statistics import mode
from django.db import models
import uuid
# Create your models here.

# ========USER MODEL=========
class UserModell(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    password = models.CharField(max_length=250)   #while taking it as an input in forms we will use PasswordInput on form
    phone = models.BigIntegerField(blank=False, null=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    userImg = models.ImageField(upload_to='accounts/images', null=True, blank=True)
    desc = models.TextField(null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Word(models.Model):
    word_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wordUser = models.ForeignKey('UserModell', related_name='speaker', on_delete=models.CASCADE, null=True)
    word = models.TextField()
    spokenAudio = models.FileField(upload_to='API/views/documents', blank=True)
    spokenPhonetics = models.TextField(blank=True)
    correctPhonetics = models.TextField(blank=True)
    score = models.FloatField(default=0.0)


    def __str__(self):
        return str(self.word)