from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Note

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class NoteForm(ModelForm):
    class Meta:
        model=Note
        fields=['subject','content']