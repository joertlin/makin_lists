#from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

import json

from .models import Checklist,Unit,ListItem,ListContent

def get_filtered_items(list_id):
    #try:
    filtered_items = ListContent.objects.all().filter(list_id = list_id).order_by('-date_checked_off')
    #except filtered_items.DoesNotExist:
    #    raise Http404("Requested list does not exist.")

    return filtered_items

@login_required()
def index(request):
	ordered_checklists = Checklist.objects.filter(user_id = request.user).order_by('-date_created')
	context = RequestContext(request,{'ordered_checklists':ordered_checklists})
	
	return render(request, 'checklist/index.html', context)

@login_required()
def detail(request, list_id):
	filtered_items = get_filtered_items(list_id)
	checklist = Checklist.objects.get(pk = list_id)
	context = RequestContext(request,{'filtered_items':filtered_items,'checklist':checklist})
	
	return render(request, 'checklist/detail.html', context)

@login_required()
def check_off(request, list_id, content_id):
    l  = get_object_or_404(Checklist, pk=list_id)
    c = get_object_or_404(ListContent, pk=content_id)

    if c.date_checked_off == None:
    	c.date_checked_off = timezone.now()
    else:
    	c.date_checked_off = None
    c.save()

    filtered_items = get_filtered_items(list_id)
    completion = []

    for filtered_item in filtered_items:
        #print filtered_item.date_checked_off
        #fc = get_object_or_404(ListContent, pk=filtered_item.content_id)
    
        if filtered_item.date_checked_off == None:
            completion.append(False)
        else:
            #print('test')
            completion.append(True)
    
    if False in completion:
        l.date_completed = None

    else:
        l.date_completed = timezone.now()
    
    l.save()
    
    return redirect('detail',list_id)

@login_required()
def test_jquery(request):
	#ordered_checklists = Checklist.objects.order_by('-date_created')
	#context = RequestContext(request,{'ordered_checklists':ordered_checklists})
	
	return render(request, 'checklist/test_jquery.html')

@login_required()
def add_checklist(request):
    if request.method == 'GET':
        test =  'you\'ve submitted a GET request to add_checklist.  nothing really hapened thou.'

    elif request.method == 'POST':
        test =  'POST Data:' +  request.POST['checklist_name'] + ' user: ' + 'jeremiah'
        #u = User.objects.get(username = 'jeremiah')
        u = request.user
        c = Checklist(list_name = request.POST['checklist_name'], date_created = timezone.now(), user = u)
        c.save()

        entry = {'list_name': request.POST['checklist_name'],'pk': c.list_id}

        return HttpResponse( json.dumps(entry) )

    return HttpResponse(test)