from django.db import models
import datetime
class UserManager(models.Manager):
	def regchecks(self,post):
		errors = []
		if (User.objects.filter(username=post['user_username'])) =={}:
			errors.append("Username is already being used")
		if not errors:
			new = User.objects.create(username = post['user_username'],\
			 password = post['user_pass'], name= post['user_name'], \
			 email= post['user_email'], sum_invested=0, sum_profit=0)
			debug = {"succeed": True, "data": new}
		else:
			debug = {"succeed": False, "data": errors}
		return debug

	def loginchecks(self,post):
		errors = []
		
		if  (User.objects.filter(username=post['user_username'])) =={}:
			errors.append("Username does not exist")
			return {"succeed": False, "data": errors}
		check=User.objects.filter(username=post['user_username']).filter(password = post['user_pass'])
		if  check =={}:
			errors.append("Password did not match")
			return {"succeed": False, "data": errors}
		else:
			return {"succeed": True, "data": check}
	def getObject(self, post):
		return  User.objects.get(username = post)

	def delete(self, post):
		User.objects.filter(username =post).delete()
class BasketManager(models.Manager):
	errors = []
	def basketchecks(self,post):
		new = Basket.objects.create(name= post['basket_name'])
		return {"succeed": True, "data": new}
class StockManager(models.Manager):
	errors = []
	def delete(self, post):
		Stock.objects.filter(name =post).delete()
	def compchecks(self,post):
		new = Stock.objects.create(name = post['company_name'],\
			symbol = post['company_symbol'], price= post['company_price'])
		return {"succeed": True, "data": new}

class Stock(models.Model):
	name = models.CharField(max_length=20)
	symbol = models.CharField(max_length=20)
	PE = models.DecimalField(max_digits=None, decimal_places=3)
	change_pct = models.DecimalField(max_digits=None, decimal_places=5)
	last = models.DecimalField(max_digits=None, decimal_places=3)
	short_ratio = models.DecimalField(max_digits=None, decimal_places=2)
	buying_date = models.DateTimeField(auto_now=False, auto_now_add = False,default= datetime.date.today())
	current_date = models.DateTimeField(auto_now=False, auto_now_add = False,default= datetime.date.today())
	objects = StockManager()

class Basket(models.Model):
	name = models.CharField(max_length=20)
	my_stock= models.ForeignKey(Stock, blank = True, null = True)
	no_shares = models.IntegerField()
	profit = models.FloatField()
	invested = models.FloatField()
	objects = BasketManager()
class User(models.Model):
	name = models.CharField(max_length=20)
	username = models.CharField(max_length=15)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	sum_invested = models.FloatField()
	sum_profit = models.FloatField()
	my_basket = models.ForeignKey(Basket, blank = True, null = True)
	objects=UserManager()

