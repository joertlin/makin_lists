from django.contrib import admin

from .models import Checklist, ListItem, ListContent
# Register your models here.

class ChecklistAdmin(admin.ModelAdmin):
	"""Formatted to show the list contents."""
	list_display = ('list_id','list_name','date_created',
				'date_completed','user','is_a_complete_list')

class ListContentAdmin(admin.ModelAdmin):
	"""
	Formatting Contents to be shown on the admin page.
	"""
	list_display = ('content_id','list_id','item_quantity','date_checked_off','is_a_checked_off_item')

class ListItemAdmin(admin.ModelAdmin):
	"""
	Formattin an admin view for the ListItem model.  This model contains all of the items in the database.
	"""
	list_display = ('item_id','item_name')

admin.site.register(Checklist,ChecklistAdmin)
admin.site.register(ListItem,ListItemAdmin)
admin.site.register(ListContent,ListContentAdmin)