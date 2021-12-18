from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from estateapp.forms import RegistrationForm
#from accounts.models import User


def admin(request):
    return render(request, "estateapp/admin.html")

#register new user
def register(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        #is_admin = form.cleaned_data.get('is_admin')
        #is_agent = form.cleaned_data.get('is_agent')
        #is_customer = form.cleaned_data.get('is_customer')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('accounts:register')
                #print('Username taken')
            elif User.objects.filter(email=email).exists():
                #print('Email taken')
                messages.info(request, 'Email Taken')
                return redirect('accounts:register')
            else:
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,password=password1)
                user.save();
                messages.info(request, 'New User Created')
                #print('User created')
                return redirect('accounts.login')
        else:
            messages.info(request, 'Password not matching ...')
            return redirect('accounts:register')
        return redirect('/')

    else:
        return render(request, 'estateapp/register.html', {"form": form})


    return render(request, "estateapp/register.html", {"form": form})

# Login User.
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login Failed'

    return render(request, 'estateapp/login.html', context = {'form':form, 'message':message})

# Log out User
@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    messages.info(request, "You have logged out")
    return redirect('/')
