from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

class Checklist(models.Model):
	"""
	This is the table that identifies lists that the user has generated.
	"""
	list_id = models.AutoField(primary_key  = True)
	list_name = models.CharField(max_length = 10)
	date_created = models.DateTimeField('date list was created')
	date_completed = models.DateTimeField('date list was completed',null = True,blank = True)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.list_name

	def is_a_complete_list(self):
		if self.date_completed == None:
			return False
		else:
			return True 
	is_a_complete_list.admin_order_field = 'date_completed'
	is_a_complete_list.boolean = True
	is_a_complete_list.short_description = 'Was the list finished?'


class ListItem(models.Model):
	"""
	This is a list of all the items users have ever input into any list.
	"""
	item_id = models.AutoField(primary_key = True)
	item_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.item_name

class Unit(models.Model):
	"""
	This is a list of availalble units.
	"""
	unit_id = models.AutoField(primary_key = True)
	unit_name = models.CharField(max_length = 4)

	def __str__(self):
		return self.unit_name

class ListContent(models.Model):
	"""
	This is the table with all of the lists that users generate.
	"""
	content_id = models.AutoField(primary_key  = True)
	list_id = models.ForeignKey(Checklist, db_column = 'list_id')
	item_id = models.ForeignKey(ListItem, db_column = 'item_id')
	item_quantity = models.FloatField('number of units')
	unit_name = models.ForeignKey(Unit,default = 1)
	date_checked_off = models.DateTimeField('date item was checked off', null = True,blank = True)

	def is_a_checked_off_item(self):
		if self.date_checked_off == None:
			return False
		else:
			return True
	is_a_checked_off_item.admin_order_field = 'date_checked_off'
	is_a_checked_off_item.boolean = True
	is_a_checked_off_item.short_description = 'Item checked off?'