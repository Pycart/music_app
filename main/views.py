# Python
import oauth2 as oauth
import cgi

# Django
from django.shortcuts import render, render_to_response
from main.models import Artists, Albums
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from main.models import CustomUser
from django.contrib.auth.decorators import login_required
import requests

google_token_url = "https://accounts.google.com/o/oauth2/token"
google_auth_url = "https://accounts.google.com/o/oauth2/auth"

def home(request):

    context = {}

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def artist_list(request):
    context = {}

    context['all_artists'] = Artists.objects.all()

    return render_to_response('artist_list.html', context, context_instance=RequestContext(request))

def artist_detail(request, artist_id):
    context = {}

    context['artist'] = Artists.objects.get(artist_id=artist_id)

    return render_to_response('artist_detail.html', context, context_instance=RequestContext(request))


def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = settings.CLIENT_ID
    redirect_uri = "http://127.0.0.1:8000/google_auth/"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri=token_request_uri,
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scope=scope)
    return HttpResponseRedirect(url)

def google_authenticate(request):
    parser = Http()
    login_failed_url = '/'
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseRedirect('{loginfailed}'.format(loginfailed=login_failed_url))

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://127.0.0.1:8000/google_auth"
    params = urllib.urlencode({
        'code':request.GET['code'],
        'redirect_uri':redirect_uri,
        'client_id':settings.CLIENT_ID,
        'client_secret':settings.OAUTH_SECRET,
        'grant_type':'authorization_code'
    })
    headers={'content-type':'application/x-www-form-urlencoded'}
    resp, content = parser.request(access_token_uri, method='POST', body=params, headers=headers)
    token_data = jsonDecode(content)
    resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token_data['access_token']))
    #this gets the google profile!!
    google_profile = jsonDecode(content)
    #log the user in-->
    #HERE YOU LOG THE USER IN, OR ANYTHING ELSE YOU WANT
    #THEN REDIRECT TO PROTECTED PAGE
    return HttpResponseRedirect('/home')
