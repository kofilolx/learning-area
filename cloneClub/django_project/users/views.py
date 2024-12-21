from django.shortcuts import render
from django.contrib.auth.forms import UserCreaationForm

def register(request):
    form = UserCreaationForm()
    return render(request, 'users/register.html', {'form': form})
