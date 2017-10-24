from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.landing),
    url(r'^index$',views.index),
	url(r'^basket$',views.basket),
	url(r'^login$',views.login),
	url(r'^registration$',views.registration),
	url(r'^delete$',views.delete),
	url(r'^admin$',views.admin),
	url(r'^addcompany$',views.addcompany),
	url(r'^deletecompany$',views.deletecompany),
	url(r'^(?P<user_name>)/(?P<bakset_name>)$',views.viewbasket),
	url(r'^deletebasket$',views.deletebasket),
	url(r'^addbasket$',views.addbasket),
	url(r'^logout$',views.logout),
	url(r'^stock$',views.stock),

]
