from django.conf.urls import  url
import views

urlpatterns = [

    url(r'^products/$', views.all_products, name='products')

]