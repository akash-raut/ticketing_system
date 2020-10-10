from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    ''' Register user '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account created and you can login now!')
            return redirect('login')
    form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})


@login_required()
def dashboard(request):
    return render(request, 'Users/dashboard.html')

