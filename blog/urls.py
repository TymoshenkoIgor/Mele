from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2))/(?P<post>[-\W]+)/$', views.post_detail, name='post_detail'),
]
