from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Stock,Basket


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
def index(request):
	context = {'this_user': request.COOKIES['user']}
	response = render(request, "first_app/index.html", context)

	return response 

def landing(request):
	context = { 'members': User.objects.all()}
	return render(request, "first_app/landing.html",context)

def delete(request):
	User.objects.delete(request.POST['user'])
	return redirect('/')



def basket(request):

	return render(request, "first_app/basket.html")

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




