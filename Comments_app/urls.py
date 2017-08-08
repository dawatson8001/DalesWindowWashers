from django.conf.urls import url
import views

urlpatterns = [
    url(r'^comments/$', views.post_list),
    url(r'^comments/(?P<id>\s+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
]