from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from .models import CatColony

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

    cols = CatColony.objects.all()
    
    #template = loader.get_template('cattrack/colonies.html')
    #context = {}
    #return HttpResponse(template.render(context,request))
    context = {'colonies_list': cols}
    return render(request, 'cattrack/colonies.html', context)
