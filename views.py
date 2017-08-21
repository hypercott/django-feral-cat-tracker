from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.views.generic import DetailView
from django.db.models import Q
from .models import Cat,CatColony

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)

    template = loader.get_template('cattrack/index.html')
    context = {}
    return HttpResponse(template.render(context,request))


def colonies(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)

    cols = CatColony.objects.filter(~Q(colony_name = "None"))
    
    #template = loader.get_template('cattrack/colonies.html')
    #context = {}
    #return HttpResponse(template.render(context,request))
    context = {'colonies_list': cols}
    return render(request, 'cattrack/colonies.html', context)

#class ColonyDetail(DetailView):
#    model = CatColony

def colony_detail(request,pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(settings.LOGIN_URL)

    col = CatColony.objects.get(pk=pk)
    cats = Cat.objects.filter(cat_colony=pk)

    context = {'catcolony' : col,
               'cats' : cats}
    return render(request, 'cattrack/catcolony_detail.html',context)

