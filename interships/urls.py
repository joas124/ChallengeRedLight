from django.urls import re_path
from . import views

urlpatterns = [
    # //
    re_path(r'^$', views.interns_list, name='interns_list'),
    # /intern/{intern_id}/
    re_path(r'^intern/(?P<pk>[0-9]+)/$', views.intern_detail, name='intern_detail'),
    # /intern/{intern_id}/edit/
    re_path(r'^intern/(?P<pk>[0-9]+)/edit/$', views.intern_edit, name='intern_edit'),
    # /intern/{intern_id}/insertrole/
    re_path(r'^intern/(?P<pk>[0-9]+)/addstatus/$', views.intern_addstatus, name='intern_addstatus'),
    # /intern/{intern_id}/rolestatus/{rolestatus_id}/edit/
    re_path(r'^intern/(?P<pk>[0-9]+)/rolestatus/(?P<rolestatus_pk>[0-9]+)/edit/$', views.intern_editstatus, name='intern_editstatus'),
    # /intern/{intern_id}/rolestatus/{rolestatus_id}/delete/
    re_path(r'^intern/(?P<pk>[0-9]+)/rolestatus/(?P<rolestatus_pk>[0-9]+)/delete/$', views.intern_deletestatus, name='intern_deletestatus'),
    # /intern/{intern_id}/delete/
    re_path(r'^intern/(?P<pk>[0-9]+)/delete/$', views.intern_delete, name='intern_delete'),
    # /role/{role_id}/
    re_path(r'^role/(?P<pk>[0-9]+)/$', views.role_detail, name='role_detail'),
    # /role/{role_id}/edit/
    re_path(r'^role/(?P<pk>[0-9]+)/edit/$', views.role_edit, name='role_edit'),
    # /role/{role_id}/delete/
    re_path(r'^role/(?P<pk>[0-9]+)/delete/$', views.role_delete, name='role_delete'),
    # /insert/intern
    re_path(r'^insert/intern$', views.insertIntern, name='insert_intern'),
    # /insert/role
    re_path(r'^insert/role$', views.insertRole, name='insert_role'),
    # /avatars/{avatar_src}
    re_path(r'^intern/(?P<path>.*)$', views.avatar, name='avatar'),
]