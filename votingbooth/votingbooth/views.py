from django.http import HttpResponse, HttpResponseRedirect, HttpRequest

def redirect_to_home(request):
    return HttpResponseRedirect('admin')