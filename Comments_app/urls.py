from django.conf.urls import url
import views

urlpatterns = [
    url(r'^comments/$', views.post_list),
]