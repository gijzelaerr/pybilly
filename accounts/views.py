from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import unixuser

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/logout/')

def login(request):
    return HttpResponseRedirect('/')


@login_required
def details(request):
    username = request.user.username
    user = unixuser.details(username)
    return render_to_response('accounts/details.html',
			{'user': user},
			context_instance=RequestContext(request)
	)


