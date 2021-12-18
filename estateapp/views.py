from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Agent
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
import json

#Import pagination
from django.core.paginator import Paginator

#filters
from .filters import PropertyFilter

# Create your views here.
#create json view
def json(request):
    data = list(Property.objects.values())
    return JsonResponse(data, safe=False)

# index view here
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    prop_list = Property.objects.all().order_by("-id")
    agt_list = Agent.objects.all().order_by("name")
    context = {

        'prop_list': prop_list,
        'agt_list': agt_list

}
    return render(request, "estateapp/index.html", context )

# about page view here
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def about(request):
    return render(request, "estateapp/about.html")

# property grid, list all the properties ordered by id
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def property(request):
    user = request.user.id

    prop_list = Property.objects.filter(user=user)

    # set up pagination
    p = Paginator(Property.objects.filter(user=user), 3)
    page = request.GET.get('page')
    prop = p.get_page(page)
    return render(request, "estateapp/property-grid.html",
    {
    'prop_list': prop_list,
    'prop': prop
    })

# list single property
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def property_single(request, id):
    prop_single = get_object_or_404(Property, id=id)

    if prop_single:
        return render(request, "estateapp/property-single.html", {"prop_single": prop_single})
    else:
        #return HttpResponse("<h1>You are not allowed to access this content</h1>")
        messages.info(request, "You are not allowed to access this content")
    return render(request, "estateapp/property-single.html", {"prop_single": prop_single})


#list agents
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def agents(request):
    #user = request.user
    agents_list = Agent.objects.all()
    return render(request, "estateapp/property-grid.html", {'agents_list': agents_list})

# single agent detail
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def agent_detail(request, id):
    agt_single = Agent.objects.get(id=id)
    return render(request, "estateapp/agent-single.html", {"agt_single": agt_single})

# search properties
@csrf_exempt
@login_required()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def show_all_properties(request):

    context = {}

    filtered_properties = PropertyFilter(
        request.GET,
        queryset=Property.objects.all()
    )

    context['filtered_properties'] = filtered_properties

    paginated_filtered_properties = Paginator(filtered_properties.qs, 2)
    page_number = request.GET.get('page')
    property_page_obj = paginated_filtered_properties.get_page(page_number)

    context['property_page_obj'] = property_page_obj

    return render(request, 'estateapp/show_all_properties.html', context=context)

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


@csrf_exempt
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    messages.info(request, "You have logged out")
    return redirect('estateapp:index')
