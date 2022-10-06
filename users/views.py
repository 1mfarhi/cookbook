from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from recipes import models
from .import forms

# from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created, please login')
            return redirect('user-login')
        else:
            form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
        


@login_required()
class ProfileModel():
    def profile(request):
        return render(request, 'users/profile.html')