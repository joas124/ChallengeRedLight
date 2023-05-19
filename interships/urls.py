from django.urls import re_path
from . import views

urlpatterns = [
    # /home/
    re_path(r'^$', views.interns_list, name='interns_list'),
    # /home/{intern_id}/
    re_path(r'^(?P<pk>[0-9]+)/$', views.intern_detail, name='intern_detail'),
]