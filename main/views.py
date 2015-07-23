from django.shortcuts import render, render_to_response
from main.models import Artists, Albums
from django.template import RequestContext
# Create your views here.


def artist_list(request):
    context = {}

    context['all_artists'] = Artists.objects.all()

    return render_to_response('artist_list.html', context, context_instance=RequestContext(request))

def artist_detail(request, artist_id):
    context = {}

    context['artist'] = Artists.objects.get(artist_id=artist_id)

    return render_to_response('artist_detail.html', context, context_instance=RequestContext(request))