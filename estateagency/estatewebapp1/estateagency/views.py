from django.shortcuts import render
from .models import Property, Agent

# Create your views here.
def index(request):
    prop_list = Property.objects.all().order_by("-id")
    #agt_list = Agent.objects.all().order_by("name")
    context = {
        'prop_list': prop_list,
        #'agt_list': agt_list
}
    return render(request, "estateagency/index.html", context )

#list property in grid form
def property(request):
    user = request.user.id

    prop_list = Property.objects.filter(user=user)

    # set up pagination
    p = Paginator(Property.objects.filter(user=user), 3)
    page = request.GET.get('page')
    prop = p.get_page(page)
    return render(request, "estateagency/property-grid.html",
    {
    'prop_list': prop_list,
    'prop': prop
    })

def property_single(request, id):
    prop_single = get_object_or_404(Property, id=id)

    if prop_single in request.user.agentuser.all():
        return render(request, "estateagency/property-single.html", {"prop_single": prop_single})
    else:
        #return HttpResponse("<h1>You are not allowed to access this content</h1>")
        messages.info(request, "You are not allowed to access this content")
    return render(request, "estateagency/property-single.html", {"prop_single": prop_single})


#list agents
#@csrf_exempt
#@login_required(login_url='accounts:login')
def agents(request):
    #user = request.user
    agents_list = Agent.objects.all()
    return render(request, "estateagency/agent-grid.html", {'agents_list': agents_list})

# single agent detail
#@csrf_exempt
#@login_required(login_url='accounts:login')
def agent_detail(request, id):
    agt_single = Agent.objects.get(id=id)
    return render(request, "estateagency/agent-single.html", {"agt_single": agt_single})

# search properties
#@csrf_exempt
#@login_required(login_url='login')
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

    return render(request, 'estateagency/show_all_properties.html', context=context)
