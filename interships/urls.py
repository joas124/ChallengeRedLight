from django.urls import re_path
from . import views

urlpatterns = [
    # //
    re_path(r'^$', views.interns_list, name='interns_list'),
    # /{intern_id}/
    re_path(r'^(?P<pk>[0-9]+)/$', views.intern_detail, name='intern_detail'),
    # /{intern_id}/edit/
    re_path(r'^(?P<pk>[0-9]+)/edit/$', views.intern_edit, name='intern_edit'),
    # /insert/
    re_path(r'^insert/$', views.insert, name='insert'),
    # /avatars/{avatar_src}
    re_path(r'^avatars/(?P<path>.*)$', views.avatar, name='avatar'),
]