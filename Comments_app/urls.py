from django.conf.urls import url
import views

urlpatterns = [
    url(r'^comments/$', views.post_list, name='comments'),
    url(r'^new_post/$', views.new_comment, name='new_comment'),
    url(r'^edit/(?P<post_id>\d+)/$', views.edit_comment, name='edit_comment'),
    url(r'^usercomments/$', views.post_user_list, name='user_comments'),
    url(r'^post/delete/(?P<post_id>\d+)/$', views.delete_comment, name='delete_comment'),
]