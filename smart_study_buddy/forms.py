from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class RegistrationForm(UserCreationForm):
    group_choices = [(group.id, group.name) for group in Group.objects.all()]  

    group = forms.ChoiceField(choices=group_choices, label="Роль")  

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'group']  

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Подтвердите новый пароль", widget=forms.PasswordInput)

