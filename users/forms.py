# from profile import Profile
# import users.models
# from django.forms import ModelForm
# from django.core.validators import validate_email
# from .models import *

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         # fields = ['username', 'email', 'password1', 'password2']   
#         exclude = ['user']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ["username", "email"]

# class ProfileUpdateForm(forms.ModelForm):
#     Profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE, verbose_name="Report Author")
#     model = Profile
#     fields = ["image"]