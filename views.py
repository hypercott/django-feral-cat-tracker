from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.db.models import Q
#from django.urls import reverse
from django.core.urlresolvers import reverse
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

    if (pk == "1"):
        context = {'catcolony' : col,
                   'cats' : cats}
        return render(request, 'cattrack/catcolony_none.html',context)
    else:
        context = {'catcolony' : col,
                   'cats' : cats,
                   'pk' : pk}
        return render(request, 'cattrack/catcolony_detail.html',context)
    
class ColonyEditView(UpdateView):
    model = CatColony
    fields = ['colony_name','colony_location_name','colony_street_address',
              'colony_city','colony_state','colony_zip','colony_year_formed',
              'colony_setting','colony_setting_other']
    
    template_name_suffix = '_edit'

#    def get_object(self):
#        return self
    
    def get_success_url(self):
        return reverse('cattrack-colony-detail', kwargs={'pk' : self.object.pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ColonyEditView, self).get_context_data(**kwargs)
        # Add in information on the primary key
        context['pk'] = self.object.pk
        return context
    
