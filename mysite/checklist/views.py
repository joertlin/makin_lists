#from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.conf.urls import url

from .models import Checklist,Unit,ListItem,ListContent

def index(request):
	ordered_checklists = Checklist.objects.order_by('-date_created')
	context = RequestContext(request,{'ordered_checklists':ordered_checklists})
	
	return render(request, 'checklist/index.html', context)

def detail(request, list_id):
	try:
		filtered_items = ListContent.objects.all().filter(list_id = list_id).order_by('-date_checked_off')
	except filtered_items.DoesNotExist:
		raise Http404("Requested list does not exist.")
	
	checklist = Checklist.objects.get(pk = list_id)
	context = RequestContext(request,{'filtered_items':filtered_items,'checklist':checklist})
	
	return render(request, 'checklist/detail.html', context)

def check_off(request, list_id, content_id):
    l  = get_object_or_404(Checklist, pk=list_id)
    c = get_object_or_404(ListContent, pk=content_id)

    if c.date_checked_off == None:
    	c.date_checked_off = timezone.now()
    else:
    	c.date_checked_off = None
    c.save()
    return redirect('detail',list_id)

def test_jquery(request):
	ordered_checklists = Checklist.objects.order_by('-date_created')
	context = RequestContext(request,{'ordered_checklists':ordered_checklists})
	
	return render(request, 'checklist/test_jquery.html')