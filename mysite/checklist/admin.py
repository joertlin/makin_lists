from django.contrib import admin

from .models import Checklist, ListItem, ListContent, Unit
# Register your models here.

class ChecklistAdmin(admin.ModelAdmin):
	"""Formatted to show the list contents."""
	list_display = ('list_id','list_name','date_created',
				'date_completed','user','is_a_complete_list')
	search_fields = ('list_name',)
class ListContentAdmin(admin.ModelAdmin):
	"""
	Formatting Contents to be shown on the admin page.
	"""
	list_display = ('content_id','list_id','item_id','item_quantity','unit_name','date_checked_off','is_a_checked_off_item')
	#search_fields = ('list_id',)
class ListItemAdmin(admin.ModelAdmin):
	"""
	Formatting an admin view for the ListItem model.  This model contains all of the items in the database.
	"""
	list_display = ('item_id','item_name')

class UnitAdmin(admin.ModelAdmin):
	"""
	Formatting a list of units that are available to the user.
	"""
	list_display = ('unit_id','unit_name')

admin.site.register(Checklist,ChecklistAdmin)
admin.site.register(ListItem,ListItemAdmin)
admin.site.register(ListContent,ListContentAdmin)
admin.site.register(Unit,UnitAdmin)