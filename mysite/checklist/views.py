#from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Checklist,Unit,ListItem,ListContent

def index(request):
	ordered_checklists = Checklist.objects.order_by('-date_created')
	context = RequestContext(request,{'ordered_checklists':ordered_checklists})
	
	return render(request, 'checklist/index.html', context)

def detail(request, list_id):
	try:
		filtered_items = ListContent.objects.all().filter(list_id = list_id)
	except filtered_items.DoesNotExist:
		raise Http404("Requested list does not exist.")
	
	checklist = Checklist.objects.get(pk = list_id)
	context = RequestContext(request,{'filtered_items':filtered_items,'checklist':checklist})
	
	return render(request, 'checklist/detail.html', context)