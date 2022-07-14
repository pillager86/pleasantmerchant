from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse
from .models import Item

@user_passes_test(lambda u: u.is_authenticated)
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

@user_passes_test(lambda u: u.is_authenticated)
def item_list_view(request):
    if(not request.user.has_perms(["inventory.view_item"])):
        return redirect('permissiondenied')
    items = Item.objects.all()
    template = loader.get_template('items.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))

def permission_denied_view(request):
    template = loader.get_template('permissiondenied.html')
    return HttpResponse(template.render({}, request))

def logout_view(request):
    logout(request)
    messages.info(request, 'You have logged out successfully')
    return redirect("login")
