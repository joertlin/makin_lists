from django.contrib import admin

from .models import Checklist, ListItem, ListContent
# Register your models here.

class ChecklistAdmin(admin.ModelAdmin):
	"""Formatted to show the list contents."""
	list_display = ('list_id','list_name','date_created',
				'date_completed','user','is_a_complete_list')
	
class ChecklistInline(admin.TabularInline):
    model = Checklist

class ListContentAdmin(admin.ModelAdmin):
	"""
	Formatting Contents to be shown on the admin page.
	"""
	#inline = (ChecklistInline,)
	list_display = ('list_id','item_quantity','date_checked_off')



admin.site.register(Checklist,ChecklistAdmin)
admin.site.register(ListItem)
admin.site.register(ListContent,ListContentAdmin)