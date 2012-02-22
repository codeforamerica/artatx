from django.shortcuts import render_to_response
from django.template import RequestContext

from artworks.models import Artwork

def index(request, template_name='home/index.html'):
    context = {}
    context['artworks'] = Artwork.objects.all()
    return render_to_response(template_name, context,
        context_instance=RequestContext(request))
