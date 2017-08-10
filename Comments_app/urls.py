from django.conf.urls import url
import views

urlpatterns = [
    url(r'^Comments/$', views.post_list, name='comments'),
    url(r'^post/new/$', views.new_post, name='new_post'),
]