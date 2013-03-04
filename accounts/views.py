from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponse
from django.template import RequestContext
import django.contrib.auth as auth

def login(request):
    if request.POST:
        try:
            identifier = request.POST['identifier']
            password = request.POST['password']
        except KeyError:
            return HttpResponseBadRequest('Enter your email or phone and a password.')
        user = auth.authenticate(identifier=identifier, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                if 'next' in request.POST and request.POST['next']:
                    print 'next = ', request.POST['next']
                    return redirect(request.POST['next'])
                else: return redirect('/')
        else: return HttpResponseBadRequest('Invalid credentials.')
    template_vars = {
        'next': request.GET.get('next', ''),
    }
    return render_to_response('login.html', template_vars,
        context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect('/')

def create_account(request):
    return render_to_response('create_account.html', {},
        context_instance=RequestContext(request))