from django.urls import re_path
from . import views

urlpatterns = [
    # //
    re_path(r'^$', views.interns_list, name='interns_list'),
    # /intern/{intern_id}/
    re_path(r'^intern/(?P<pk>[0-9]+)/$', views.intern_detail, name='intern_detail'),
    # /intern/{intern_id}/edit/
    re_path(r'^intern/(?P<pk>[0-9]+)/edit/$', views.intern_edit, name='intern_edit'),
    # /role/{role_id}/
    re_path(r'^role/(?P<pk>[0-9]+)/$', views.role_detail, name='role_detail'),
    # /insert/intern
    re_path(r'^insert/intern$', views.insertIntern, name='insert'),
    # /insert/role
    re_path(r'^insert/role$', views.insertRole, name='insert'),
    # /avatars/{avatar_src}
    re_path(r'^intern/avatars/(?P<path>.*)$', views.avatar, name='avatar'),
]