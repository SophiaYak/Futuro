from django.db import models
from datetime import datetime, timedelta
import pandas as pd
import pandas_datareader.data as web
class UserManager(models.Manager):
	def regchecks(self,post):
		errors = []
		if (User.objects.filter(username=post['user_username'])):
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
		existing = User.objects.filter(username=post['user_username'])
		if not existing:
			errors.append("Username does not exist")
			
		check=User.objects.filter(username=post['user_username'], password = post['user_pass'])
		if not check:
			errors.append("Password did not match")
		if not errors:
			debug = {"succeed": True, "data": check}
		else:
			debug = {"succeed": False, "data": errors}
		return debug
			
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
	def newStock(self, post):
		day_range=7
		end = Stock.objects.mostRecent()
		start= Stock.objects.recentPrior(day_range,end)
		df = web.DataReader(post, "yahoo", start, end)
		# q = web.get_quote_yahoo(post)
		# #df = pd.DataFrame(q)
		# df = pd.DataFrame(q, index = [post])
		# #df= pd.DataFrame(q, index = ['AMZN'], columns = ['PE','change_pct','last','short_ratio','time'])
		# new  = Stock.objects.create(symbol =post, PE= df['PE'][0], \
		# 	change_pct= df['change_pct'][0],  last = df['last'][0],\
		# 	 short_ratio= df['short_ratio'][0],  current_date = df['time'][0])
		# context['companies'] =  info
		# new  = Stock.objects.create(symbol =post, PE= df['PE'][0], \
		# 	change_pct= df['change_pct'][0],  last = df['last'][0],\
		# 	 short_ratio= df['short_ratio'][0],  current_date = df['time'][0])
		add = 0
		for entry in range (0,day_range-1):			
			new  = Stock.objects.create(symbol =post, open_price= df['Open'][entry], \
				high_price= df['High'][entry],  low_price = df['Low'][entry], diff=df['High'][entry]-df['Low'][entry],\
				 adj_close= df['Adj Close'][entry], volume = df['Volume'][entry], current_date = start+timedelta(days=entry))
			add += df['High'][entry]-df['Low'][entry]
		return add/day_range-1
	def mostRecent(self):
		return datetime.today()
	def recentPrior(self,number,start):
		current = start-timedelta(days=number)
		return current

class Stock(models.Model):
	name = models.CharField(max_length=20)
	symbol = models.CharField(max_length=20)
	PE = models.DecimalField(max_digits=6, decimal_places=3,default=0)
	change_pct = models.DecimalField(max_digits=5, decimal_places=5,default=0)
	last = models.DecimalField(max_digits=6, decimal_places=3,default=0)
	short_ratio = models.DecimalField(max_digits=3, decimal_places=2,default=0)
	buying_date = models.DateTimeField(auto_now=False, auto_now_add = False,default= datetime.today())
	past_date = models.DateTimeField(auto_now=False, auto_now_add = False,default= datetime.today())
	current_date = models.DateField(auto_now=False, auto_now_add = False,default= datetime.today())
	open_price= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	high_price= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	low_price= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	close_price= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	adj_close= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	diff= models.DecimalField(max_digits=10, decimal_places=6,default=0)
	volume= models.IntegerField()
	objects = StockManager()


class Basket(models.Model):
	name = models.CharField(max_length=20)
	my_stock= models.ForeignKey(Stock, blank = True, null = True)
	no_shares = models.IntegerField()
	ave_diff= models.DecimalField(max_digits=10, decimal_places=6,default=0)
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

