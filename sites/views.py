
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import os

@login_required
def list(request):
    username = request.user.username
    try:
        sitesdir = '/home/%s/sites/' % username
        sites = os.listdir(sitesdir)
    except OSError:
        sites = []

    return render_to_response('sites/list.html', {'sites': sites}, context_instance=RequestContext(request))
