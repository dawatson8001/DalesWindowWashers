from django.conf.urls import url
import views

urlpatterns = [
    url(r'^comments/$', views.post_list, name='comments'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^post/edit/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^usercomments/$', views.post_user_list, name='user_comments'),
]