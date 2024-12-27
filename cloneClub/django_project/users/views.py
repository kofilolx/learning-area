from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()  # Save the new user to the database
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()  # Instantiate a new form for GET requests
    return render(request, 'users/register.html', {'form': form})

def login(request):

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get(username)
            form.save()
            messages.success(request, f'Login successful {username}')
            return reidercct('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/login.html', {'form':form})
