from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import Users
from django import forms


class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Input password'}))

    class Meta:
        model = Users
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegistration(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input last name'}))
    username = forms.EmailInput(attrs={'placeholder': 'Input email'})

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfile(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name', 'status')

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'