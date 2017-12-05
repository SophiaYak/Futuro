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
	def basketchecks(self,post,stock):
		new = Basket.objects.create(name= post, my_stock= Stock.objects.createStock(stock))
		return {"succeed": True, "data": new}
class StockManager(models.Manager):
	errors = []
	def delete(self, post):
		Stock.objects.filter(name =post).delete()
	def compchecks(self,post):
		new = Stock.objects.create(name = post['company_name'],\
			symbol = post['company_symbol'], price= post['company_price'])
		return {"succeed": True, "data": new}

	def newStock(self, post, start=datetime.today(), end=datetime.today()):
		# df = web.DataReader(post, "yahoo", start,end)
		# add = 0
		# totalshares=0
		# index = pd.bdate_range(start,end)
		# for entry in index.date:			
		# 	new  = Stock.objects.create(symbol =post, open_price= df['Open'][entry], \
		# 		high_price= df['High'][entry],  low_price = df['Low'][entry], diff=df['High'][entry]-df['Low'][entry],\
		# 		 adj_close= df['Adj Close'][entry], volume = df['Volume'][entry], current_date = index.date[entry])
		# 	add += (df['Volume'][entry]*df['Adj Close'][entry])
		# 	totalshares += df['Volume'][entry]
		# return add/totalshares
		start=end-timedelta(days=10)#one more day than you need
		df = web.DataReader(post, "yahoo", start,end)
		add = 0
		totalshares=0
		index = pd.bdate_range(start,end)
		for events in index.date:
			try:
				value = df.ix[events][3] * df.ix[events][5]
				add += value
				totalshares += df.ix[events][5]
			except (TypeError,KeyError):
				pass

		return add/totalshares


	def createStock(self, post):
		new = Stock.objects.create(name = post[0], score = post[1])



		
	def mostRecent(self):
		return datetime.today()-timedelta(days=1)
	def recentPrior(self,number,start):
		current = start-timedelta(days=number+1)
		return current

class Stock(models.Model):
	name = models.CharField(max_length=20)
	symbol = models.CharField(max_length=20)
	score = models.DecimalField(max_digits=5, decimal_places=2,default=0)
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

