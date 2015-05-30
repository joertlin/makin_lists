from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

class Checklist(models.Model):
	"""
	This is the table that identifies lists that the user has generated.
	"""
	list_id = models.AutoField(primary_key  =True)
	list_name = models.CharField(max_length = 10)
	date_created = models.DateTimeField('date list was created')
	date_completed = models.DateTimeField('date list was completed',null = True)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.list_name

	def is_a_complete_list(self):
		if self.date_completed == 'null':
			return False
		else:
			return True 

class ListItems(models.Model):
	"""
	This is the table with all of the lists that users generate.
	"""
	list_id = models.ForeignKey(Checklist)
	item_id = models.ManyToManyField(AllItems)
	item_quantity = models.CharField(max_length = 10)
	date_checked_off = models.DateTimeField('date item was checked off', null = True)
	
	def __str__(self):
		return self.item_quantity

	def is_a_checked_off_item(self):
		if self.date_checked_off == 'null':
			return True
		else:
			return False

class AllItems(models.Model):
	"""
	This is a list of all the items users have ever input into any list.
	"""
	item_id = models.AutoField(primary_key = True)
	item_name = models.CharField(max_length = 10)

	def __str__(self):
		return self.item_name