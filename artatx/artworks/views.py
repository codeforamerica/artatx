from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from artworks.models import Artwork

def index(request, template_name='artworks/index.html'):
    context = {}
    context['artworks'] = Artwork.objects.all()
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))

def view(request, id= None, template_name='artworks/view.html'):
    context = {}
    context['artwork'] = get_object_or_404(Artwork, id=id) 
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))
