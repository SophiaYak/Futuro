from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Stock,Basket
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime, timedelta



#Post to login
def login(request):
	context = {'user_username': request.POST['name'],'user_pass': request.POST['pass']}
	result = User.objects.loginchecks(context)
	userobject = context['user_username']
	response = redirect('/index')
	if result['succeed']:
		response.set_cookie('user',userobject)
		return response
	
	else:
		for error in result['data']:
			messages.error(request, error)
		return redirect('/')
#post to register	
def registration(request):
	context = {'user_username': request.POST['username'], 'user_name': request.POST['name'],\
	'user_email': request.POST['email'],'user_pass': request.POST['pass']}
	result = User.objects.regchecks(context)
	userobject = context['user_username']
	response = redirect('/index')
	if result['succeed']:
		response.set_cookie('user',userobject)
		return response
	
	else:
		for error in result['data']:
			messages.error(request, error)
		return redirect('/')
#dashboard
def index(request):
	context = {'this_user': request.COOKIES['user']}
	response = render(request, "first_app/index.html", context)

	return response 
#first page
def landing(request):
	context = { 'members': User.objects.all()}
	return render(request, "first_app/landing.html",context)
#post to delete a user
def delete(request):
	User.objects.delete(request.POST['user'])
	return redirect('/')
#logouts a user
def logout(request):
	response =  render(request, "first_app/landing.html")
	response.delete_cookie('user')
	return response

def basket(request):
	context = {}
	measure = {}
	
	# response.set_cookie('counts','1')
	# request.session['count'] = int(request.session.get('count',1))+1
	count = int(request.session.get('count',1))+1
	#mycount = int(request.COOKIES['counts'])
	for items in range(0,count):
		measure = { items: ""}
	context = {'items': measure}
	return  render(request, "first_app/basket.html",context)

def addbasket(request):
	context = {'basket_name': request.POST['name']}
	result = Basket.objects.basketchecks(context)
	return redirect('/index')

def deletebasket(request):
	return redirect('/basket')

def viewbasket(request, user_name, basket_name):
	return redirect('/basket')	



def admin(request):
	context = {'members': User.objects.all(), 'companies': Stock.objects.all()}
	return render(request, "first_app/admin.html",context)

def addcompany(request):
	context = {'company_name': request.POST['name'], 'company_symbol': request.POST['symbol'],\
	'company_price': request.POST['price']}
	result = Stock.objects.compchecks(context)
	return redirect('/admin')


def deletecompany(request):
	Stock.objects.delete(request.POST['company_name'])
	return redirect('/admin')

def stock(request):
	context = {}
	key = request.session.keys()
	end = datetime.today()
	start = end-timedelta(days=10)
	for company in key:
		name = request.session.get(company)
		score = Stock.objects.newStock(name,start)
		

	context={'score': score,'all':Stock.objects.all()}
	return render(request, "first_app/stock.html",context)

def lookup( request):
	request.session.flush()
	name = request.POST['symb']
	request.session[ 'symb'] = name

	return redirect('/stock')
def addlookup (request):
	
	response =  redirect('/basket')
	#response.set_cookie('count',int(request.COOKIES['count',1])+1)
	# request.session['count'] = int(request.session.get('count',1))
	return response