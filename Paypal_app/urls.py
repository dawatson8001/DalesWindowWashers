from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
import views

urlpatterns = [

    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', views.paypal_return),
    url(r'^paypal-cancel', views.paypal_cancel),


]