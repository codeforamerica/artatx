from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from artworks.models import Artwork

def index(request, template_name='artworks/index.html'):
    context = {}
    context['artworks'] = Artwork.objects.all()
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))

def level(request, level=None, template_name='artworks/level.html'):
    context = {}
    context['artworks'] = Artwork.objects.filter(level=level)
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))

def view(request, id=None, template_name='artworks/view.html'):
    context = {}
    prev_id = int(id) - 1
    context['prev_id'] = prev_id if id > 0 else None 
    context['artwork'] = get_object_or_404(Artwork, id=id) 
    next_id = int(id) + 1
    context['next_id'] = next_id if Artwork.objects.filter(id=next_id).exists() else None 
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))
