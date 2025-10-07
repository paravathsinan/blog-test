from django.shortcuts import render, redirect
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Registered Successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Registeration not  Successfully!')
    form = SignupForm()
    return render(request, 'user\signup.html', {'form':form})


def login_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        form = authenticate(request, email=email, password=password)
        if form:   
            login(request, form)
            messages.error(request, 'Login Successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Invaild E-Mail and Password')

    return render(request, 'user\login.html')


@login_required
def logout_views(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Failed Profile Update!')
            
    form = ProfileForm(instance=request.user)
    return render(request, 'user/profile.html', {'forms':form})
    