from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hood.models import Business, Neighborhood, Post, Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Type a valid email address!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('name', 'location', 'description', 'photo', 'health_phone', 'police_phone')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business 
        exclude = ('user', 'neighborhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighorhood')