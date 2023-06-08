from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    date_of_birth = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'date_of_birth', 'gender', 'phone_number', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.profile_picture = self.cleaned_data.get('profile_picture')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.gender = self.cleaned_data.get('gender')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.address = self.cleaned_data.get('address')

        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('username', 'email', 'password')


class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
